import studente
import MyDataObj as json
import studente as stu
import pagella as pg

class GestioneStudenti:

    def caricaStudentiSulJson(self, id, nome, eta,  classroom):
        nuovo_pagella = pg.Pagella(id=id, materia="", voto=0)
        nuovo_studente = stu.Studente(id=id, name=nome, age=eta, classroom=classroom, Pagella=nuovo_pagella)
        writer = json.WriteObject()
        writer.WriteOnJson(nuovo_studente)

    def caricaStudentiVotieMaterieSulJson(self, id, nome, eta,  classroom, materia, voto):
        nuovo_pagella = pg.Pagella(id=id, materia=materia, voto=voto)
        nuovo_studente = stu.Studente(id=id, name=nome, age=eta, classroom=classroom, Pagella=nuovo_pagella)
        writer = json.WriteObject()
        writer.WriteOnJson(nuovo_studente)

    def caricaVotieMaterielJson(self,id, materia, voto):
        materie_voti = pg.Pagella(id, materia, voto)
        writer = json.WriteObject()
        writer.WriteOnJson(materie_voti)

    def stampaTuttoJson(self):
        writer = json.WriteObject()
        writer.ReadOnJson("data.json")