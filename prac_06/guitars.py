# Creat guitar class
class Guitar:
    def __init__(self, name, year, cost, age=0):
        """ Initialise a Guitar instance.
           year: float show the year the guitar was born
           cost: float how much the guitar is
           age: for get_age function and is_vantage function
               """
        self.name = name
        self.year = year
        self.cost = cost
        self.age = age

    def get_age(self):
        """Count the age of the guitar"""
        self.age = 2018 - self.year
        return self.age

    def is_vintage(self):
        """Try to find out this is vintage or not"""
        if self.age >= 50:
            return True
        else:
            return False

    def __str__(self):
        """Print the details of the guitar in string """
        return '{} ({}) : ${}'.format(self.name, self.year, self.cost)
