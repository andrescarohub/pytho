frases = [
    "que huevada ",
    "solo se que nada se ",
    "la  ia acabara con el mundo entero espero ",
]

palabra_clave="nada"
palabra_segunda=" "


resultados=[frases for frases in frases if palabra_clave in frases.lower()]


print(resultados)