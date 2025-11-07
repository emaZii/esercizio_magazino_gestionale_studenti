import software as sw

nuovo_software = sw.Software()

vuoi_uscire = False

def main():
    while vuoi_uscire == False:
        MenuPrincipale()
        if vuoi_uscire == True:
            break

def MenuPrincipale():
    print("Scegli la modalita: \n")
    print("tasto-1 Salvare le informazione e stampare (sincrono) \n")
    print("tasto-2 Salvare le informazione e stampare (asyncrono) \n")
    print("tasto-3 stampa la classe specifica \n")
    print("Tasto Q-q (quit) per uscire dal software \n")
    tasto  = input("Scegli la modalita: \n")

    #Crea lo studente sincorno
    if tasto =="1":
        nuovo_software.SalvaInformazionieStudente()

    # Crea lo studente in modo asicrono
    if tasto == "2":
        ...
        #nuovo_software.SalvaInformazionieStampaAsync()

    if tasto == "3":
        ...
        #nuovo_software.printPagellaOfAnClassroom()
    if tasto == "q" or tasto == "Q":
        global vuoi_uscire
        vuoi_uscire = True

if __name__ == "__main__":
    main()