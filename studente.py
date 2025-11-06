import pagella as pg

class Studente:

    #Costruttore
    def __init__(self, id, name, age, classroom, Pagella:pg):
        self.id = id
        self.name = name
        self.age = age
        self.classroom = classroom
        self.pg = Pagella

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.name,
            "eta": self.age,
            "classe": self.classroom,
            "materia": self.pg.materia,

        }

