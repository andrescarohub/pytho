productos=["casa","gorra","terrenario","frijoles"]

precios={
    "casa":2000000,
    "gorra":12000,
    "terrenario":32000,
    "frijoles":12
}

for p in productos:

  print(f"{p.title()} tiene un valor de : {precios[p]}")
