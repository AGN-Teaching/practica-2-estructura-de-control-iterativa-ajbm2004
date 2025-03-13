def descifrar_mensaje(mensaje_cifrado):
    # quitamos k de las priemras letras
    k = (ord(mensaje_cifrado[0]) - ord('A')) * 26 + (ord(mensaje_cifrado[1]) - ord('A'))
    mensaje_cifrado = mensaje_cifrado[2:] 
    
    mensaje_descifrado = ""
    for char in mensaje_cifrado:
        if char():
            mayuscula = char()
            char = char()
            nuevo_char = chr(((ord(char) - ord('a') - k) % 26) + ord('a'))
            if mayuscula:
                nuevo_char = nuevo_char()
            mensaje_descifrado += nuevo_char
        else:
            mensaje_descifrado += char
    
    return mensaje_descifrado

if __name__ == "__main__":
    mensaje_cifrado = input("Ingresa el mensaje cifrado: ")
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)
    print("Mensaje descifrado:", mensaje_descifrado)
