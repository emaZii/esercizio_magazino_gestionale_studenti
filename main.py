import software_json as sw

nuovo_software = sw.SoftwareJson()

vuoi_uscire = False

def main():
    while vuoi_uscire == False:
        MenuPrincipale()
        if vuoi_uscire == True:
            break

def MenuPrincipale():
    ComandiText()
    tasto  = input("Scegli la modalita: \n")

    #Crea lo studente sincorno
    if tasto =="1":
        nuovo_software.SalvaInformazionieStudente()

    # assegnare un voto a un studente esistente
    if tasto == "2":
        nuovo_software.assegnavotoemateria()


    #stampa lo studente dal leta piu piccola al piu grande
    if tasto == "3":
        nuovo_software.printAgeHighAndLow()

    # stampa studenti di una classe specifica
    if tasto == "4":
        nuovo_software.queryclasse()

    if tasto == "5":
        nuovo_software.queryStudente_materia()

    if tasto == "6":
        nuovo_software.mediaVoto()

    #esci dal software
    if tasto == "q" or tasto == "Q":
        global vuoi_uscire
        vuoi_uscire = True

def ComandiText():
    print("Scegli La Modalita: \n")
    print("-1 Crea uno studente")
    print("-2 Assegna un voto ad una materia a uno studente")
    print("-3 Stampa lo studente piu piccolo al piu grande")
    print("-4 Stampa una classe specifica")
    print("-5 Stampa un voto di una materia di uno studente")
    print("-6 Stampa la media dei Voti")
    print("'Q'or'q'(quit) per uscire dal software")

if __name__ == "__main__":
    main()