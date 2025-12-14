from generador_codigo import GeneradorCodigo

def main():
    print("=== Generador Automático de Código con IA ===")
    descripcion = input("Describe el código que deseas generar: ")

    generador = GeneradorCodigo()
    codigo = generador.generar(descripcion)

    print("Código generado:")
    print(codigo)

if __name__ == "__main__":
    main()