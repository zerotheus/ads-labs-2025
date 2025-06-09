def soma_pares(n):
    return sum(i for i in range(2, n + 1, 2))

def main():
    n = int(input("Digite um número inteiro positivo: "))
    resultado = soma_pares(n)
    print(f"A soma dos números pares de 1 até {n} é {resultado}")

if __name__ == "__main__":
    main()
