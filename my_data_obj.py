import json
import os

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
            print("Entry added successfully!")
        else:
            self.write_data(new_entry)
            print("Entry added successfully!")

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

    def delete(self, key, value):
        """
        <summary>
            Cancella i dati che combaciano a chiave e valore.
        </summary>
        """
        data = self.read_data()
        updated_data = [entry for entry in data if entry.get(key) != value]
        if len(data) != len(updated_data):
            self.write_data(updated_data)
            print("Entry deleted successfully!")
        else:
            print("Entry not found!")

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

        studenti_filtrati = []

        for studente in data:
            if "classe" in studente and studente["classe"] == nome_classe:
                studenti_filtrati.append(studente)

        for studente in studenti_filtrati:
            print(f"Studente: {studente}")

        return studenti_filtrati

    def MediaDeiVoti(self):

        data = self.read_data()

        # Lista di studenti con nome e voto
        studenti = []
        somma = 0

        for studente in data:
            nome = studente["nome"]
            voto = studente["valutazione"]
            studenti.append((nome, voto))
            somma += voto

        # Calcolo la media
        media = somma / len(studenti)
        print("Media dei voti:", round(media, 2))

        #riordina l array dallo studente col voto piu piccolo al piu grande
        for i in range(len(studenti)):
            for j in range(i + 1, len(studenti)):
                if studenti[i][1] > studenti[j][1]:
                    studenti[i], studenti[j] = studenti[j], studenti[i]

        # Tre studenti con i voti più bassi
        print("Tre studenti con voti più bassi:")
        print(studenti[0][0], ":", studenti[0][1])
        print(studenti[1][0], ":", studenti[1][1])
        print(studenti[2][0], ":", studenti[2][1])

        # Tre studenti con i voti più alti
        print("Tre studenti con voti più alti:")
        print(studenti[-1][0], ":", studenti[-1][1])
        print(studenti[-2][0], ":", studenti[-2][1])
        print(studenti[-3][0], ":", studenti[-3][1])



    def queryStudenteMateria(self,nome_studente, materia):

        data = self.read_data()

        for studente in data:
            if studente["nome"] == nome_studente:
                print(f"Studente: {studente}")
                print(f"Materia: {materia} {studente['valutazione']}")
