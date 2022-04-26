class Avaliado:
    '''classe que irá definir características inerentes à pessoas avaliadas'''

    def __init__(self, nome=input('Nome: '), idade=float(input('Idade: ')), peso=float(input("Peso: ")), altura= int(
        input("Altura (cm): "))):
        #construtor (atributos para todos os avaliados)
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura/100

    def imc(self): #calculador do IMC do avaliado
        imc = round(self.peso/(self.altura * self.altura))
        print('============================================\n'
              'Valor IMC\t\t\t\tClassificação\n'
              '============================================\n'
              'Menor que 18,5 kg/m2\tMagreza\n'
              '18,5 a 24,9 kg/m2\t\tNormal\n'
              '25 a 29,9 kg/m2\t\t\tSobrepeso\n'
              '30 a 34,9 kg/m2\t\t\tObesidade grau I\n'
              '35 a 39,9 kg/m2\t\t\tObesidade grau II\n'
              'Maior que 40 kg/m2\t\tObesidade grau III\n')
        if imc <=18.4:
            return(f'seu imc é: {imc}, nível MAGREZA.')
        elif imc <= 24.9:
            return (f'seu imc é: {imc}, nível NORMAL.')
        elif imc <= 29.9:
            return (f'seu imc é: {imc}, nível SOBREPESO.')
        elif imc <= 34.9:
            return (f'seu imc é: {imc}, nível OBESIDADE GRAU I.')
        elif imc <= 39.9:
            return (f'seu imc é: {imc}, nível OBESIDADE GRAU II.')
        else:
            return (f'iseu imc é: {imc}, nível OBESIDADE GRAU III.')

