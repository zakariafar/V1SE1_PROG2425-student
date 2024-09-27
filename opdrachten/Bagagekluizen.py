def toon_menu():
    print("[1] Ik wil weten hoeveel kluizen nog vrij zijn.")
    print("[2] Ik wil een nieuwe kluis.")
    print("[3] Ik wil even iets uit mijn kluis halen.")
    print("[4] Ik geef mijn kluis terug.")
    print("[5] Ik wil stoppen.")


def aantal_vrije_kluizen():
    totaal_kluizen = 12
    try:
        with open("kluizen.txt", "r") as f:
            regels = f.readlines()
            toegewezen_kluizen = len(regels)
            return totaal_kluizen - toegewezen_kluizen
    except FileNotFoundError:
        return totaal_kluizen


def nieuwe_kluis():
    with open("kluizen.txt", "a") as f:
        nieuwe_kluisnummer = aantal_vrije_kluizen() + 1
        code = input("Voer je code in:  ")
        f.write(f"{nieuwe_kluisnummer};{code}\n")
        print(f"Je hebt kluisnummer {nieuwe_kluisnummer}.")

def uit_kluis_halen():
    kluisnummer = int(input("Voer je kluisnummer in: "))
    code = int(input("Voer je code in:  "))
    with open("kluizen.txt", "r") as f:
        regels = f.readlines()
    for regel in regels:
        nummer, opgeslagen_code = regel.strip().split(";")
        if kluisnummer == int(nummer) and code == opgeslagen_code:
            print("Je hebt iets uit je kluis gehaald.")
            return
        print ("Kluisnummer of code is onjuist.")

def kluist_teruggeven():
    kluisnummer = int(input("Voer je kluisnummer in: "))
    code = int(input("Voer je code in:  "))
    with open("kluizen.txt", "r") as f:
        regels = f.readlines()
    nieuwe_regels = []
    kluis_gevonden = False
    for regel in regels:
        nummer, opgeslagen_code = regel.strip().split(";")
        if kluisnummer == int(nummer) and code == opgeslagen_code:
            kluis_gevonden = True
            print("Je hebt je kluis teruggeven.")
        else:
            nieuwe_regels.append(regel)
        if kluis_gevonden:
            with open("kluizen.txt", "w") as f:
                f.writelines(nieuwe_regels)
        else:
            print("Kluisnummer of code is onjuist.")

def main():
    while True:
        keuze = int(input("Welke optie wil je kiezen? "))

        if keuze == 1:
            print(f"Aantal vrije kluizen: {aantal_vrije_kluizen()}")
        elif keuze == 2:
            nieuwe_kluis()
        elif keuze == 3:
            uit_kluis_halen()
        elif keuze == 4:
            kluist_teruggeven()
        elif keuze == 5:
            print("Bedankt voor het gebruiken van deze programma. Tot ziens")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
            keuze = int(input("Welke optie wil je kiezen? "))

toon_menu()
main()



