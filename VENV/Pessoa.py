class Pessoa :
    "Isto é uma classe chamada Pessoa"

    Idade = 15

    def saudacao(self):
        print("Olá Pessoas !!!")

print(Pessoa.idade)
print(Pessoa.saudacao)

objetoPessoa = Pessoa()

objetoPessoa.saudacao()
print(objetoPessoa.idade)
