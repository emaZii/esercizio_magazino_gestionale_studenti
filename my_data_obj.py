import json
import os
import math

'''
<Summary>   
    Classe che si occupa di fare le Query sul file json
</Summary>
'''
class JSONManager:

    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def read_data(self):
        """
        <summary>
            Leggi tutti i dati da un json
        </summary>
        """
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                data = []
            return data

    def write_data(self, data):
        """
        <summary>
            Scrive dati in un file json
        </summary>
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def insert(self, new_entry):
        """
        <summary>
            Inserisce un nuovo dato
        </summary>
        """

        if os.path.getsize(self.file_path) > 1:
            data = self.read_data()
            data.append(new_entry)
            self.write_data(data)
        else:
            self.write_data(new_entry)
        print("Entry added successfully!")

    def delete_studente(self, name):
        """
        <summary>
            Dato il nome dello studente lo cancella
        </summary>
        """
        data = self.read_data()

        data = [studente for studente in data if studente["nome"] != name]

        self.write_data(data)

    def updatestudentefromname(self, name, materia, voto):
        data = self.read_data()
        updated = False
        for entry in data:
            if entry.get("nome") == name:
                entry['materia'] = materia
                entry['valutazione'] = voto
                updated = True
                break  # Se vuoi aggiornare solo il primo match

        if updated:
            self.write_data(data)

    def etaYoungOld(self, key):
        """
        <summary>
            Query che accetta 'eta' come chiave, stampa nome ed età ordinati dal più giovane al più anziano.
        </summary>
        """
        data = self.read_data()

        filtered = []

        for entry in data:
            if key in entry:
                nome = entry.get("nome")
                valore = entry[key]
                filtered.append((nome, valore))

        sorted_results = sorted(filtered)

        for nome, eta in sorted_results:
            print(f"Nome: {nome}, Età: {eta}")

        return sorted_results


    def classespecifica(self, nome_classe):

        data = self.read_data()

        #studenti_filtrati = []

        for studente in data:
            if "classe" in studente and studente["classe"] == nome_classe:
                print(f"Studente: {studente}")

                #studenti_filtrati.append(studente)

        #for studente in studenti_filtrati:
        #    print(f"Studente: {studente}")

        return studente

    def MediaDeiVoti(self):
        """
        <summary>
            Lista di studenti con nome e voto prendere i tre studenti con la media alta e i tre studenti con la media bassa
        </summary>
        """
        data = self.read_data()
        studenti = []
        somma = 0
        for studente in data:
            nome = studente["nome"]
            voto =[v['valutazione'] for v in studente["Pagella"]]
            somma = sum(voto)
            media = math.ceil(somma / len(voto))
            studenti.append((nome, media))
        studenti.sort(key=lambda x: x[1])
        print("🔻 Tre studenti con media più bassa:")
        print(studenti[:3])
        print("🔺 Tre studenti con media più alta:")
        print(studenti[-3:])

    def queryStudenteMateria(self,nome_studente, materia):

        data = self.read_data()

        for studente in data:
            if studente["nome"] == nome_studente:
                print(f"Studente: {studente}")
                print(f"Pagella: {materia} {studente['valutazione']}")
