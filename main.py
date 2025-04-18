import os
import msvcrt
import time

piattaforme = []
password = []
dizionario = {}

#crea la stringa con la piattaforma e la password da inserire nel file
def crea_stringa(stringa1,stringa2):
    return stringa1 + "," + stringa2 + "\n"

#crea il file con le password, se esiste gia va avanti, se non esiste lo crea inserendo una riga di intestazione.Il nome del file viene scelto dall'utente e ogni volta che il file viene avviato viene chiesto il nome e quindi aperto il file richiesto
def inizializza_file_nuovo():
    global nome
    nome = str(input("Scegli nome del file: "))
    
    file = open(nome+".csv","a")
    file.write(crea_stringa("PIATTAFORMA","PASSWORD"))
    file.close()

#scrive sul file la password con la relativa piattaforma
def scrivi_su_file(piattaforma,password):
    file = open(nome+".csv","a")
    file.write(crea_stringa(piattaforma,password))
    file.close()
    aggiungi_a_dizionario(piattaforma,password)

#aggiungi elementi al dizionario
def aggiungi_a_dizionario(piattaforma,password):
    dizionario[piattaforma] = password
    return

#legge riga x riga del file, inserisce le piattaforme e le password nell'apposita lista e poi crea il dizionario.Stampa un messaggio opportuno se c'è un errore nella lettura del file perche non esiste
def crea_dizionario():
    try:
        file = open(nome+".csv","r")
        for riga in file:
            riga.strip().split(",")
            piattaforme.append(riga[0])
            password.append(riga[1])
        dizionario(dict(zip(piattaforme,password)))
    except FileNotFoundError:
        print("File non esistente")

#prendi input in modo criptato con gli asterischi
def prendi_input_criptato(prompt=""):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()  # Legge un carattere senza mostrarlo
        if char == b"\r":  # Invio (Enter)
            print()  # Nuova riga
            break
        elif char == b"\b":  # Backspace
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)  # Cancella l'asterisco
        else:
            password += char.decode("utf-8")
            print("*", end="", flush=True)
    
    return password

#elimina i dati della piattaforma richiesta
def elimina(piattaforma):
    verifica = verifica_piattaforma(piattaforma)  
    if verifica == True:
        del dizionario[piattaforma]

#stampa tutte le password nel formato: piattaforma : password
def stampa_tutte():
    for elemento in dizionario:
        if elemento == "PIATTAFORMA":
            pass
        else:
            print(elemento," : ",dizionario[elemento])

    x = input("\n\npremi un tasto per continuare...")

#stampa la password della piattaforma richiesta nel formato: piattaforma : password
def stampa_specifica(piattaforma):
    verifica = verifica_piattaforma(piattaforma)  
    if verifica == True:
        print(piattaforma," ",dizionario[piattaforma])
    x = input("\n\npremi un tasto per continuare...")

#verifica se la piattaforma inserite esiste o no
def verifica_piattaforma(piattaforma):
    if piattaforma not in dizionario.keys():
        print("Piattaforma non presente")
        return False
    else:
        return True
        
#stampa il menu e prende la scelta di quale voce eseguire
def stampa_menu():
    print("******MENU******")
    print("1. Aggiungi password")
    print("2. Togli password")
    print("3. Mostra tutte le password")
    print("4. Mostra password specifica")
    print("5. Esci")
    print("")

    scelta = int(input("Scelta: "))
    return scelta

#stampa e prende la scelta di quale voce eseguire inizialmente
def stampa_menu_iniziale():
    print("******MENU******")
    print("1. Crea nuovo file")
    print("2. Usa file esistente")
    print("3. Esci")
    print("")

    scelta = int(input("Scelta: "))
    return scelta

#main
def main():
    os.system("cls")
    scelta = stampa_menu_iniziale()
    if scelta == 1:
        inizializza_file_nuovo()
        uscita = False
    elif scelta == 2:
        nome = str(input("Scegli file da modificare: "))
        if os.path.exists(nome+'.csv'):
            crea_dizionario()
            time.sleep(2)
            uscita = False
        else:
            print("Nessun file con questo nome")
            uscita = True
            time.sleep(2)
    else:
        print("Scelta non valida o nulla")
        time.sleep(2)
        uscita = True
    
    os.system("cls")
    
    while not uscita:
        scelta = stampa_menu()
        if scelta == 1:
            print()
            piattaforma = str(input("Nome piattaforma: "))
            password = prendi_input_criptato("Password: ")
            aggiungi_a_dizionario(piattaforma,password)
            scrivi_su_file(piattaforma,password)
            print("\nModifice apportate con successo")
            time.sleep(2.5)
        elif scelta == 2:
            print()
            piattaforma = str(input("Nome piattaforma: "))
            elimina(piattaforma)
            print("\nModifice apportate con successo")
            time.sleep(2.5)
        elif scelta == 3:
            print()
            print("\nEcco le tue password nel seguente formato\nPiattaforma : Password")
            stampa_tutte()
        elif scelta == 4:
            print()
            piattaforma = str(input("Nome piattaforma: "))
            print("Ecco la password di "+piattaforma)
            stampa_specifica(piattaforma)
        elif scelta == 5:
            print()
            print("Uscita...")
            time.sleep(2)
            uscita = True
        else:
            print("scelta nulla")
            time.sleep(2)
        os.system("cls")
main()