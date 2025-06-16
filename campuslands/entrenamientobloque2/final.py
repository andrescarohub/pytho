#Registrar estudiantes (nombre, edad, ciudad)
estudiantes=[]
def registrar_estudiantes() :
    nombre=input("ingrese su nombre")
    edad=int(input("ingrese su edad "))
    ciudad=input("ingrese su ciudad de nacimiento ")
    estudiante = {"nombre":nombre,"edad":edad,"ciudad":ciudad}
    estudiantes.append(estudiante)
    print("✅ estudiante guardado ")

#Listarlos

def listar_estudiantes():
    if not estudiantes:
        print("🚫 No hay estudiantes registrados.")
    else:
        print("-_-_-_-_-_ Listado de estudiantes inscritos ✅")
        for i, estudiante in enumerate(estudiantes):
            print(f"{i+1}). {estudiante['nombre']} // {estudiante['edad']} // {estudiante['ciudad']}")

#Buscar uno por nombre
def buscar_estudiante():
    buscar = input("¿Qué estudiante deseas buscar? ")
    encontrados = [e for e in estudiantes if e["nombre"].lower() == buscar.lower()]
    
    if encontrados:
        print("------ Estudiantes encontrados ------")
        for i, estudiante in enumerate(encontrados):
            print(f"{i+1}). {estudiante['nombre']} // {estudiante['edad']} // {estudiante['ciudad']}")
    else:
        print("🚫 No se encontró ningún estudiante con ese nombre.")


#Salir

while True:

    print("""
--- MENÚ DE OPCIONES ---
1. Registrar estudiante
2. Listar estudiantes
3. Buscar estudiante
4. Salir
""")
    opcion=input("selecciona una opcion :")

    if opcion == "1":
        print(registrar_estudiantes())

    elif opcion =="2":
        print(listar_estudiantes())
    elif opcion == "3":
        print(buscar_estudiante())
    elif opcion == "4":
        print("bien echo bro lo hiciste genial ")
        break  
    else:
        print("bro opcion no valida ")          


