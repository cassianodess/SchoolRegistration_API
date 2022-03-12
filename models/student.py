class Student():
    def __init__(self, id: str, name: str, course: str):
        self.id = id if id else None
        self.name = name
        self.course = course

    def parse(self) -> dict:
        return self.__dict__
