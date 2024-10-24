class Livro:
    def __init__(self, titulo, autor, ano, dias_atraso):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._dias_atraso = dias_atraso

    def get_titulo(self):
        return self._titulo
    
    def get_autor(self):
        return self._autor
    
    def get_ano(self):
        return self._ano
    
    def get_dias_atraso(self):
        return self._dias_atraso
    
    def calcular_multa(self):
        pass


class LivroFisico(Livro):
    def calcular_multa(self):
        return self._dias_atraso * 2


class LivroDigital(Livro):
    def calcular_multa(self):
        return self._dias_atraso * 1


def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano = int(input("Ano de publicação: "))
    dias_atraso = int(input("Dias de atraso: "))
    tipo = input("Tipo do livro (fisico/digital): ").lower()

    if tipo == "fisico":
        return LivroFisico(titulo, autor, ano, dias_atraso)
    elif tipo == "digital":
        return LivroDigital(titulo, autor, ano, dias_atraso)
    else:
        print("Tipo inválido!")
        return None


def consultar_livro(livro):
    if livro:
        print(f"Título: {livro.get_titulo()}")
        print(f"Autor: {livro.get_autor()}")
        print(f"Ano de Publicação: {livro.get_ano()}")
    else:
        print("Nenhum livro cadastrado.")


def calcular_multa(livro):
    if livro:
        print(f"Multa a pagar: R${livro.calcular_multa():.2f}")
    else:
        print("Nenhum livro cadastrado.")


def menu():
    livro = None

    while True:
        print("\n1. Cadastrar livro")
        print("2. Consultar livro")
        print("3. Calcular multa")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            livro = cadastrar_livro()
        elif opcao == "2":
            consultar_livro(livro)
        elif opcao == "3":
            calcular_multa(livro)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()
