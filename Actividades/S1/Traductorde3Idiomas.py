print("=== Traductor Básico de 3 Idiomas ===")
print("1. Español a Inglés")
print("2. Español a Francés")
print("3. Español a Italiano")

opcion = int(input("¿A qué idioma deseas traducir? Elige 1, 2 o 3: "))

# (Inglés)
if opcion == 1:
    print("\n--- Traductor a Inglés ---")
    palabra = input("Escribe una palabra a traducir (hola, amor, gato): ").lower()

    if palabra == "hola":
        print("La traducción es: HELLO")
    elif palabra == "amor":
        print("La traducción es: LOVE")
    elif palabra == "gato":
        print("La traducción es: CAT")
    else:
        print("Lo siento, esa palabra no está en mi base de datos.")

# (Francés)
elif opcion == 2:
    print("\n--- Traductor a Francés ---")
    palabra = input("Escribe una palabra a traducir (hola, amor, gato): ").lower()
    
    if palabra == "hola":
        print("La traducción es: BONJOUR")
    elif palabra == "amor":
        print("La traducción es: AMOUR")
    elif palabra == "gato":
        print("La traducción es: CHAT")
    else:
        print("Lo siento, esa palabra no está en mi base de datos.")

# (Italiano)
elif opcion == 3:
    print("\n--- Traductor a Italiano ---")
    palabra = input("Escribe una palabra a traducir (hola, amor, gato): ").lower()

    if palabra == "hola":
        print("La traducción es: CIAO")
    elif palabra == "amor":
        print("La traducción es: AMORE")
    elif palabra == "gato":
        print("La traducción es: GATTO")
    else:
        print("Lo siento, esa palabra no está en mi base de datos.")

else:
    print("\nOpción no disponible. Por favor, reinicia el programa y elige 1, 2 o 3.")