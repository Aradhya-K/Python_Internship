class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and {self.gender}.")

# Example usage:
if __name__ == "__main__":
    person1 = Person("Sita", 40, "female")
    person1.introduce()

    person2 = Person("Ram", 30, "male")
    person2.introduce()
