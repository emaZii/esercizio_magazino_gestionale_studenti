import pandas as pd
import os

'''
<summary>
    ---Classe che legge e gestisce i CSV---
</summary>
'''
class CSVReader:
    """
    <summary>
        Classe per leggere file CSV usando pandas in modo sicuro e riutilizzabile.
    <summary>
    """
    def __init__(self, file_path: str, sep: str = ",", encoding: str = "utf-8"):
        self.file_path = file_path
        self.sep = sep
        self.encoding = encoding
        self.dataframe = None

    def validate_file(self) -> bool:
        """
        <summary>
            Controlla se il file esiste e ha estensione .csv
        <summary>
        """
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"File non trovato: {self.file_path}")
        if not self.file_path.lower().endswith(".csv"):
            raise ValueError("Il file deve avere estensione .csv")
        return True

    def load_data(self) -> pd.DataFrame:
        """
        <summary>
            Legge il file CSV in un DataFrame pandas.
        </summary>
        """
        self.validate_file()
        self.dataframe = pd.read_csv(self.file_path, sep=self.sep, encoding=self.encoding)
        return self.dataframe

    def get_head(self, n: int = 5) -> pd.DataFrame:
        """
        <summary>
            Restituisce le prime n righe del DataFrame.
        </summary>
        """
        if self.dataframe is None:
            raise ValueError("I dati non sono stati caricati")
        return self.dataframe.head(n)

    def get_info(self):
        """
        <summary>
            Mostra informazioni sul DataFrame.
        </summary>
        """
        if self.dataframe is None:
            raise ValueError("I dati non sono stati caricati")
        return self.dataframe.info()

    def csv_to_json(csv_path, json_path, orient="records"):
        """
        <summary>
            Legge un file CSV e lo salva come JSON.
        </summary>
        """
        # Controllo esistenza file
        if not os.path.isfile(csv_path):
            raise FileNotFoundError(f"Il file CSV '{csv_path}' non esiste.")
        # Lettura CSV
        df = pd.read_csv(csv_path)
        # Salvataggio in JSON
        df.to_json(json_path, orient=orient, force_ascii=False, indent=4)

        print(f"Conversione completata: '{json_path}' creato con successo.")

