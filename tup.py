people = (('Alice', 30), ('Bob', 25), ('Charlie', 35))

sorted_people = sorted(people, key=lambda person: person[1], reverse=True)

sorted_people = tuple(sorted_people)

print(sorted_people)
