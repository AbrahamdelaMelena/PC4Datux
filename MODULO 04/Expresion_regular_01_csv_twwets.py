import csv
import re

def buscar_coincidencias():
    buscar = r"@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"
    with open("/Users/abrah/OneDrive/Escritorio/MODULO 04/short_tweets.csv","r") as archivo_csv:
        reader = csv.reader(archivo_csv, delimiter=",")
    #lista = [archivo_csv]
        for row in reader:
            #if row[5] == buscar:
                #matched_row = row
                #break
                print(re.search(buscar,row))
        print(matched_row)

buscar_coincidencias()