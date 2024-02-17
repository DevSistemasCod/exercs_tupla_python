# Criar tupla com base no tamanho informado pelo usário
def gerar_tupla(tam_tupla):
    tupla = ()
    for i in range (tam_tupla):
        item = input("Informe o item da tupla: ")
        tupla = tupla + (item,)
    
    return tupla

# gera a tupla resultante de tupla1 e tupla2 
def gerar_tupla_resultante(tupla1, tupla2):
    for i in range(len(tupla1)):
        resultado_da_soma = tupla1[i] + tupla2[i]
        tupla_resultante = tupla_resultante + (resultado_da_soma,)

    return tupla_resultante
  

if __name__ == "__main__":
    tam_tupla1 = int(input("Informe o tamanho da tupla 1: "))
    tam_tupla2 = int(input("Informe o tamanho da tupla 2: "))

    while(tam_tupla1 != tam_tupla2):
        print("Para efetuar a soma dos itens o tamanho deve ser igual: ")
        tam_tupla1 = int(input("Informe o tamanho da tupla 1: "))
        tam_tupla2 = int(input("Informe o tamanho da tupla 2: "))
        
        if tam_tupla1 == tam_tupla2:
            break

    print("  Itens para a 1ª Tupla")
    tupla1 = gerar_tupla(tam_tupla1)
    print("  Itens para a 2ª Tupla")
    tupla2 = gerar_tupla(tam_tupla2)
    
    tupla_resultante = gerar_tupla_resultante(tupla1, tupla2)
    print("Tupla Resultante:", tupla_resultante)