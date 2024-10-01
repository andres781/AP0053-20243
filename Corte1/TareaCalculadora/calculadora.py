class Calculadora:

    def digitar_numeros(self):
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def mostrar_menu(self):
        print("\nMenú Calculadora:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

    def operaciones(self):
        
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione la opción deseada:\n ")

            if opcion == '5':
                print("Saliendo.......")
                break

            elif opcion in ['1', '2', '3', '4']:
                a,b = self.digitar_numeros()

                if opcion == '1':
                    resul = self.suma(a, b)
                    print(f"Resultado de la suma: {resul}")

                elif opcion == '2':
                    resul = self.resta(a, b)
                    print(f"Resultado de la resta: {resul}")

                elif opcion == '3':
                    resul= self.mult(a, b)
                    print(f"Resultado de la multiplicación: {resul}")

                elif opcion == '4':
                    try:
                        resul = self.div(a, b)
                        print(f"Resultado de la división: {resul}")

                    except ValueError as error:
                        print(error)
            else:
                print("Opción no válida. Seleccione nuevamente.")


