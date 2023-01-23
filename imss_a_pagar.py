def calcular_imss_a_pagar():
    suma_percepciones = float(input("Ingrese la suma de percepciones: "))
    if suma_percepciones <= 9538.48:
            imss_a_pagar = suma_percepciones * 0.0304 
    else:
            imss_a_pagar = 289.16
    print("IMSS a pagar: ",imss_a_pagar)
    return imss_a_pagar

calcular_imss_a_pagar()
