# função para criar uma tupla
def gerar_tupla(tam_tupla):
    tupla = ()
    for i in range (tam_tupla):
        item = int(input("Informe o item da tupla: ")) 
        #cria a tupla por meio da concatenação de seus elementos
        tupla = tupla + (item,)
    
    return tupla

def main():
    meus_numeros = (7, 8, 9, 10)
    
    # obter o tamanho da tupla
    tam_tupla = int(input("Informe o tamanho da tupla: "))
    # cria a tupla por meio do método gerar_tupla(tam_tupla)
    # e retorna a tupla criada para a variável tupla
    tupla = gerar_tupla(tam_tupla)

    # concatenação da tupla mais meus_numeros
    tupla_final = tupla + meus_numeros
    print(tupla_final)
    # retorna o indice do valor passado no método .index()
    indice = tupla_final.index(7)
    print("Indice da primeira ocorrência do valor 7: ",indice)
    print(f"Item do indice {indice-1} é: {tupla_final[indice-1]}")

if __name__ == "__main__":
    main()