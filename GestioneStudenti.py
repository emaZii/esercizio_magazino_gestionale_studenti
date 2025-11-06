import studente
import Myjson as json
import studente as stu
import pagella as pg

class GestioneStudenti:

    def caricaStudentiSulJson(self, id, nome, eta,  classroom):
        nuovo_studente = stu.Studente(id=id, name=nome, age=eta, classroom=classroom)
        writer = json.WriteObject()
        writer.WriteOnJson(nuovo_studente)

    def caricaVotieMaterielJson(self,id, materia, voto):
        materie_voti = pg.Pagella(id, materia, voto)
        writer = json.WriteObject()
        writer.WriteOnJson(materie_voti)

    def stampaTuttoJson(self):
        writer = json.WriteObject()
        writer.ReadOnJson("data.json")