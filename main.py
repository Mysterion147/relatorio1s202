# criação da classe mãe
class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som
    def emitir_som(self):
        print(self.som)
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor

# criação da classe filho
class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        self.tamanho = tamanho
        super().__init__(nome, idade, especie, cor, som)
    def trombar(self):
        print(self.som)
    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

# entrada de dados
input_nome = input("Digite o nome do elefante: ")
input_idade = input("Digite a idade (inteiro) do elefante: ")
input_especie = input("Digite a especie do elefante: ")
input_cor = input("Digite a cor do elefante: ")
input_som = input("Digite o som do elefante: ")
input_tamanho = input("Digite o tamanho do elefante: ")

# criação do objeto com base nas entradas
elefante1 = Elefante(input_nome, input_idade, input_especie, input_cor, input_som, input_tamanho)

# tratamento dos dados como pedido
if(elefante1.especie == "Africano" and int(elefante1.idade) < 10):
    elefante1.mudar_tamanho("pequeno")
    elefante1.som = "Paaah"
elif(elefante1.especie == "Africano" and int(elefante1.idade) > 10):
    elefante1.mudar_tamanho("grande")
    elefante1.som = "PAHHHHHH"

# saída de dados
elefante1.trombar()
print("O tamanho do elefante e", elefante1.tamanho)

# # testes (functioning)
# elefante1.emitir_som()
# elefante1.mudar_cor("Azul")
# print(elefante1.cor)