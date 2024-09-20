def standaardprijs(afstandKM):
    if afstandKM <= 0:
        prijs = 0
        print("Je reist 0 kilometer!")
    elif afstandKM <= 50:
        prijs = afstandKM * 0.80
        print("Je reist minder dan 50 kilometer!")
    else:
        prijs = 15 + (afstandKM * 0.60)
        print("Je reist meer dan 50 kilometer!")
    return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    basisprijs = standaardprijs(afstandKM)

    if leeftijd < 12 or leeftijd > 65:
        if weekendrit:
            korting = 0.35
        else:
            korting = 0.30

    else:
        if weekendrit:
            korting = 0.40
        else:
            korting = 0

    prijs_met_korting = basisprijs * (1 - korting)

    return prijs_met_korting


naam = input("Wat is je naam?: ")
print(f"Hallo, {naam}!")

leeftijd = int(input("Hoe oud ben je?: "))

weekendrit = input("Ga je in het weekend reizen? (ja/nee): ")
while weekendrit != "ja" and weekendrit != "nee":
    print("Ongeldige antwoord. Antwoord met 'ja' of 'nee'")
    weekendrit = input("Ga je in het weekend reizen? (ja/nee): ")

afstandKM = int(input("Hoeveel kilometer ga je reizen?: "))

definitieve_prijs = ritprijs(leeftijd, weekendrit, afstandKM)
print(f"De prijs van je treinrit is: €{definitieve_prijs:.2f}")








