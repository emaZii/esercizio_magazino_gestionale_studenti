import my_data_obj as json
import studente as stu
import pagella as pg

class GestioneStudenti:

    def caricaStudente(self, id, nome, eta, classroom, materia="", voto=None):
        nuovo_pagella = pg.Pagella(id=id, materia=materia, voto=voto)
        nuovo_studente = stu.Studente(id=id, name=nome, age=eta, classroom=classroom, pagella=nuovo_pagella)
        writer = json.JSONManager("data.json")
        writer.insert(nuovo_studente.to_dict())

    def caricaStudentiVotieMaterieSulJson(self, id, nome, eta,  classroom, materia, voto):
        nuovo_pagella = pg.Pagella(id=id, materia=materia, voto=voto)
        nuovo_studente = stu.Studente(id=id, name=nome, age=eta, classroom=classroom, pagella=nuovo_pagella)
        writer = json.JSONManager("data.json")
        writer.insert(nuovo_studente.to_dict())

    def caricaVotieMaterielJson(self,id, materia, voto):
        materie_voti = pg.Pagella(id, materia, voto)
        writer = json.JSONManager("data.json")
        writer.query(id, materia)

    def stampaTuttoJson(self):
        reader = json.JSONManager("data.json")
        data = reader.read_data()
        print(data)
