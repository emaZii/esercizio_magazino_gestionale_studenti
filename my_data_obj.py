import json
import os

class JSONManager:

    def __init__(self, file_path):
        self.file_path = file_path
        # Ensure the file exists
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

    '''
    <summary>
    # vecchio codice non funziona.....non so il perche
        def read_data(self):
            with open(self.file_path, 'r') as file:
                return json.load(file)
                if not isinstance(data, list):
                    data = []
                return data 
    </summary>
    '''
    def update(self, key, value, updated_entry):
        """
        <summary>
            aggiorna un specifico record che combacia chiave valore
        </summary>
        """
        data = self.read_data()
        for entry in data:
            if entry.get(key) == value:
                entry.update(updated_entry)
                self.write_data(data)
                print("Entry updated successfully!")
                return
        print("Entry not found!")

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

    '''
    def query(self, key):
        """
        <summary>
            Query e ritorna i dati che combaciano con chiave valore.
        </summary>
        """
        data = self.read_data()
        results = [entry.get("") for entry in data if key in entry]
        for entry in data:
            for key in entry:
                nome = entry.get("nome")
                eta = entry[key]
                print(f"Nome: {nome}, Età: {eta}")
                results.append((nome, eta))
        return results
    '''

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
            if "classe"in studente and studente["classe"] == nome_classe:
                studenti_filtrati.append(studente)

        for studente in studenti_filtrati:
            print(f"Studente: {studente}")

        return studenti_filtrati