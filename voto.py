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
        self.materie =  {
            "Italiano": [],
            "Matematica": [],
            "Inglese": [],
            "Fisica": []
        }
        self.valutazione = valutazione

    def aggiungi_voto(self, materia, valutazione):
        # Aggiunge un voto alla materia specificata
        if materia in self.materie:
            if valutazione>=1 and valutazione<=10:
                  self.materie[materia].append(str(valutazione))
            else:
                raise("Error Valutazione deve essere tra 1 e 10")
        else:
            print(f"Materia '{materia}' non trovata!")
