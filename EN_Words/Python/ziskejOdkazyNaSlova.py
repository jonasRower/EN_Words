#propoji seznam vet s daty v Excelu
import pandas as pd

class propojSExcelem():

    def __init__(self, seznamVet, slovaCsvAll):

        self.vytvorPoleSlovZeSeznamuVet(seznamVet)
        slovaVetyAll = self.vytvorPoleSlovZeSeznamuVet(seznamVet)
        prvniPismenaAll = self.vratPrvniPismena(slovaVetyAll)

        indexDvojiceAll = self.vratIndexyDvojiceAll(slovaVetyAll, prvniPismenaAll, slovaCsvAll)
        odkazyNaSlovaAll = self.nahradIndexyOdkazy(indexDvojiceAll, slovaCsvAll)

        self.slovaVetyAll = slovaVetyAll
        self.odkazyNaSlovaAll = odkazyNaSlovaAll



    def getSlovaVetyAll(self):
        return(self.slovaVetyAll)


    def getOdkazyNaSlovaAll(self):
        return(self.odkazyNaSlovaAll)



    def nahradIndexyOdkazy(self, indexDvojiceAll, slovaCsvAll):

        odkazyAll = []

        for i in range(0, len(indexDvojiceAll)):
            dvojiceVety = indexDvojiceAll[i]
            odkazyProVetu = self.nahradIndexyOdkazyProVetu(dvojiceVety, slovaCsvAll)

            odkazyAll.append(odkazyProVetu)

        return(odkazyAll)


    def nahradIndexyOdkazyProVetu(self, dvojiceVety, slovaCsvAll):

        odkazyProVetu = []

        for i in range(0, len(dvojiceVety)):
            dvojice = dvojiceVety[i]
            if(len(dvojice) == 0):
                nazevListu = "-1"
                indexRadku = -1
            else:
                indexListu = dvojice[0]
                indexRadku = dvojice[1]
                nazevListu = slovaCsvAll[indexListu][0]

            odkaz = nazevListu + "_" + str(indexRadku)

            odkazyProVetu.append(odkaz)

        return(odkazyProVetu)


    def vratIndexyDvojiceAll(self, slovaVetyAll, prvniPismenaAll, slovaCsvAll):

        indexDvojiceAll = []

        for i1 in range(0, len(slovaVetyAll)):
            indexDvojiceProVetu = self.vratIndexyDvojiceProVetu(slovaVetyAll, prvniPismenaAll, slovaCsvAll, i1)
            indexDvojiceAll.append(indexDvojiceProVetu)

        return(indexDvojiceAll)


    def vratIndexyDvojiceProVetu(self, slovaVetyAll, prvniPismenaAll, slovaCsvAll, i1):

        indexDvojiceProVetu = []

        for i2 in range(0, len(slovaVetyAll[i1])):
            slovo = slovaVetyAll[i1][i2]
            prvniPismeno = prvniPismenaAll[i1][i2]

            indexDvojice = self.ziskejIndexaciDanehoSlova(slovo, prvniPismeno, slovaCsvAll)
            indexDvojiceProVetu.append(indexDvojice)

        return(indexDvojiceProVetu)


    def ziskejIndexaciDanehoSlova(self, slovo, prvniPismenoExp, slovaCsvAll):

        indexDvojice = []

        for i in range(0, len(slovaCsvAll)):
            slovaCsvList = slovaCsvAll[i]
            prvniPismeno = slovaCsvList[0]

            if(prvniPismeno == prvniPismenoExp):
                indexRadku = self.ziskejIndexRadkuNaListu(slovaCsvList, slovo)

                indexDvojice.append(i)
                indexDvojice.append(indexRadku)

                break

        return(indexDvojice)


    def ziskejIndexRadkuNaListu(self, slovaCsvList, slovoExp):

        indexRadku = -1

        for i in range(1, len(slovaCsvList)):
            dvojice = slovaCsvList[i]
            slovo = dvojice[0]

            if(slovo == slovoExp):
                indexRadku = i
                break

        return(indexRadku)



    #def ziskejPoleIndexu1(self, prvniPismenaAll, slovaCsvAll):



    def vytvorPoleSlovZeSeznamuVet(self, seznamVet):

        slovaVetyAll = []

        for i in range(0, len(seznamVet)):
            veta = seznamVet[i]
            vetaBezTecky = veta.replace('.', '')

            slovaVety = vetaBezTecky.split()
            slovaVetyAll.append(slovaVety)

        return(slovaVetyAll)

    
    def vratPrvniPismena(self, slovaVetyAll):

        prvmiPismenaAll = []

        for i in range(0, len(slovaVetyAll)):
            slovaVety = slovaVetyAll[i]
            polePrvnichPismen = self.vratPolePrvnichPismen(slovaVety)
            prvmiPismenaAll.append(polePrvnichPismen)

        return(prvmiPismenaAll)


    def vratPolePrvnichPismen(self, slovaVety):

        polePrvnichPismen = []

        for i in range(0, len(slovaVety)):
            slovo = slovaVety[i]
            prvniPismeno = slovo[0:1:1]

            polePrvnichPismen.append(prvniPismeno.upper())

        return(polePrvnichPismen)