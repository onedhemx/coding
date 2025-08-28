import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('steps.db')
cursor = conn.cursor()

# Удаляем таблицу, если она существует
cursor.execute("DROP TABLE IF EXISTS steps")

# Создаем таблицу
cursor.execute('''
CREATE TABLE steps(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hour INTEGER,
    step INTEGER
)
''')

conn.commit()

try:
    jirni = float(input('введите свой вес: '))
except :
    print('че та не верно, поробуй снова ')
    
kalzashag = 0.04
kal_dla_minus_1_kg = 750

kal_dla_cnijz_vesa = jirni - kal_dla_minus_1_kg

if jirni > 0:
    print(f'для того чтобы избавиться от {jirni} кг нужно сжечь около {kal_dla_cnijz_vesa} кал')
else:
    print('вес не указан или не может равняться нулю ')
    
# Ввод данных для каждого часа
for hour in range(6, 23):
    while True:
        try:
            # Исправлено: убрано повторяющееся "step_count"
            step_count = int(input(f"Введите количество шагов за {hour} часов: "))
            if step_count < 0:
                print("Количество шагов не может быть отрицательным.")
                continue
            cursor.execute('INSERT INTO steps (hour, step) VALUES (?, ?)', (hour, step_count))
            conn.commit()
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

# Исправлено: название столбца в запросе должно быть 'step', а не 'steps'
cursor.execute('SELECT SUM(step) FROM steps')
total_steps = cursor.fetchone()[0]

obsh_kolvo_sojzenih_kal = total_steps - kalzashag

print(f'Общее количество шагов за день: {total_steps}')
print(f"Общее сожжено калорий: {obsh_kolvo_sojzenih_kal} ккал.")

if jirni > 0:
    ostav_kal = kal_dla_cnijz_vesa - kal_dla_cnijz_vesa - obsh_kolvo_sojzenih_kal
    if ostav_kal > 0:
        print(f"Еще нужно сжечь примерно {ostav_kal:.2f} ккал, чтобы избавиться от {jirni} кг.")
    else:
        print("Вы уже достигли или превысили цель по снижению веса!")
else:
    print("Цель по снижению веса не установлена.")


conn.close()
