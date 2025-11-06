import voto
import studente

class Pagella:
    def __init__(self, idStudente, Studente, Voto):
        self.idStudente = idStudente
        self.Studente = Studente.id
        self.Voto = Voto.materia
        self.Voto = Voto.valutazione