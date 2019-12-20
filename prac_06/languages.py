# Import Class
from prac_06.programming_language import ProgrammingLanguage


def main():
    """" Value"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    """" Add value to class """
    languages = [ruby, python, visual_basic]
    print('The dynamically typed languages are: ')
    """" Loop for dynamic typing"""
    for language in languages:
        if language.is_dynamic():
            print('{}'.format(language.field))
    """ Loop for print languages"""
    for each in languages:
        print(each)


if __name__ == '__main__':
    main()
