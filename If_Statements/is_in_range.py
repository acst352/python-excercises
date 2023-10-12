# Make a program that asks the number between 1 and 10. If the number is out of range the program should display “invalid number”.

def ask_number():
    try:
        number = int(input("Ingrese un número dentro de 1 y 10: "))

        if 1 <= number <= 10:
            print("Correcto, el número que ingresaste está dentro del rango.")
        else:
            print(
                "El número que ingresaste es inválido. Debe estar dentro del rango de 1 a 10."
            )
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")


ask_number()