class Student:
    # private(__), protected(_), public
    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    def get_name(self):
        return self.__name

    def get_dept(self):
        return self.__dept

    def set_name(self, name):
        self.__name = name

    def set_dept(self, dept):
        self.__dept = dept

    def __str__(self, ):
        return self.__name + " " + self.__dept
