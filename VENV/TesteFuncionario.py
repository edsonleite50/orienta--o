    """
        Criação de objetos e chamados dos métodos
    """
    from Funcionario import Funcionario


    Funcionario = Funcionario('Antonio' , 'Edson@gmail')

    print (Funcionario)

    Funcionario.cadastro_hora('Jan', 280)
    Funcionario.cadastro_hora('Feb', 250)
    Funcionario.cadastro_salario_hora('Jan', 250)
    Funcionario.cadastro_salario_hora('Feb',250)
    print(funcionario.calcula_salario('Jan'))
    print(funcionario)
    print(funcionario.calcula_salario('Feb'))
    print(funcionario)

    print(repr(funcionario))
    