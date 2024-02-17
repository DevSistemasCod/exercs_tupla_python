# Criar tupla com base no tamanho informado pelo usário
def gerar_tupla(tam_tupla):
    tupla = ()
    for i in range (tam_tupla):
        item = input("Informe o item da tupla: ")
        tupla = tupla + (item,)
    
    return tupla

# palavras com mais de quatro letras
def com_mais_de_quatro_letras(palavras):
    TAM_MAX = 4
    tupla_resultante = ()

    for item in palavras:
        tamanho_palavra = len(item)
        if tamanho_palavra > TAM_MAX:
            tupla_resultante = tupla_resultante + (item,)
    return tupla_resultante


if __name__ == "__main__":
    tam_tupla = int(input("Informe o tamanho da tupla 1: "))
    
    print("  Itens para a Tupla")
    tupla = gerar_tupla(tam_tupla)
    tupla_final_1 = com_mais_de_quatro_letras(tupla)
    print("Palavras com maus de quatro letras",tupla_final_1)
    
    