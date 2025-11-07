"""
<summary>

    Quando si avvia il programma ci chiederà di scegliere una modalità tra le seguenti:
    [1] Salvataggio delle informazioni e print a schermo.
    Questa modalità permette di creare uno studente e successivamente inserire i voti.

    A questo punto devo poter:
        - chiedere di vedere la pagella dello studente più grande/piccola
        - chiedere di vedere la pagella degli studenti presente una classe
        - chiedere di vedere i 3 studenti con la media voto in pagella più alta/bassa. (in ordine)
    Es.
        Premi 1 per creare uno studente e i voti
        Premi 2 per chiedere di vedere la pagella dello studente più grande o piccola
        Ecc
        *HO PREMUTO 1*
        Crea lo studente.
        Nome: input nome
        Eta:
        Classe:
        Riepilogo dati, è corretto? Ok
        Adesso quale è il voto dello studente x in materia y?

    [2] Salvataggio delle informazioni in maniera “asincrona” e print a schermo.
        Uguale alla modalità precedente, ma posso scegliere se creare lo studente o creare il voto da assegnare alla pagella dello studente.
    A questo punto devo poter:
        - chiedere di vedere la pagella dello studente più grande/piccola
        - chiedere di vedere la pagella degli studenti presente una classe
        - chiedere di vedere i 3 studenti con la media voto in pagella più alta/bassa. (in ordine)
    Es.
        Premi 1 per creare uno studente
        Premi 2 per assegnare i voti allo studente x
        Ecc
    [3] Lettura da file excel e print a schermo
        Creare a mano un file excel con una tabella con le seguenti colonne: nome, età, classe, VotoInglese, VotoItaliano, VotoMatematica, VotoFisica.
        Le informazioni vengono salvate e poi mostrate a schermo.
    A questo punto devo poter:
        - chiedere di vedere la pagella dello studente più grande/piccola
        - chiedere di vedere la pagella degli studenti presente una classe
        - chiedere di vedere i 3 studenti con la media voto in pagella più alta/bassa. (in ordine)
</summary>
"""
import gestione_studenti as gs
import voto as vt
import my_data_obj as mydataobj

class Software:

    def __init__(self):
        self.id_counter = 0

    def printPagellaOfAnClassroom(self, ):
        new_data = mydataobj.WriteObject()
        print(new_data.ReadOnJson("classroom"))

    def sortPagellaLowHigh(self):
        ...

    def printPagellaHighAndLow(self):
        ...

    '''
    <summary>
       Crea lo studente in modo sincrono
    </summary>
    '''
    def SalvaInformazionieStudente(self):
        print("Creazione Studente")
        nuovo_studente = gs.GestioneStudenti()
        self.id_counter += 1
        name = input("Scegli nome: ").lower()
        eta = input("Scegli eta: ").lower()
        classe = input("Scegli classe: ").lower()
        risposta = input("Adesso vuoi dai il voto dello studente a qualche materia y=si n=no? \n").lower()
        if risposta == "y":
            materia = input("Scegli materia: ").lower()
            voto = int(input("Scegli voto tra 1 a 10: "))
            nuova_valutazione = vt.Voto(materia, voto)
            nuovo_studente.caricaStudentiVotieMaterieSulJson(self.id_counter, name, eta, classe, materia, voto)
        elif risposta == "n":
            nuovo_studente.caricaStudentiSulJson(self.id_counter, name, eta, classe)

    def SalvaInformazionieStampaAsync(self):
        ...
