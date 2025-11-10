import software_json as sw

nuovo_software = sw.SoftwareJson()

vuoi_uscire = False

def main():
    while vuoi_uscire == False:
        Scelta_Json_o_Csv()
        if vuoi_uscire == True:
            break

def Scelta_Json_o_Csv():
    global vuoi_uscire

    print("---SCEGLI MODALITA---\n")

    modalita = input("-Scegli di lavorare con i json o csv? 1-JSON, 2-CSV 3-Uscire_Dal_Software: \n")

    if modalita == "1":
        MenuPrincipalejson()
    elif modalita == "2":
        MenuPrincipaleCSV()
    elif modalita == "3":
        vuoi_uscire = True


def MenuPrincipalejson():
    ComandiTextJson()
    tasto  = input("Scegli: \n")

    #Crea lo studente sincrono
    if tasto =="1":
        nuovo_software.SalvaInformazionieStudente()

    # Assegnare un voto a un studente esistente
    if tasto == "2":
        nuovo_software.assegnavotoemateria()

    # Stampa lo studente dall'eta piu piccola al piu grande
    if tasto == "3":
        nuovo_software.printAgeHighAndLow()

    # Stampa studenti di una classe specifica
    if tasto == "4":
        nuovo_software.queryclasse()

    if tasto == "5":
        nuovo_software.queryStudente_materia()

    if tasto == "6":
        nuovo_software.mediaVoto()

    if tasto == "7":
        nuovo_software.PrintAllData()

    # Esci dal software
    if tasto == "q" or tasto == "Q":
        global vuoi_uscire
        vuoi_uscire = True

def MenuPrincipaleCSV():
    pass
    #ComandiTextCsv()

def ComandiTextJson():
    print("---MODALITA JSON--- \n")
    print("Scegli:")
    print("-1 Crea uno studente")
    print("-2 Assegna un voto ad una materia a uno studente")
    print("-3 Stampa lo studente piu piccolo al piu grande")
    print("-4 Stampa una classe specifica")
    print("-5 Stampa un voto di una materia di uno studente")
    print("-6 Stampa la media dei Voti")
    print("-7 Stampa tutti i studenti")
    print("'Q'or'q'(quit) per uscire dal software")

def ComandiTextCsv():
    #print("---MODALITA CSV--- \n")
    #print("Scegli:")
    #print("'Q'or'q'(quit) per uscire dal software")
    pass

if __name__ == "__main__":
    main()