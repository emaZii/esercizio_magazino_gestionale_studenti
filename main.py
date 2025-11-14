import software_json as sw
import csvdata as csv

nuovo_software = sw.SoftwareJson()

vuoi_uscire = False

csv_path = "dati.csv"
json_path = "data.json"

reader = csv.CSVReader(csv_path, sep=";")

def main():
    while vuoi_uscire == False:
        scelta_json_o_csv()
        if vuoi_uscire == True:
            break

def scelta_json_o_csv():
    global vuoi_uscire

    print("---SCEGLI MODALITA---\n")

    modalita = input("-Scegli di lavorare con i json o csv?\n 1-JSON,\n 2-CSV\n q-Uscire_Dal_Software: \n")

    if modalita == "1":
        menu_principale_json()
    elif modalita == "2":
        menu_principale_csv()
    elif modalita == "q" or modalita == "Q":
        vuoi_uscire = True


def menu_principale_json():
    comandi_text_json()
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
        nuovo_software.cancella_studente()

    if tasto == "8":
        nuovo_software.PrintAllData()

    # Esci dal software
    if tasto == "q" or tasto == "Q":
        global vuoi_uscire
        vuoi_uscire = True

def menu_principale_csv():
    global reader
    global csv_path

    comandi_text_csv()

    tasto = input("Scegli: \n")
    # stampa la media dei voti
    if tasto == "1":
        nome_materia = input("Scegli la materia scrivendo 'VotoMateria Esempio VotoFisica': \n")
        media = reader.media_dei_voti(csv_path, nome_materia)
        print(media)
    #
    if tasto == "2":
        print("Ecco La Lista dei studenti dal piu grande al piu piccolo")
        dal_piu_grande_al_piu_piccolo = reader.dal_piu_grande_al_piu_piccolo(csv_path)
        print(dal_piu_grande_al_piu_piccolo)
    #
    if tasto == "3":
        nome_classe = input("Scegli la classe: \n")
        stampa_classe = reader.stampa_una_classe_specifica(csv_path, nome_classe)
        print(stampa_classe)

    #converti il csv in json
    if tasto == "4":
        conversione = reader.csv_to_json('dati.csv', 'data.json')
        print(f"Conversione fatta dal file dati.csv al data.json")

    # Esci dal software
    if tasto == "q" or tasto == "Q":
        global vuoi_uscire
        vuoi_uscire = True

def comandi_text_json():
    print("---MODALITA JSON--- \n")
    print("Scegli:")
    print("-1 Crea uno studente")
    print("-2 Assegna un voto ad una materia a uno studente")
    print("-3 Stampa lo studente piu piccolo al piu grande")
    print("-4 Stampa una classe specifica")
    print("-5 Stampa un voto di una materia di uno studente")
    print("-6 Stampa la media dei Voti")
    print("-7 Cancella un studente specifico")
    print("-8 Stampa tutti i studenti")
    print("'Q'or'q'(quit) per uscire dal software")

def comandi_text_csv():
    print("---MODALITA CSV--- \n")
    print("Scegli:")
    print("-1 Stampa la media dei Voti di una materia")
    print("-2 Stampa lo studente piu piccolo al piu grande")
    print("-3 Stampa i voti di una classe specifica")
    print("-4 Converti il csv in json")
    print("'Q'or'q'(quit) per uscire dal software")

if __name__ == "__main__":
    main()