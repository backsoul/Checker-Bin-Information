
import pycurl 
import json
import requests
import os

API = "https://lookup.binlist.net/"
banner = """

  ____  _          _____        __                           _   _             
 |  _ \(_)        |_   _|      / _|                         | | (_)            
 | |_) |_ _ __      | |  _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __  
 |  _ <| | '_ \     | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 | |_) | | | | |   _| |_| | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | |
 |____/|_|_| |_|  |_____|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                                                               
                                                                               
create by: Daniel Sarmiento Dev 
creation date: 28-July-2020
"""

def GetBin(Bin):
    print(banner)
    if len(Bin) == 6:
        API_BIN = API + Bin
        response = requests.get(API_BIN)
        response_json = json.loads(response.text)
        pais = response_json['country']
        print("----------------------------------------")
        print("Información del pais")
        print("----------------------------------------")
        try:
            print("Pais de Origén:",pais['name'])
            print("Número identificador del país:","+" + pais['numeric'])
            print("Moneda del País:",pais['currency'])
            print("----------------------------------------")
            print("Información del Banco")
            print("----------------------------------------")
        except:
            print("No se obtuvo mas información acerca del bin.")
        try:
            banco = response_json['bank']
            print("Nombre del Banco:",banco['name'])
            print("Url del Banco:",banco['url'])
            print("Número del Banco:",banco['phone'])
        except:
            print("No se obtuvo mas información acerca del bin.")
        
        print("----------------------------------------")
        print("Información del Bin")
        print("----------------------------------------")
        try:
            scheme = response_json['scheme']
            print("Proveedor:",scheme)
            type_bin = response_json['type']
            print("Tipo del Bin:",type_bin)
            brand = response_json['brand']
            print("Nivel del Bin:",brand)
        except:
            print("No se obtuvo mas información acerca del bin.")
    else:
        print("Numero de Bin Incorrecto.")


if __name__ == "__main__":
    try:
        os.system ("clear") 
        Bin = input('Inserte Bin: ')
        os.system ("clear")
        GetBin(Bin)
    except ValueError:
     print("Numero de Bin Incorrecto.")


