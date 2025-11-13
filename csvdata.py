import pandas as pd
import json
import os

'''
<summary>
    ---Classe che legge e gestisce i CSV---
</summary>
'''
class CSVReader:
    """
    <summary>
        Classe per leggere file CSV usando pandas.
    <summary>
    """
    def __init__(self, file_path: str, sep: str = ";"):
        self.file_path = file_path
        self.sep = sep
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

    def csv_to_json(self, csv_path='dati.csv', json_path='data.json', orient="records"):
        """
        <summary>
            Legge un file CSV e lo salva nel JSON.
        </summary>
        """
        #verifica se il file csv esista
        if not os.path.isfile(csv_path):
            return "Il file CSV non è stato trovato: crea il file 'dati.csv'."

        # verifica se il file json esiste o e vuoto
        if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
            with open(json_path, 'w') as f:
                json.dump([], f, ensure_ascii=False, indent=4)

        #legge il file csv
        idcount = 0

        df = pd.read_csv(csv_path, sep=';')
        df.columns.tolist()
        df.columns = df.columns.str.strip().str.lower()

        #salva i dati del json in una variabile
        with open(json_path, 'r') as f:
            data = json.load(f)

        for index, row in df.iterrows():
            idcount += 1
            nome = row["nome"]
            eta = row["eta"]
            classe = row["classe"]
            header_names = row.keys()
            names_materie = [nome for nome in header_names if nome.startswith("voto")]
            data.append({
                "nome": nome,
                "eta": eta,
                "classe": classe,
                "Pagella":[
                    {
                        "id_valutazione": idcount,
                        "materia": nome_materia,
                        "valutazione": row[nome_materia]
                    } for nome_materia in names_materie
                ]
            })

        #salva i dati uniti nel json
        with open(json_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return f"Conversione completata: {csv_path} a {json_path}"

    def media_dei_voti(self, csv_path, nome_materia_voto):
        """
        <summary>
            Legge un file CSV fa la media dei tre studenti con i voti piu alti
            e la media dei voti dei tre studenti con i voti piu bassi.
        </summary>
        """
        self.validate_file()
        df = pd.read_csv(csv_path, sep=';')

        print("Colonne del CSV:", df.columns.tolist())
        print(df.columns.tolist())

        df_ordinato_1 = df.sort_values(by=nome_materia_voto, ascending=False)
        medie_piu_alti = df_ordinato_1.groupby('Nome')[nome_materia_voto].mean()
        tre_piu_alti = df_ordinato_1.head(3)

        df_ordinato_2 = df.sort_values(by=nome_materia_voto, ascending=True)
        medie_piu_bassi = df_ordinato_2.groupby('Nome')[nome_materia_voto].mean()
        tre_piu_bassi = df_ordinato_2.head(3)

        return f"{tre_piu_alti[['Nome', nome_materia_voto]]}, {tre_piu_bassi[['Nome', nome_materia_voto]]}"


    def dal_piu_grande_al_piu_piccolo(self, csv_path):
        """
        <summary>
            Legge un file CSV e stampa dallo studente piu grande al piu piccolo di eta.
        </summary>
        """
        self.validate_file()

        df = pd.read_csv(csv_path, sep=';')
        df_ordinato = df.sort_values(by='eta', ascending=False)

        return f"{df_ordinato[['Nome','eta']]}"

    def stampa_una_classe_specifica(self, csv_path, nome_classe):
        """
        <summary>
            Legge un file CSV e stampa una classe specifica.
        </summary>
        """
        self.validate_file()
        df = pd.read_csv(csv_path, sep=';')

        # Filtra i record
        df_mask = df['Classe'] == nome_classe
        filtered_df = df[df_mask]
        print(filtered_df)
