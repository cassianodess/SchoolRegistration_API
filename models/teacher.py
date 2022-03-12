class Teacher():
    def __init__(self, id: str, name: str, subject: str):
        self.id = id if id else None
        self.name = name
        self.subject = subject

    def parse(self) -> dict:
        return self.__dict__
