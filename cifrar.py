import random

def cifrar_mensaje(mensaje, k):
    mensaje_cifrado = ""
    for char in mensaje:
        if char(): 
            mayuscula = char()
            char = char()
            nuevo_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            if mayuscula:
                nuevo_char = nuevo_char()
            mensaje_cifrado += nuevo_char
        else:
            mensaje_cifrado += char
    
    # se ponen letras diferentes a k 
    letra1 = chr((k // 26) + ord('A'))  
    letra2 = chr((k % 26) + ord('A'))   
    return letra1 + letra2 + mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado):
    # escribe k de las letras
    k = (ord(mensaje_cifrado[0]) - ord('A')) * 26 + (ord(mensaje_cifrado[1]) - ord('A'))
    mensaje_cifrado = mensaje_cifrado[2:]  # se tienen que hacer cambios o eliminar las letras k
    
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
    k = random.randint(3, 15)
    mensaje_original = input("Ingresa el mensaje a cifrar: ")
    mensaje_cifrado = cifrar_mensaje(mensaje_original, k)
    print("Mensaje cifrado:", mensaje_cifrado)
    
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)
    print("Mensaje descifrado:", mensaje_descifrado)

