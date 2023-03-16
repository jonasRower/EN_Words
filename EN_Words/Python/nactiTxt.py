
class ziskejSeznamVet():

    def __init__(self):

        adresa = "C:/Users/jonas/OneDrive/Dokumenty/2022/AJ/AJ_macro/text.txt"
        obsahTxt = self.nacitejTxt(adresa)
        poleSlov = obsahTxt.split()

        indexySlovZacinajicichVet = self.vratIndexySlovZacinajicichVet(poleSlov)

        self.seznamVet = self.vratSeznamVet(indexySlovZacinajicichVet, poleSlov)


    def getSeznamVet(self):
        return(self.seznamVet)



    # ziska pole slov, kde posledni slovo je pred slovem s velkym pismenem
    def vratSeznamVet(self, indexySlovZacinajicichVet, poleSlov):

        poleVetMinAll = self.vratPoleVetMinAll(indexySlovZacinajicichVet, poleSlov)
        boolKonceVet = self.vratBoolKonceVet(poleVetMinAll)
        seznamVet = self.vratPoleVetMin(poleVetMinAll, boolKonceVet)

        return(seznamVet)


    def vratPoleVetMin(self, poleVetMinAll, boolKonceVet):

        seznamVet = []

        for i in range(0, len(boolKonceVet)):
            jeToveta = boolKonceVet[i]

            if(jeToveta == True):
                veta = poleVetMinAll[i]
                if(veta != ""):
                    seznamVet.append(veta)

        return(seznamVet)


    def vratPoleVetMinAll(self, indexySlovZacinajicichVet, poleSlov):

        poleDvojicIndexu = self.vratDvojiciPrvnihoAPoslIndexu(indexySlovZacinajicichVet)
        poleVetMin = []

        for i in range(0, len(poleDvojicIndexu)):
            dvojiceIndexu = poleDvojicIndexu[i]
            vetaMin = self.sestavVetuPodleIndexuSlov(dvojiceIndexu, poleSlov)
            poleVetMin.append(vetaMin)

        return(poleVetMin)


    def sestavVetuPodleIndexuSlov(self, dvojiceIndexu, poleSlov):

        prvniIndex = dvojiceIndexu[0]
        posldeniIndex = dvojiceIndexu[1]
        vetaMin = ""

        if(posldeniIndex > prvniIndex + 1):

            for i in range(prvniIndex, posldeniIndex):
                slovo = poleSlov[i]
                vetaMin = vetaMin + slovo
                if(i < posldeniIndex-1):
                    vetaMin = vetaMin + " "

        return(vetaMin)


    def vratDvojiciPrvnihoAPoslIndexu(self, indexySlovZacinajicichVet):

        poleDvojicIndexu = []

        for i in range(1, len(indexySlovZacinajicichVet)):
            index0 = indexySlovZacinajicichVet[i-1]
            index1 = indexySlovZacinajicichVet[i]

            dvojiceIndexu = []

            dvojiceIndexu.append(index0)
            dvojiceIndexu.append(index1)

            poleDvojicIndexu.append(dvojiceIndexu)

        return(poleDvojicIndexu)



    def vratIndexySlovZacinajicichVet(self, poleSlov):

        indexySlovZacinajicichVet = []

        for i in range(0, len(poleSlov)):
            slovo = poleSlov[i]
            slovoZacinaVelkymPismenem = self.detekujZdaSlovoZacinaVelkymPismenem(slovo)
            indexySlovZacinajicichVet.append(slovoZacinaVelkymPismenem)

        seznamIndexuZac = self.find_indices(indexySlovZacinajicichVet, True)

        return(seznamIndexuZac)


    def vratBoolKonceVet(self, poleVetMin):

        indexyKonceVet = []
        posledniZnakJeTecka = False

        for i in range(0, len(poleVetMin)):
            veta = poleVetMin[i]

            if(veta != ""):
                posledniZnakJeTecka = self.detekujZdaSlovoKonciTeckou(veta)


            indexyKonceVet.append(posledniZnakJeTecka)

        return (indexyKonceVet)


    # detekuje, zda prvni pismeno je velke a druhe male
    def detekujZdaSlovoZacinaVelkymPismenem(self, slovo):

        prvniPismeno = self.vratPismenoZeZacatku(slovo, 0)
        druhePismeno = self.vratPismenoZeZacatku(slovo, 1)

        prvniPismenoJeVelke = self.detekujZdaSeJednaOvelkePismeno(prvniPismeno)
        druhePismenoJeMale = self.detekujZdaSeJednaOmalePismeno(druhePismeno)

        slovoZacinaVelkymPismenem = False

        if(prvniPismenoJeVelke == True):
            if(druhePismenoJeMale == True):
                slovoZacinaVelkymPismenem = True

        return(slovoZacinaVelkymPismenem)



    def detekujZdaSlovoKonciTeckou(self, slovo):

        posledniZnakSlova = self.vratPismenoZKonce(slovo, 1)
        if(posledniZnakSlova == "."):
            posledniZnakJeTecka = True
        else:
            posledniZnakJeTecka = False

        return(posledniZnakJeTecka)



    def detekujZdaSeJednaOvelkePismeno(self, pismeno):

        pismenoVelke = pismeno.upper()

        if(pismeno == pismenoVelke):
            pismenoJeVelke = True
        else:
            pismenoJeVelke = False

        return(pismenoJeVelke)



    def detekujZdaSeJednaOmalePismeno(self, pismeno):

        pismenoMale = pismeno.lower()

        if (pismeno == pismenoMale):
            pismenoJeMale = True
        else:
            pismenoJeMale = False

        return (pismenoJeMale)



    def vratPismenoZeZacatku(self, text, indexPismene):

        pismeno = text[indexPismene:indexPismene+1:1]
        return(pismeno)


    def vratPismenoZKonce(self, text, indexPismeneOdKonce):

        delkaText = len(text)
        indexPismene = delkaText - indexPismeneOdKonce
        pismeno = text[indexPismene:indexPismene+1:1]

        return(pismeno)


    def detekujPritomnostZnaku(self, radek, znak):

        try:
            indexZnaku = radek.index(znak)
        except:
            indexZnaku = -1

        if(indexZnaku > -1):
            pritomnostZnaku = True
        else:
            pritomnostZnaku = False


        return(pritomnostZnaku)


    def find_indices(self, a_list, item_to_find):
        indices = []
        for idx, value in enumerate(a_list):
            if value == item_to_find:
                indices.append(idx)
        return indices





    def nacitejTxt(self, adresa):

        f = open(adresa, "r", encoding='utf-8')
        obsahTxt = f.read()

        return(obsahTxt)