# Criar tupla com base no tamanho informado pelo usuário
def gerar_tupla(tam_tupla):
    tupla = ()
    for i in range(tam_tupla):
        item = int(input("Informe o item da tupla: "))
        tupla = tupla + (item,)
    return tupla

# Gera a tupla resultante de tupla1 e tupla2
def gerar_tupla_resultante(tupla1, tupla2):
    tam_menor = min(len(tupla1), len(tupla2))
    tupla_elems_soma = ()
    
    for i in range(tam_menor):
        resultado_da_soma = tupla1[i] + tupla2[i]
        tupla_elems_soma = tupla_elems_soma + (resultado_da_soma,)
    
    if len(tupla1) > len(tupla2):
        #pegamos todos os elementos de tupla1 a partir do índice tam_menor até o final".
        tupla_elems_soma = tupla_elems_soma + tupla1[tam_menor:]
    elif len(tupla2) > len(tupla1):
        tupla_elems_soma = tupla_elems_soma + tupla2[tam_menor:]
    
    return tupla_elems_soma

if __name__ == "__main__":
    tam_tupla1 = int(input("Informe o tamanho da tupla 1: "))
    tupla1 = gerar_tupla(tam_tupla1)

    tam_tupla2 = int(input("Informe o tamanho da tupla 2: "))
    tupla2 = gerar_tupla(tam_tupla2)

    tupla_resultante = gerar_tupla_resultante(tupla1, tupla2)
    print("Tupla Resultante:", tupla_resultante)
