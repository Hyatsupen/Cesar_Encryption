def descifrar(texto, desplazamiento=3):
    resultado = []
    for char in texto:
        codigo = ord(char)
        if 32 <= codigo <= 126:  # ASCII imprimible
            nuevo = 32 + (codigo - 32 - desplazamiento) % 95
            resultado.append(chr(nuevo))
        else:
            resultado.append(char)
    return ''.join(resultado)