
class odkazyNaVety():

    def __init__(self, seznamVet, slovaCsvAll):

        seznamIndexuSVetamiAll = self.vratIndexyVsechVet(slovaCsvAll, seznamVet)
        seznamIndexuSVetamiReduct = self.vratIndexyVsechVetReduct(seznamIndexuSVetamiAll)

        self.seznamIndexuVet = seznamIndexuSVetamiReduct


    def getSeznamIndexuVet(self):
        return(self.seznamIndexuVet)


    # redukuje data, jen na ty slova, kde nalezl indexy
    # je totiz zbytecne, aby tiskl vsechno
    def vratIndexyVsechVetReduct(self, seznamIndexuSVetamiAll):

        seznamIndexuSVetamiReduct = []

        for i in range(0, len(seznamIndexuSVetamiAll)):
            seznamIndexuSVetamiList = seznamIndexuSVetamiAll[i]
            seznamIndexuSVetamiRequir = self.redukuIndexyVetNaListu(seznamIndexuSVetamiList)
            seznamIndexuSVetamiReduct.append(seznamIndexuSVetamiRequir)

        return(seznamIndexuSVetamiReduct)


    def redukuIndexyVetNaListu(self, seznamIndexuSVetamiList):

        seznamIndexuSVetamiRequir = []

        for i in range(1, len(seznamIndexuSVetamiList)):
            slovoAIndexy = seznamIndexuSVetamiList[i]
            delkaPole = len(slovoAIndexy)
            if(delkaPole > 1):
                seznamIndexuSVetamiRequir.append(slovoAIndexy)

        return(seznamIndexuSVetamiRequir)


    def vratIndexyVsechVet(self, slovaCsvAll, seznamVet):

        seznamIndexuSVetamiAll = []

        for i in range(0, len(slovaCsvAll)):
            slovaNaLsitu = slovaCsvAll[i]
            seznamIndexuSVetamiList = self.proDaneSlovoVratVyskytVeVetach(slovaNaLsitu, seznamVet)

            seznamIndexuSVetamiAll.append(seznamIndexuSVetamiList)

        return(seznamIndexuSVetamiAll)


    def proDaneSlovoVratVyskytVeVetach(self, slovaNaLsitu, seznamVet):

        seznamIndexuSVetamiList = []
        seznamIndexuSVetamiList.append(slovaNaLsitu[0])

        for i in range(1, len(slovaNaLsitu)):
            dvojice = slovaNaLsitu[i]
            slovo = dvojice[0]

            if(slovo == ""):
                seznamIndexuSVetami = []
                seznamIndexuSVetami.append(slovo)
            else:
                seznamIndexuSVetami = self.ziskejIndexyDanehoSlova(seznamVet, slovo)

            seznamIndexuSVetamiList.append(seznamIndexuSVetami)

        return(seznamIndexuSVetamiList)


    # projde vsechny vety a nalezen indexy danych slov
    def ziskejIndexyDanehoSlova(self, seznamVet, slovo):

        seznamIndexuSVetami = []
        seznamIndexuSVetami.append(slovo)

        for i in range(0, len(seznamVet)):
            veta = seznamVet[i]
            vetaObsahujeSlovo = self.detekujPritomnostSlova(veta, slovo)

            if(vetaObsahujeSlovo == True):
                seznamIndexuSVetami.append(i)

        return(seznamIndexuSVetami)


    def detekujPritomnostSlova(self, text, slovo):

        try:
            indOf = text.index(slovo)
            textObsahujeSlovo = True
        except:
            textObsahujeSlovo = False

        return(textObsahujeSlovo)