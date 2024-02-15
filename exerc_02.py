# Gerar tupla de elementos únicos
def criar_conjunto_unico(tupla1, tupla2):
    tupla_final = ()
    conjunto1 = set(tupla1)
    conjunto2 = set(tupla2)
    
    conjunto_unico = conjunto1.intersection(conjunto2)
    tupla_final = (conjunto_unico)
    return tupla_final

# Criar tupla com base no tamanho informado pelo usário
def gerar_tupla(tam_tupla):
    tupla = ()
    for i in range (tam_tupla):
        item = (input("Informe o item da tupla: ")) 
        tupla = tupla + (item,)
    
    return tupla


def main():
    tam_tupla1 = int(input("Informe o tamanho da tupla 1: "))
    tam_tupla2 = int(input("Informe o tamanho da tupla 2: "))

    print("  Itens para a 1ª Tupla")
    tupla1 = gerar_tupla(tam_tupla1)
    print("  Itens para a 2ª Tupla")
    tupla2 = gerar_tupla(tam_tupla2)

    tupla_resultante = criar_conjunto_unico(tupla1, tupla2)

    # Exibir o resultado
    print("Conjunto com elementos comuns nas duas tuplas:", tupla_resultante)



if __name__ == "__main__":
    main()
