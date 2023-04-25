from pojistenci import Pojistenci
import os



class Sprava:

    uloziste_pojistencu = []

    def pridej_pojistence(self):
        print("\n------------------------------------------------------")
        print("Evidence nového pojištěnce:")
        print("------------------------------------------------------")

        while True:
            jmeno = input("Zadejte jmeno: ")
            if jmeno.isalpha():
                break
            else:
                print("Neplané zadání,zadej znovu." )
        while True:
            prijmeni = input("Zadejte prijmeni: ")
            if prijmeni.isalpha():
                break
            else:
                print("Neplané zadání,zadej znovu.")
        vek = input("Zadejte věk: ")
        telefon = input("Zadejte telefonní číslo: ")
        pojistenec = Pojistenci(jmeno,prijmeni,vek,telefon)
        self.uloziste_pojistencu.append(pojistenec)
        print(pojistenec)
        input("\nPojištěnec byl přidán do evidence,\n"
              ""
              " pokračujte stiskutím tlačítka ENTER...")



    def vyhledej_pojistence(self):

        print("\n------------------------------------------------------")
        print("Vyhledej pojištěnce:")
        print("------------------------------------------------------")
        while True:
            jmeno = input("Zadejte jméno: ").lower()
            if jmeno.isalpha():
                break
            else:
                print("Neplatné zadání,zadej znovu.")
        while True:
            prijmeni = input("Zadejte příjmení: ").lower()
            if prijmeni.isalpha():
                break
            else:
                print("Neplatné zadání,zadej znovu.")

        vysledek_hledani = []
        print("\nVýsledek hledání:")
        if len(self.uloziste_pojistencu) != 0:
            for pojistenec in (self.uloziste_pojistencu):
                if pojistenec.jmeno.lower() == jmeno and pojistenec.prijmeni.lower() == prijmeni:
                    vysledek_hledani.append(pojistenec)
                    print(pojistenec)
                    input("\npokračujte stiskutím tlačítka ENTER...")
            if vysledek_hledani == []:
                print("Nebyl nalezen žádný záznam.")
                input("\npokračujte stiskutím tlačítka ENTER...")

        else:
            print("Nebyl nalezen žádný záznam.")
            input("\npokračujte stiskutím tlačítka ENTER...")


    def vypis_pojistence(self):
        print("\n------------------------------------------------------")
        print("Výpis pojištěnců:")
        print("------------------------------------------------------")
        if len(self.uloziste_pojistencu) == 0:
            print("Do databáze nebyly vloženy žádné záznamy.")
            input("\npokračujte stiskutím tlačítka ENTER...")
        else:
            for pojistenec in self.uloziste_pojistencu:
                print(pojistenec)
            input("\npokračujte stiskutím tlačítka ENTER...")



    def volic(self, volba):

        if volba == "1":
            self.pridej_pojistence()
            return True
        elif volba == "2":
            self.vypis_pojistence()
            return True
        elif volba == "3":
            self.vyhledej_pojistence()
            return True
        elif volba == "4":
            print("Program byl ukončen.")
            exit()


        else:
            print("\nNeplatná volba,proveďte volbu znovu.")
            input("\npokračujte stiskutím tlačítka ENTER...")



    def spustit_program(self):
        while True:
            print("\n------------------------------------------------------")
            print("Evidence pojištění")
            print("------------------------------------------------------")
            print("Vyberte si číslo akce a stiskněte Enter:")
            print("1 - Přidat jméno pojištěného")
            print("2 - Vypsat všechny pojištěné")
            print("3 - Vyhledat pojištěného")
            print("4 - Konec")

            volba = input()
            self.volic(volba)








