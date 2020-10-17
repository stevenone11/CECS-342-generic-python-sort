# We will demonstarate the use of the sorted() and 
# the .sort() function to sort an array in python.
# Given a key function it can be used as a generic sort.


# Person class to be used in the generic sort program.
class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    # String representation of the Person class.
    def __repr__(self):
        return '{}: {} : age {}'.format(self.__class__.__name__, 
                                        self.name, 
                                        self.age)


# List of numbers followed by the .sort() function.
nums = [645.32, 37.40, 76.30, 5.40, -34.23, 1.11, -34.94, 23.37, 635.46, -876.22, 467.73, 62.26]
nums.sort()
print("Sorted list of numbers:\n{0:}\n".format(nums))


# People is a list of Person objects that we will sort.
People = [Person("Hal", 20), Person("Susann", 31), Person("Dwight", 19), Person("Kassandra", 21), Person("Lawrence", 25), Person("Cindy", 22), Person("Cory", 27), Person("Mac", 19), Person("Romana", 27), Person("Doretha", 32), Person("Danna", 20), Person("Zara", 23), Person("Rosalyn", 26), Person("Risa", 24), Person("Benny", 28), Person("Juan", 33), Person("Natalie", 25)]


# We want to sort by their names first
# so only their name attribute is required.
# Does not include the age attribute
# because it does not matter in this case.
# Note: sorted() returns a new sorted list.
func = lambda person: (person.name, person.age)
People.sort(key=func)

# print the sorted list
print("People sorted by name:")
for p in People:
    print(p)


# Because we want to sort people by the age, we pass a 
# function (or lambda expression) to obtain the sorting
# criteria that we want (descending by age, ascending by name).
# The key will first reverse sort by age and if the ages are equal,
# we will sort by the names of the individuals by using the str
# .lower() function to ignore uppercase.
func2 = lambda person: (- person.age, person.name)
People.sort(key=func2)
# the 'key=' requires what arguments the 
# list should be sorted by, which is why we made a 
# lambda expression to sort in descending order
# by age first, then ascending by name if they are equal.

# print the list
print("\nPeople sorted by their age:")
for p in People:
    print(p)
