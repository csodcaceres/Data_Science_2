# Una posible solución a este punto la encuentras a continuación:

dias = int(input("¿Cuántas diarias? "))
ciudad = input("¿Cuál es la ciudad? [Salvador, Fortaleza, Natal o Aracaju]: ")
distancias = [850, 800, 300, 550]
paseo = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gastos_gasolina(ciudad):
    if ciudad == 'Salvador':
        return (2 * distancias[0] * gasolina ) / km_l
    elif ciudad == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif ciudad == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif ciudad == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_paseo(ciudad, dias):
    if ciudad=="Salvador":
        return paseo[0] * dias
    elif ciudad=="Fortaleza":
        return paseo[1] * dias
    elif ciudad=="Natal":
        return paseo[2] * dias 
    elif ciudad=="Aracaju":
        return paseo[3] * dias 
    
gastos = gasto_hotel(dias) + gastos_gasolina(ciudad) + gasto_paseo(ciudad, dias)
print(f"Con base en los gastos definidos, un viaje de {dias} días a {ciudad} desde Recife costaría {round(gastos, 2)} reales")
