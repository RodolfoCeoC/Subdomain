import sys
import requests
from os import path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help="Escribe el dominio: ")
parser = parser.parse_args()


def main():
    if parser.target:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt', 'r')
            wordlist = wordlist.read().split('\n')

            for subdomain in wordlist:
                url = "http://" + subdomain + "." + parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio Descubierto: " + url)

    else:
        print("No se encuentra el subdominio, por favor, ingresa uno válido")
        sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
