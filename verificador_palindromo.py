import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def eh_palindromo(frase):
    frase = frase.lower()
    frase = remover_acentos(frase)
    frase = ''.join(frase.split())
    return frase == frase[::-1]

def main():
    frase = input("Digite uma palavra ou frase: ")
    if eh_palindromo(frase):
        print("✅ É um palíndromo!")
    else:
        print("❌ Não é um palíndromo.")

if __name__ == "__main__":
    main()
