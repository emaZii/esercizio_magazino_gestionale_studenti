# gestione_studenti.py

import my_data_obj as json
import studente as stu
import pagella as pg

class GestioneStudenti:

    '''
    <summary>
        carica i dati dello studente dando il voto
    <summary>
    '''
    def caricaStudentiVotieMaterieSulJson(self, id_counter, nome, eta, classroom, materia, voto):
        id_counter += 1
        nuovo_pagella = pg.Pagella(id_counter=id_counter, materia=materia, voto=voto)
        nuovo_studente = stu.Studente(id_counter=id_counter, name=nome, age=eta, classroom=classroom, pagella=nuovo_pagella)
        writer = json.JSONManager("data.json")
        writer.insert(nuovo_studente.to_dict())

    def mediaVoti(self):
        reader = json.JSONManager("data.json")
        data = reader.MediaDeiVoti()
        print(data)

    '''
    <summary>
        Carica i dati dello studente senza dare il voto
    <summary>
    '''
    def caricaStudentiSulJson(self, id_counter, name, eta, classe, materia="",  voto = 0):
        id_counter += 1
        nuovo_pagella = pg.Pagella(id_counter=id_counter, materia=materia, voto=voto)
        nuovo_studente = stu.Studente(id_counter=id_counter, name=name, age=eta, classroom=classe, pagella=nuovo_pagella)
        writer = json.JSONManager("data.json")
        writer.insert(nuovo_studente.to_dict())

