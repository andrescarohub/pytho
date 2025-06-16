productos=["casa","gorra","terrenario","frijoles"]

precios={
    "casa":2000000,
    "gorra":12000,
    "terrenario":32000,
    "frijoles":12
}


minuta =[]

while True :
    orden = input("dime que quieres comer ? (oprime '1' para salir )(y si quiere ver su orden oprima 2)")

    if orden == "1" :
        break
    elif orden in precios:
        minuta.append(orden)

    else :
        print("pide otra cosa ojete ")

  

       