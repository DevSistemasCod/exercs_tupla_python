

def meses_de_inverno_e_outono():
    meses_do_ano = ( "janeiro", "fevereiro", "março", "abril",
    "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
    m_verao = ("dezembro", "janeiro", "fevereiro")
    m_primavera = ("setembro", "outubro", "novembro") 

    # Encontrar meses que não são nem de verão nem de primavera
    tupla_final = set(meses_do_ano) - set(m_verao) - set(m_primavera)
    
    print("Meses que não são de verão nem de primavera:", tupla_final)

def main():
    meses_de_inverno_e_outono()


if __name__ == "__main__":
    main()