'''
<summary>
    Ci devono essere 4 materie
        # Inglese
        # Italiano
        # Matematica
        # Fisica
</summaru>
'''

class Voto:

    def __init__(self,  materia, valutazione):
        if materia not in ["italiano", "matematica", "inglese", "fisica"]:
            raise ValueError(f"Materia '{materia}' non valida.")
        if not (1 <= valutazione <= 10):
            raise ValueError("Valutazione deve essere tra 1 e 10.")
        self.materia = materia
        self.valutazione = valutazione

    def aggiungi_voto(self, materia, valutazione):
        # Aggiunge un voto alla materia specificata
        valutazione = int(valutazione)
        if materia in self.materie:
            if valutazione>=1 and valutazione<=10:
                  self.materie[materia].append(str(valutazione))
            else:
                raise("Error Valutazione deve essere tra 1 e 10")
        else:
            print(f"Materia '{materia}' non trovata!")
