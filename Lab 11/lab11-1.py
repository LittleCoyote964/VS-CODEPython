def conversion(Dollar):
    Peso = Dollar / 0.058
    Pesos = f"{Peso:.2f}"
    print("Mexican Pesos: $", Pesos)

Dollar = float(input("Please enter US Dollars: $"))
conversion(Dollar)
