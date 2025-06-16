precios={
"hamburguesa":50000,
"hotdogs":23000,
"desgranado":22500,
"pizza":23987,
"albhondigas":19000,
"papas":4000
}
print("estos son los precios de algunos productos:", precios ["hamburguesa"] , precios ["pizza"] )

precios["perico"]= 2
precios["gorra"]=3
precios["hamburguesa"]=12
del precios["desgranado"]
print(f"estos son la listas actualizadas: {precios}")