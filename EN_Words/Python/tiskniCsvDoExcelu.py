# zde tiskme csv, ktere si pak zpetne nacita pomoci VBA

import pathlib
import string

class tiskniDoExcelu():

    def __init__(self, odkazyVetyKtisku, odkazySlovaKTisku, seznamVet):

        adresaKamTisknout = self.ziskejAdresuCsv()

        # tiskne data
        self.tiskniCsv(odkazyVetyKtisku, adresaKamTisknout, 'odkazyVety.csv')
        self.tiskniCsv(odkazySlovaKTisku, adresaKamTisknout, 'odkazySlova.csv')
        self.tiskniCsv(seznamVet, adresaKamTisknout, 'seznamVet.csv')

        print()




    def tiskniCsv(self, dataKTisku, adresaKamTisknout, nazevSouboru):

        dataWrite = ""
        adresaSouboru = adresaKamTisknout + nazevSouboru
        f = open(adresaSouboru, 'w')

        for i in range(0, len(dataKTisku)):
            radek = dataKTisku[i]

            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()


    def ziskejAdresuCsv(self):
        actPath = str(pathlib.Path().resolve())
        pathSpl = actPath.split('\\')
        pathNadr = ""

        for i in range(0, len(pathSpl) - 1):
            fold = pathSpl[i]
            pathNadr = pathNadr + fold + '\\'

        pathCsv = pathNadr + "CsvToExcel\\"

        return (pathCsv)