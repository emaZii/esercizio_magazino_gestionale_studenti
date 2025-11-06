import json
import os

class WriteObject:

    def WriteOnJson(self, data):
            file_path = "data.json"
            existing_data = []

            # Se il file esiste, leggi il contenuto esistente
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                        try:
                            existing_data = json.load(file)
                        except json.JSONDecodeError:
                            # File vuoto o malformato: parti da lista vuota
                            existing_data = []

                # Aggiungi o aggiorna i dati
                # Se `existing_data` è una lista:
                if isinstance(existing_data, list):
                    existing_data.append(data)
                # Se invece è un dizionario, puoi aggiornare le chiavi:
                elif isinstance(existing_data, dict) and isinstance(data, dict):
                    existing_data.update(data)
                else:
                    # In caso di formato inaspettato, sovrascrivi
                    existing_data = data

                # Riscrivi il file aggiornato
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(existing_data, file, indent=4, ensure_ascii=False, cls=CustomEncoder)

    def ReadOnJson(self):
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def QueryOnJson(self, key_name, default_value):
        with open("data.json", "r") as file:
            data = json.load(file)
            result = data.get(key_name, default_value)
            return result


#decoder
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()
        return super().default(o)
