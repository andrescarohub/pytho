#Crea un programa que le pida al usuario su edad y si tiene su documento de identidad (sí o no).
#Con esa info, el programa decide si puede entrar o no a la discoteca.

edad=int(input("ingrese su edad porfavor :"))
documento=input("trae el documento de c.c con usted ? :")

match(edad,documento):
    case (18,_) :
        print("hey bro estrenando c.c eh :")
    case (e,"si") if e >= 18:
        print("ok bro pasale y disfruta ")

    case (_,d) if d != "si"  :
        print("perdon bro debes terner tu documento ")    
    case (e,d) if d == "si" and e <18:
        print("perdon bro pero en el documento dice que eres menor de edas !sorry!")
   
    case _:
        print("sorry bro vete ")        
