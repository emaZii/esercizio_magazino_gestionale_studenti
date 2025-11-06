import voto
import studente as Studente
import voto as Voto

class Pagella:

    def __init__(self, studente: Studente, voto: Voto):
        self.id = studente.id
        self.materia = voto.materia
        self.voto = voto.valuta
