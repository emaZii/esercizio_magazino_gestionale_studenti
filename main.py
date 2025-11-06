import software as sw

nuovo_software = sw.Software()

def main():

    print("Scegli la modalita: \n")
    print("tasto-1 Salvare le informazione e stampare (sincrono) \n")
    print("tasto-2 Salvare le informazione e stampare (asyncrono) \n")
    print("tasto-3 stampa la classe specifica")
    tasto  = input("Scegli la modalita: \n")

    #Crea lo studente sincorno
    if tasto =="1":
        nuovo_software.SalvaInformazionieStudente()


    # Crea lo studente in modo asicrono
    if tasto == "2":
        pass
        #nuovo_software.SalvaInformazionieStampaAsync()

    if tasto == "3":
        pass
        #nuovo_software.printPagellaOfAnClassroom()

if __name__ == "__main__":
    main()