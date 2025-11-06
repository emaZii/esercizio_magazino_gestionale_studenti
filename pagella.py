import voto
import studente as Studente
import voto as Voto
import json

class Pagella:

    def __init__(self, id, materia, voto=None):
        self.id = id
        self.materia = materia
        self.valutazioni = []
        if voto is not None:
            self.valutazioni.append(voto)

    def to_dict(self):
        return {
            "id": self.id,
            "materia": self.materia,
            "valutazione": self.valutazioni
        }


