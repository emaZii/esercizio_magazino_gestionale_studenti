from pagella import Pagella

class Studente:

    #Costruttore
    def __init__(self, id_counter, name, age, classroom, pagella:Pagella):
        self.id_counter = id_counter
        self.name = name
        self.age = age
        self.classroom = classroom
        self.pg = pagella

    def to_dict(self):

        return {
            "id_studente": self.id_counter,
            "nome": self.name,
            "eta": self.age,
            "classe": self.classroom,
            "Pagella": [ self.pg.to_dict(),]
        }

