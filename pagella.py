import voto
import studente as Studente
import voto as Voto
import json

class Pagella:

    def __init__(self, id_counter, materia, voto):
        self.id_counter = id_counter
        self.materia = materia
        self.voto = voto

    def to_dict(self):
        return {
            "id_valutazione": self.id_counter,
            "materia": self.materia,
            "valutazione": self.voto
        }