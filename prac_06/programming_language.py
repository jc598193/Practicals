# Creat ProgrammingLanguage class
class ProgrammingLanguage:

    def __init__(self, field, typing, reflection, year):
        """" Represent details of programming language Object"""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """" Check this is dynamic typed or not"""
        if self.typing == 'Dynamic':
            return True

    def __str__(self):
        """" Return details of the objects in string method"""
        return '{}, {} Typing, Reflection = {}, First appeared in {}'.format(self.field, self.typing, self.reflection,
                                                                             self.year)
