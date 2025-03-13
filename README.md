Introduccion 
Mi informe describe la implementación de dos programas en Python para cifrar y descifrar mensajes utilizando el cifrado César con un desplazamiento aleatorio. La estrategia utilizada permite incluir de forma segura el desplazamiento en el mensaje cifrado, asegurando su posterior recuperación para el descifrado
Metodo de mi estrategia 
consiste en desplazar cada letra del mensaje original un número  de posiciones en el alfabeto. Para garantizar que el receptor pueda descifrar el mensaje sin conocer previamente , se incluye este valor en las primeras dos letras del mensaje cifrado. La técnica empleada es la siguiente:
Se generan dos letras iniciales que representan , donde:
La primera letra codifica la parte entera de la división de  entre 26.
La segunda letra codifica el residuo de la división de  entre 26.
Estas dos letras se anteponen al mensaje cifrado, permitiendo la recuperación de  en el proceso de descifrado.
Comentarios 
Este enfoque permite cifrar y descifrar mensajes de manera eficiente utilizando el cifrado César con un desplazamiento aleatorio. La inclusión de  dentro del mensaje cifrado permite su correcta recuperación sin la necesidad de transmitirlo por separado, lo que mejora la seguridad básica del método.
