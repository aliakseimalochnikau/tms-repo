from person import Person

my_friends = [Person('Bill Stevens', 40, 'M'),
              Person('Nora Folks', 32, 'F'),
              Person('Stanley White', 26, 'M')]


def get_oldest_person(lst):
    oldest = None
    for person in lst:
        if oldest is None or person.age > oldest.age:
            oldest = person
    return oldest


def get_male_person(lst):
    return [person for person in lst if person.gender == 'M']


print('My friends are: ')
for friend in my_friends:
    friend.print_person_info()

print()
print('The oldest friend is: ')
oldest_friend = get_oldest_person(my_friends)
oldest_friend.print_person_info()

print()
print('My male friends are: ')
male_friends = get_male_person(my_friends)
for friend in male_friends:
    friend.print_person_info()
