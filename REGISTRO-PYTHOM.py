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

if __name__ == "__main__":
    main()