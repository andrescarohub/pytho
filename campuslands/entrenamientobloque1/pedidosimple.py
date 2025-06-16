#crea un menu 
#que recoja la orden 
#calcule el total 

def calcular_orden(precios,orden):
    total=0
    for i in orden:
        total += precios[i]
    return total

productos=["burguer","salchicha","perro",";langostin"]
precios={"burguer":11,"salchicha":12,"perro":4378,";langostin":12}
orden=[]


while True:
    pedido=input("ingrese que quiere comer: (oprima 'x' para salir )")
    if pedido == "x":
        break
    elif pedido in precios :
        orden.append(pedido)
        print(f"{pedido.title()}su pedido fue agregado exitosamente")
    else:
        print("no tenemos eso pirobo :")


print("---------su orden señor --------")
if orden:
    print("usted ordeno ")
    for i in orden:
        print(f"{i.title()}")
    total_a_pagar = calcular_orden(precios,orden)
    print("--------------------------------------")
    print(f"total a pagar es : {total_a_pagar}")
else:
    print("no ordeno nada usted joven ")
