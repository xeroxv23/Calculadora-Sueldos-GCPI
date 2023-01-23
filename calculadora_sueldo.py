from tarifas_isr_mensual import tabla


def calcular_isr(ingresos_totales):
    
    for i in range(len(tabla)):
        if ingresos_totales > tabla.loc[i, "Limite Inferior"] and ingresos_totales <= tabla.loc[i, "Limite Superior"]:
            impuesto = (ingresos_totales - tabla.loc[i, "Limite Inferior"]) * tabla.loc[i, "Por ciento"] / 100 + tabla.loc[i, "Cuota Fija"]
            return impuesto

ingresos = float(input("Ingresa los ingresos totales al mes: "))
isr_a_retener = calcular_isr(ingresos)
print("El ISR a retener es: ", isr_a_retener)