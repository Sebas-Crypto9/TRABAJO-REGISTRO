def main():
    # Primer nombre (obligatorio)
    while True:
        primer_nombre = input("Ingrese su primer nombre: ").strip()
        if primer_nombre.isalpha():
            break
        else:
            print("❌ Error: Solo se permiten letras en el primer nombre. Intente nuevamente.")

    # Segundo nombre (opcional)
    while True:
        segundo_nombre = input("Ingrese su segundo nombre (opcional, puede dejar vacío): ").strip()
        if segundo_nombre == "" or segundo_nombre.isalpha():
            break
        else:
            print("❌ Error: Solo se permiten letras en el segundo nombre. Intente nuevamente.")
    # Primer apellido (obligatorio)
    while True:
        primer_apellido = input("Ingrese su primer apellido: ").strip()
        if primer_apellido.isalpha():
            break
        else:
            print("❌ Error: Solo se permiten letras en el primer apellido. Intente nuevamente.")

    # Segundo apellido (obligatorio)
    while True:
        segundo_apellido = input("Ingrese su segundo apellido: ").strip()
        if segundo_apellido.isalpha():
            break
        else:
            print("❌ Error: Solo se permiten letras en el segundo apellido. Intente nuevamente.")

     # Edad (obligatorio)
    while True:
        edad = input("Ingrese su edad: ").strip()
        if edad.isdigit():
            break
        else:
            print("❌ Error: Solo se permiten números en la edad. Intente nuevamente.")

    # Año de nacimiento (obligatorio)
    while True:
        año_nacimiento = input("Ingrese su año de nacimiento: ").strip()
        if año_nacimiento.isdigit():
            break
        else:
            print("❌ Error: Solo se permiten números en el año de nacimiento. Intente nuevamente.")

    print(f"EL USUARIO IDENTIFICADO CON EL NOMBRE DE {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido} CON LA EDAD DE {edad} AÑOS NACIDO EL AÑO {año_nacimiento} HA SIDO REGISTRADO CORRECTAMENTE")


if __name__ == "__main__":
    main()