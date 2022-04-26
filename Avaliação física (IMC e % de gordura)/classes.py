class Avaliado:
    """classe que irá definir características inerentes à pessoas avaliadas"""

    def __init__(self, nome=input('Nome: '), idade=float(input('Idade: ')), peso=float(input("Peso: ")), altura= int(input("Altura (cm): "))):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura/100

    def imc(self):
        """calculadora de imc junto de sua tabela"""
        imc = round(self.peso/(self.altura * self.altura))
        print('\n\n==============================================\n'
              'Valor IMC\t\t\t\tClassificação\n'
              '==============================================\n'
              'Menor que 18,5 kg/m2\tMagreza\n'
              '18,5 a 24,9 kg/m2\t\tNormal\n'
              '25 a 29,9 kg/m2\t\t\tSobrepeso\n'
              '30 a 34,9 kg/m2\t\t\tObesidade grau I\n'
              '35 a 39,9 kg/m2\t\t\tObesidade grau II\n'
              'Maior que 40 kg/m2\t\tObesidade grau III\n'
              '==============================================')
        if imc <= 18.4:
            print(f'\nseu imc é: {imc}, nível MAGREZA.')
        elif imc <= 24.9:
            print(f'\nseu imc é: {imc}, nível NORMAL.')
        elif imc <= 29.9:
            print(f'\nseu imc é: {imc}, nível SOBREPESO.')
        elif imc <= 34.9:
            print(f'\nseu imc é: {imc}, nível OBESIDADE GRAU I.')
        elif imc <= 39.9:
            print(f'\nseu imc é: {imc}, nível OBESIDADE GRAU II.')
        elif imc > 39.9:
            print(f'\nseu imc é: {imc}, nível OBESIDADE GRAU III.')


class Gordura(Avaliado):
    """Classe de calculo de gordura herdando classe Avaliado"""
    def __init__(self, triciptal = float(input('dobra triciptal: ')), subescapular = float(input('dobra Subscapular: ')), peitoral = float(input('dobra Peitoral: ')), axilar_media = float(input('dobra Axilar Média: ')), abdominal = float(input('dobra Abdominal: ')), suprailiaca = float(input('dobra Suprailíaca: ')), coxa = float(input('dobra Coxa: '))):
        super().__init__()
        self.triciptal = triciptal
        self.subescapular = subescapular
        self.peitoral = peitoral
        self.axilar_media = axilar_media
        self.abdominal = abdominal
        self.suprailiaca = suprailiaca
        self.coxa = coxa

    def calculo_gordura(self):
        """Formulas para calcular gordura (jackson & Pollock 7 dobras)"""
        dc = 1.112 - 0.00043499 * (self.triciptal+self.subescapular+self.peitoral+self.axilar_media+self.abdominal+self.suprailiaca+self.coxa) + 0.00000055 * (self.triciptal+self.subescapular+self.peitoral+self.axilar_media+self.abdominal+self.suprailiaca+self.coxa) * 2 - 0.00028826 * self.idade
        percentual_gordura = ((4.95/dc) - 4.50)*100
        return f'\nSeu percentual de gordura é {"%.2f" %percentual_gordura}%'
