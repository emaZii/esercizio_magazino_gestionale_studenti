import MyDataObj as json
import studente as stu
import pagella as pg

class GestioneStudenti:

    def caricaStudente(self, id, nome, eta, classroom, materia="", voto=None):
        nuovo_pagella = pg.Pagella(id=id, materia=materia, voto=voto)
        nuovo_studente = stu.Studente(id=id, name=nome, age=eta, classroom=classroom, Pagella=nuovo_pagella)
        writer = json.WriteObject()
        writer.WriteOnJson(nuovo_studente.to_dict())

    def caricaStudentiVotieMaterieSulJson(self, id, nome, eta,  classroom, materia, voto):
        nuovo_pagella = pg.Pagella(id=id, materia=materia, voto=voto)
        nuovo_studente = stu.Studente(id=id, name=nome, age=eta, classroom=classroom, Pagella=nuovo_pagella)
        writer = json.WriteObject()
        writer.WriteOnJson(nuovo_studente.to_dict())

    def caricaVotieMaterielJson(self,id, materia, voto):
        materie_voti = pg.Pagella(id, materia, voto)
        writer = json.WriteObject()
        writer.WriteOnJson(materie_voti)

    def stampaTuttoJson(self, dataobj):
        reader = dataobj.WriteObject()
        data = reader.ReadOnJson()
        print(json.dumps(data, indent=4, ensure_ascii=False))
