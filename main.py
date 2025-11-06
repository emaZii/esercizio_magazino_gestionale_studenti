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


import Myjson
import studente
import pagella
import voto

class Software:

    def printPagellaOfAnClassroom(self):
        pass

    def sortPagellaLowHigh(self):
        pass

    def printPagellaHighAndLow(self):
        pass

    '''
    <summary>
       Crea lo studente in modo sincrono
    </summary>
    '''
    def SalvaInformazionieStampa(self, id, nome,age, materia,voto):
        pass

    def SalvaInformazionieStampaAsync(self):
        pass

 sw = Software()

def main():
    print("Scegli la modalita: \n")
    print("tasto-1 Salvare le informazione e stampare (sincrono) \n")
    print("tasto-2 Salvare le informazione e stampare (asyncrono) \n")
    tasto  = input("Scegli la modalita: \n")
    #crea lo studente sincorno
    if tasto =="1":
        sw.SalvaInformazionieStampa()

    #crea lo studente in modo asicrono
    if tasto =="2":
        pass
        #sw.SalvaInformazionieStampaAsync()

if __name__ == "__main__":
    main()