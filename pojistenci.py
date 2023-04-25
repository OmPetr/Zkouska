
class Pojistenci:


    def __init__(self,jmeno,prijmeni,vek,telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon






    def __str__(self):
        return "------------------------------------------------------\n" \
               "{0:<12}      {1:<14}      {2:>3}    {3:>9}       ".format(self.jmeno,self.prijmeni,self.vek,self.telefon)
