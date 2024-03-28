# exercise 1 
students = ['kim', 'ben', 'larry', 'bob']
print(students[1]) #second name 
print(students[-1]) #last name 

# exercise 2 
foods = ('pizza', 'cookie', 'candy', 'apples')

for food in foods:
    print(f'{food} is a good food')

# exercise 3 
food = slice(2)
print(foods[2])
print(foods[3])

# exercise 4
home_town = {
    'city': "irvine",
    'state': "California",
    'population': 8398748
}

city = home_town['city']
state = home_town['state']
population = home_town['population']


print(f'i was born in {city}, {state}, population of {population}')

# exercise 5
for key, value in home_town.items():
    print(f'{key} = {value}')

# exercise 6
cohort = []

for student in students:
    cohort.append(student)

print(cohort)

cohort.append({
    'student' : 'jane',
    'fav_food' : 'kiwi'
})

for index, student in enumerate(students):
  student_food = {'student': student, 'fav_food': foods[index]}
  cohort.append(student_food)

for i in cohort:
  print(i)


#exercise 7

awesome_studnets = students
awesome_students = [f"{student} is awesome!" for student in students]
for student in awesome_students:
    print(student)


#exercise 8
for food in [food for food in foods if 'a' in food.lower()]:
    print(food)