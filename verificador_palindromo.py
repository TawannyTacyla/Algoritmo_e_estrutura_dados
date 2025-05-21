import unicodedata

# Função para remover acentos da frase

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sem_acentos = ''.join(
        letra for letra in texto_normalizado
        if unicodedata.category(letra) != 'Mn'
    )
    return texto_sem_acentos

# Função que verifica se a frase é um palíndromo

def eh_palindromo(frase):
    frase = frase.lower()  # Coloca tudo em minúsculo
    frase = remover_acentos(frase)  # Remove acentos
    frase = ''.join(frase.split())  # Tira os espaços
    return frase == frase[::-1]  # Compara com ela mesma ao contrário

def main():
    entrada = input("Digite uma palavra ou frase: ")

    if eh_palindromo(entrada):
        print("✅ É um palíndromo!")
    else:
        print("❌ Não é um palíndromo.")

if __name__ == "__main__":
    main()
