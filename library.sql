-- Авторы
CREATE TABLE author (
  author_id      BIGSERIAL PRIMARY KEY,
  full_name      TEXT NOT NULL,
  birth_year     INT,
  death_year     INT
);

-- Издательства
CREATE TABLE publisher (
  publisher_id   BIGSERIAL PRIMARY KEY,
  name           TEXT NOT NULL UNIQUE,
  country_code   CHAR(2)
);

-- Жанры
CREATE TABLE genre (
  genre_id       BIGSERIAL PRIMARY KEY,
  name           TEXT NOT NULL UNIQUE
);

-- Книги (библиографическая запись)
CREATE TABLE book (
  book_id        BIGSERIAL PRIMARY KEY,
  isbn13         VARCHAR(13) UNIQUE,
  title          TEXT NOT NULL,
  publisher_id   BIGINT REFERENCES publisher(publisher_id),
  publication_year INT,
  language_code  CHAR(2),
  pages          INT,
  created_at     TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Связь книга-автор (many-to-many)
CREATE TABLE book_author (
  book_id        BIGINT NOT NULL REFERENCES book(book_id) ON DELETE CASCADE,
  author_id      BIGINT NOT NULL REFERENCES author(author_id) ON DELETE CASCADE,
  PRIMARY KEY (book_id, author_id)
);

-- Связь книга-жанр (many-to-many)
CREATE TABLE book_genre (
  book_id        BIGINT NOT NULL REFERENCES book(book_id) ON DELETE CASCADE,
  genre_id       BIGINT NOT NULL REFERENCES genre(genre_id) ON DELETE CASCADE,
  PRIMARY KEY (book_id, genre_id)
);

-- Филиалы
CREATE TABLE branch (
  branch_id      BIGSERIAL PRIMARY KEY,
  name           TEXT NOT NULL,
  address        TEXT
);

-- Экземпляры книги (инвентарь)
CREATE TABLE copy (
  copy_id        BIGSERIAL PRIMARY KEY,
  book_id        BIGINT NOT NULL REFERENCES book(book_id) ON DELETE CASCADE,
  branch_id      BIGINT NOT NULL REFERENCES branch(branch_id) ON DELETE RESTRICT,
  inventory_code VARCHAR(50) NOT NULL UNIQUE,
  status         VARCHAR(16) NOT NULL DEFAULT 'available' 
                 CHECK (status IN ('available','loaned','reserved','lost','damaged')),
  acquired_at    DATE
);

-- Читатели
CREATE TABLE member (
  member_id      BIGSERIAL PRIMARY KEY,
  full_name      TEXT NOT NULL,
  email          TEXT UNIQUE,
  phone          TEXT,
  registered_at  TIMESTAMP NOT NULL DEFAULT NOW(),
  is_active      BOOLEAN NOT NULL DEFAULT TRUE
);

-- Выдачи
CREATE TABLE loan (
  loan_id        BIGSERIAL PRIMARY KEY,
  copy_id        BIGINT NOT NULL REFERENCES copy(copy_id) ON DELETE RESTRICT,
  member_id      BIGINT NOT NULL REFERENCES member(member_id) ON DELETE RESTRICT,
  loaned_at      TIMESTAMP NOT NULL DEFAULT NOW(),
  due_at         DATE NOT NULL,
  returned_at    TIMESTAMP,
  CHECK (returned_at IS NULL OR returned_at >= loaned_at)
);

-- Уникальность: у экземпляра не может быть 2 активных выдач
CREATE UNIQUE INDEX uniq_active_loan_per_copy
  ON loan(copy_id)
  WHERE returned_at IS NULL;

-- Бронирование (очередь по книге, не по экземпляру)
CREATE TABLE reservation (
  reservation_id BIGSERIAL PRIMARY KEY,
  book_id        BIGINT NOT NULL REFERENCES book(book_id) ON DELETE CASCADE,
  member_id      BIGINT NOT NULL REFERENCES member(member_id) ON DELETE RESTRICT,
  queued_at      TIMESTAMP NOT NULL DEFAULT NOW(),
  fulfilled_at   TIMESTAMP,
  canceled_at    TIMESTAMP
);

-- Нельзя иметь две активные брони одной и той же книги у одного читателя
CREATE UNIQUE INDEX uniq_active_reservation_per_member_book
  ON reservation(book_id, member_id)
  WHERE canceled_at IS NULL AND fulfilled_at IS NULL;

-- Штрафы
CREATE TABLE fine (
  fine_id        BIGSERIAL PRIMARY KEY,
  member_id      BIGINT NOT NULL REFERENCES member(member_id) ON DELETE RESTRICT,
  loan_id        BIGINT REFERENCES loan(loan_id) ON DELETE SET NULL,
  amount_cents   INT NOT NULL CHECK (amount_cents > 0),
  reason         TEXT,
  created_at     TIMESTAMP NOT NULL DEFAULT NOW(),
  paid_at        TIMESTAMP


  -- Поиск по названию книги
CREATE INDEX idx_book_title ON book (LOWER(title));

-- Поиск автора по имени
CREATE INDEX idx_author_name ON author (LOWER(full_name));

-- Быстрый фильтр активных читателей
CREATE INDEX idx_member_active ON member (is_active);

-- Поиск по ISBN
CREATE INDEX idx_book_isbn ON book (isbn13);


INSERT INTO branch(name, address) VALUES ('Центральный', 'ул. Главная, 1');

INSERT INTO publisher(name, country_code) VALUES ('Питер', 'RU'), ('O''Reilly', 'US');

INSERT INTO author(full_name) VALUES ('А. С. Пушкин'), ('Лев Толстой');

INSERT INTO genre(name) VALUES ('Роман'), ('Поэзия');


-- :q — параметр поиска (например, '%война%')
SELECT DISTINCT b.book_id, b.title, b.isbn13
FROM book b
LEFT JOIN book_author ba ON ba.book_id = b.book_id
LEFT JOIN author a ON a.author_id = ba.author_id
WHERE LOWER(b.title) LIKE LOWER(:q)
   OR LOWER(a.full_name) LIKE LOWER(:q)
ORDER BY b.title;


-- :book_id, :branch_id
SELECT c.copy_id, c.inventory_code, c.status
FROM copy c
LEFT JOIN loan l ON l.copy_id = c.copy_id AND l.returned_at IS NULL
WHERE c.book_id = :book_id
  AND c.branch_id = :branch_id
  AND c.status = 'available'
  AND l.loan_id IS NULL
ORDER BY c.inventory_code;


-- :book_id
SELECT r.reservation_id, r.member_id, m.full_name, r.queued_at
FROM reservation r
JOIN member m ON m.member_id = r.member_id
WHERE r.book_id = :book_id
  AND r.canceled_at IS NULL
  AND r.fulfilled_at IS NULL
ORDER BY r.queued_at ASC;



-- :copy_id, :member_id, :days (срок, например 14)
-- 1. Проверяем доступность экземпляра
SELECT c.copy_id
FROM copy c
LEFT JOIN loan l ON l.copy_id = c.copy_id AND l.returned_at IS NULL
WHERE c.copy_id = :copy_id
  AND c.status = 'available'
  AND l.loan_id IS NULL
FOR UPDATE;

-- 2. Создаём выдачу
INSERT INTO loan(copy_id, member_id, due_at)
VALUES (:copy_id, :member_id, CURRENT_DATE + (:days || ' days')::interval)
RETURNING loan_id;

-- 3. Обновляем статус экземпляра
UPDATE copy SET status = 'loaned'
WHERE copy_id = :copy_id;


-- :loan_id
-- 1. Закрываем выдачу
UPDATE loan
SET returned_at = NOW()
WHERE loan_id = :loan_id
RETURNING copy_id, due_at;

-- 2. Начисляем штраф (например, 10 руб/день просрочки)
-- (выполнить условно, если просрочка > 0)
WITH delta AS (
  SELECT GREATEST(0, (CURRENT_DATE - l.due_at))::INT AS days_overdue,
         l.member_id, l.loan_id, l.copy_id
  FROM loan l
  WHERE l.loan_id = :loan_id
)
INSERT INTO fine(member_id, loan_id, amount_cents, reason)
SELECT member_id, loan_id, days_overdue * 1000, 'Просрочка возврата'
FROM delta
WHERE days_overdue > 0;

-- 3. Освобождаем экземпляр или резервируем под следующего в очереди
WITH bk AS (
  SELECT c.book_id, c.copy_id
  FROM copy c
  JOIN loan l ON l.copy_id = c.copy_id
  WHERE l.loan_id = :loan_id
),
next_res AS (
  SELECT r.reservation_id, r.member_id
  FROM reservation r
  JOIN bk ON bk.book_id = r.book_id
  WHERE r.canceled_at IS NULL AND r.fulfilled_at IS NULL
  ORDER BY r.queued_at ASC
  LIMIT 1
)
UPDATE copy SET status = CASE WHEN EXISTS (SELECT 1 FROM next_res) THEN 'reserved' ELSE 'available' END
WHERE copy_id = (SELECT copy_id FROM bk);

-- 4. Помечаем резерв исполненным (если был)
UPDATE reservation
SET fulfilled_at = NOW()
WHERE reservation_id = (SELECT reservation_id FROM next_res);


SELECT l.loan_id, m.full_name, m.email, c.inventory_code, b.title,
       (CURRENT_DATE - l.due_at) AS days_overdue
FROM loan l
JOIN member m ON m.member_id = l.member_id
JOIN copy c ON c.copy_id = l.copy_id
JOIN book b ON b.book_id = c.book_id
WHERE l.returned_at IS NULL
  AND l.due_at < CURRENT_DATE
ORDER BY days_overdue DESC;


SELECT b.book_id, b.title, COUNT(*) AS loans
FROM loan l
JOIN copy c ON c.copy_id = l.copy_id
JOIN book b ON b.book_id = c.book_id
WHERE l.loaned_at >= NOW() - INTERVAL '12 months'
GROUP BY b.book_id, b.title
ORDER BY loans DESC
LIMIT 10;


-- :genre_name, :year_from, :year_to
SELECT b.book_id, b.title, b.publication_year
FROM book b
JOIN book_genre bg ON bg.book_id = b.book_id
JOIN genre g ON g.genre_id = bg.genre_id
WHERE g.name = :genre_name
  AND b.publication_year BETWEEN :year_from AND :year_to
ORDER BY b.publication_year, b.title;



);
