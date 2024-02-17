# função usada para criar a tupla
def gerar_tupla(tam_tupla):
    tupla = ()
    for i in range (tam_tupla):
        item = input("Informe o item da tupla: ")
        tupla = tupla + (item,)
    
    return tupla

# filtrar nomes com base em uma letra
def filtrar_nomes(tupla_nomes, letra):
    nova_tupla = ()

    # Convertendo a letra para minúsculas 
    # (ignorando distinção entre maiúsculas e minúsculas)
    letra = letra.lower()

    for nome in tupla_nomes:
        # O método startswith() é usado para verificar 
        #se uma string começa com um determinado prefixo.
        if nome.lower().startswith(letra):
            nova_tupla = nova_tupla + (nome,)
    return nova_tupla

def main():
    tam_tupla = int(input("Informe o tamanho da tupla: "))
    
    print("Informe os nomes: ")
    tupla_nomes = gerar_tupla(tam_tupla)
    
    letra_especifica = input("Informe uma letra: ")

    nomes_filtrados = filtrar_nomes(tupla_nomes, letra_especifica)
    print(f"Nomes que começam com a letra '{letra_especifica}':", nomes_filtrados)

if __name__ == "__main__":
    main()
