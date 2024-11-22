import re

# Función para convertir un valor hexadecimal a su valor ASCII
def hex_to_ascii(hex_value):
    try:
        # Convierte el valor hexadecimal a su representación ASCII
        return chr(int(hex_value, 16))
    except ValueError:
        return ''  # Si hay un error (por ejemplo, valores no hexadecimales), se devuelve una cadena vacía.

# Función para procesar el archivo
def process_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    result = []
    
    for line in lines:
        # Extraemos solo la parte después de la coma, usando expresión regular
        match = re.findall(r'mov\s+BYTE\s+PTR\s+\[rbp-[^\]]+\],(\S+)', line)
        
        # Si encontramos valores hexadecimales, los convertimos
        if match:
            # Convertimos todos los valores hexadecimales a caracteres ASCII
            ascii_chars = [hex_to_ascii(hex_value) for hex_value in match]
            result.append(''.join(ascii_chars))  # Los concatenamos en una sola línea

    return ''.join(result)  # Concatenamos todas las líneas resultantes

# Ruta del archivo de entrada
input_file = 'archivo.txt'  # Cambia esto por la ruta de tu archivo

# Procesamos el archivo y obtenemos el resultado
output = process_file(input_file)

# Mostramos el resultado
print(output)
