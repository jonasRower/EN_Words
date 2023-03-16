
class pripravCsvKTisku():

    def __init__(self, odkazyNaSlovaAll, seznamIndexuVet, slovaENCetnostAll):

        seznamListu = self.ziskejSeznamListu(slovaENCetnostAll)
        self.vytiskniSeznamIndexuVet(seznamIndexuVet, seznamListu)
        poleRadkuVety = self.vytiskniSeznamIndexuVet(seznamIndexuVet, seznamListu)
        rozsahRadkuArr = self.ziskejRozsahRadku(poleRadkuVety, seznamListu)

        self.poleRadkuVetyKtisku = rozsahRadkuArr + poleRadkuVety
        self.odkazyNaSlovaKTisku = self.pripravOdkazyNaSlovaKTisku(odkazyNaSlovaAll)



    # vrati data
    def getOdkazyVetyKtisku(self):
        return(self.poleRadkuVetyKtisku)


    def getOdkazySlovaKisku(self):
        return(self.odkazyNaSlovaKTisku)



    def pripravOdkazyNaSlovaKTisku(self, odkazyNaSlovaAll):

        odkazyNaSlovaKTisku = []

        for i in range(0, len(odkazyNaSlovaAll)):
            odkazyNaSlova = odkazyNaSlovaAll[i]
            radekStr = self.prevedRadekNaStr(odkazyNaSlova)

            odkazyNaSlovaKTisku.append(radekStr)

        return(odkazyNaSlovaKTisku)


    # aby nemusel prohledavat vsechny radky textu, na zacatku vytiskne
    # mezi jakymi radky jsou slova zacinajici na stejne pismeno
    # cimz se samozrejmě zrychli prohledavani pomoci VBA
    def ziskejRozsahRadku(self, poleRadkuVety, seznamListu):

        rozsahRadkuArr = []

        for i in range(0, len(seznamListu)):
            nazevListu = seznamListu[i]
            rozsahRadku = self.vratIndexyMeziKterymiJeDanePismeno(poleRadkuVety, nazevListu, len(seznamListu))
            rozsahRadkuArr.append(rozsahRadku)

        return(rozsahRadkuArr)


    def vratIndexyMeziKterymiJeDanePismeno(self, poleRadkuVety, pismenoExp, posunO):

        sekceZac = -1
        sekceKon = -1

        for i in range(0, len(poleRadkuVety)):
            radek = poleRadkuVety[i]

            if(radek == ""):
                if(sekceZac == -1):
                    radekSPismenem = poleRadkuVety[i+1]
                    if(radekSPismenem == pismenoExp):
                        sekceZac = i + 2
                else:
                    sekceKon = i-1
                    break

        if(sekceKon == -1):
            sekceKon = len(poleRadkuVety)

        sekceZacKonStr = pismenoExp + ',' + str(sekceZac + posunO) + ',' + str(sekceKon + posunO)


        return(sekceZacKonStr)


    def vytiskniSeznamIndexuVet(self, seznamIndexuVet, seznamListu):

        poleRadkuAll = []

        for i in range(0, len(seznamIndexuVet)):
            nazevListu = []
            nazevListu.append("")
            nazevListu.append(seznamListu[i])
            poleRadkuAll = poleRadkuAll + nazevListu

            seznamIndexuVetPismeno = seznamIndexuVet[i]
            poleRadkuPismene = self.vratStrSeznamIndexuPismena(seznamIndexuVetPismeno)

            poleRadkuAll = poleRadkuAll + poleRadkuPismene

        return(poleRadkuAll)


    def vratStrSeznamIndexuPismena(self, seznamIndexuVetPismeno):

        poleRadku = []

        for i in range(0, len(seznamIndexuVetPismeno)):
            radek = seznamIndexuVetPismeno[i]
            radekStr = self.prevedRadekNaStr(radek)

            poleRadku.append(radekStr)

        return(poleRadku)


    def prevedRadekNaStr(self, radekData):

        radekStr = ""

        for i in range(0, len(radekData)):
            slovo = str(radekData[i])

            radekStr = radekStr + slovo

            if(i < len(radekData)-1):
                radekStr = radekStr + ','

        return(radekStr)


    def ziskejSeznamListu(self, slovaENCetnostAll):

        seznamListu = []

        for i in range(0, len(slovaENCetnostAll)):
            nazevListu = slovaENCetnostAll[i][0]
            seznamListu.append(nazevListu)

        return(seznamListu)


    def tiskniJSON(self, dataKTisku, nazevSouboru):

        dataWrite = ""
        f = open(nazevSouboru, 'w')

        for i in range(0, len(dataKTisku)):
            radek = dataKTisku[i]
            if(i < len(dataKTisku)-1):
                radek = radek + ' +'
            else:
                radek = radek + ';'

            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()

        print("")
