import nactiTxt
import ziskejOdkazyNaSlova
import nactiCsv
import ziskejOdkazyNaVety
import pripravCsv
import tiskniCsvDoExcelu


#nacte txt
vykonavejHlavniProgram = nactiTxt.ziskejSeznamVet()
seznamVet = vykonavejHlavniProgram.getSeznamVet()

# nacte csv
dataCsv = nactiCsv.nactiVsechnyListyCsv()
slovaENCetnostAll = dataCsv.getSlovaENCetnostAll()

# ziska odkazy na slova
dataCsv = ziskejOdkazyNaSlova.propojSExcelem(seznamVet, slovaENCetnostAll)
slovaVetyAll = dataCsv.getSlovaVetyAll()
odkazyNaSlovaAll = dataCsv.getOdkazyNaSlovaAll()

#ziska odkazy na vety
dataVety = ziskejOdkazyNaVety.odkazyNaVety(seznamVet, slovaENCetnostAll)
seznamIndexuVet = dataVety.getSeznamIndexuVet()

# ziska data k tsiku
dataKTisku = pripravCsv.pripravCsvKTisku(odkazyNaSlovaAll, seznamIndexuVet, slovaENCetnostAll)
odkazyVetyKtisku = dataKTisku.getOdkazyVetyKtisku()
odkazySlovaKTisku = dataKTisku.getOdkazySlovaKisku()

# tiskne data do csv jako vstup do Excelu
tiskniCsvDoExcelu.tiskniDoExcelu(odkazyVetyKtisku, odkazySlovaKTisku, seznamVet)


print()