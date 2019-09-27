class Person:
    count = 0
    avg_age = 70
    def __init__(self,name):
        print("Constructor called !")
        self.name = name
        Person.count = Person.count + 1
    def show(self):
        print("Name of person : ",self.name)
    @staticmethod
    def showCount():
        print("Total count : ",Person.count)
    @classmethod
    def set_avg_age(cls,ag):
        cls.avg_age = ag
    @classmethod
    def get_avg_age(cls):
        return(cls.avg_age)
    

#

p1 = Person("person 1")
p1.show()
p1.showCount()
Person.set_avg_age(60)
print("New average age is : ",Person.get_avg_age())
