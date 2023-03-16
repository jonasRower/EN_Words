

#nacita vsechny listy jako csv, jelikoz nacitani excelu trva prilis dlouho
import pathlib
import string

class nactiVsechnyListyCsv():

    def __init__(self):

        self.slovaENCetnostAll =self.ziskejVsechnyDataZCsv()


    def getSlovaENCetnostAll(self):
        return(self.slovaENCetnostAll)



    def ziskejVsechnyDataZCsv(self):

        abeceda = list(string.ascii_uppercase)
        pathCsv = self.ziskejAdresuCsv()
        slovaENCetnostAll = []

        for i in range(0, len(abeceda)):
            pismeno = abeceda[i]
            slovaENCetnost = self.ziskejDataZCsvProDanePismeno(pismeno, pathCsv)

            slovaENCetnostAll.append(slovaENCetnost)

        return(slovaENCetnostAll)



    def ziskejDataZCsvProDanePismeno(self, pismeno, pathCsv):

        nazevCsv = pismeno + '.csv'
        adresaCsv = pathCsv + nazevCsv
        poleRadkuCsv = self.vratPoleRadkuCsv(adresaCsv)
        slovaENCetnost = self.vratPoleSlovENCetnost(poleRadkuCsv, pismeno)

        return(slovaENCetnost)


    def vratPoleSlovENCetnost(self, poleRadkuCsv, pismeno):

        slovaENCetnost = []
        slovaENCetnost.append(pismeno)

        for i in range(0, len(poleRadkuCsv)):
            radek = poleRadkuCsv[i]

            if(radek != ""):
                slova = radek.split(',')
                slovoEN = slova[0]

                if(len(slova) == 1):
                    slovoCetnost = ""
                else:
                    slovoCetnost = slova[4]
                    if(slovoCetnost == ''):
                        slovoCetnostInt = 0
                    else:
                        slovoCetnostInt = int(slovoCetnost)

                ENCetnost = []
                ENCetnost.append(slovoEN)
                ENCetnost.append(slovoCetnostInt)

                slovaENCetnost.append(ENCetnost)

        return(slovaENCetnost)


    def vratPoleRadkuCsv(self, adresa):

        obsahCsv = self.nacitejCSV(adresa)
        poleRadkuCsv = obsahCsv.split('\n')

        return(poleRadkuCsv)


    def ziskejAdresuCsv(self):

        actPath = str(pathlib.Path().resolve())
        pathSpl = actPath.split('\\')
        pathNadr = ""

        for i in range(0, len(pathSpl)-1):
            fold = pathSpl[i]
            pathNadr = pathNadr + fold + '\\'

        pathCsv = pathNadr + "Csv\\"

        return(pathCsv)


    def nacitejCSV(self, adresa):

        f = open(adresa, "r")
        obsahTxt = f.read()

        return(obsahTxt)

