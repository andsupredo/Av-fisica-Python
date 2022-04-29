class Avaliado:
    """classe que irá definir características inerentes à pessoas avaliadas"""

    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)/100
        self.sexo = sexo
        if sexo not in 'mf':
            self.sexo = None

    def imc(self):
        """calculadora de imc junto de sua tabela"""
        imc = (self.peso/(self.altura * self.altura))
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
            return f'\nIMC: {imc:.2f}, nível MAGREZA.'
        elif imc <= 24.9:
            return f'\nIMC: {imc:.2f}, nível NORMAL.'
        elif imc <= 29.9:
            return f'\nIMC: {imc:.2f}, nível SOBREPESO.'
        elif imc <= 34.9:
            return f'\nIMC: {imc:.2f}, nível OBESIDADE GRAU I.'
        elif imc <= 39.9:
            return f'\nIMC: {imc:.2f}, nível OBESIDADE GRAU II.'
        elif imc >= 40:
            return f'\nIMC: {imc:.2f}, nível OBESIDADE GRAU III.'
        else:
            return 'Erro ao calcular IMC.'

    def gordura(self, triciptal, subescapular, peitoral, axilar_media, abdominal, suprailiaca, coxa):
        self.triciptal = float(triciptal)
        self.subescapular = float(subescapular)
        self.peitoral = float(peitoral)
        self.axilar_media = float(axilar_media)
        self.abdominal = float(abdominal)
        self.suprailiaca = float(suprailiaca)
        self.coxa = float(coxa)
        dc = 1.112 - 0.00043499 * (self.triciptal + self.subescapular + self.peitoral + self.axilar_media + self.abdominal + self.suprailiaca + self.coxa) + 0.00000055 * (self.triciptal + self.subescapular + self.peitoral + self.axilar_media + self.abdominal + self.suprailiaca + self.coxa) * 2 - 0.00028826 * self.idade
        percentual_gordura = ((4.95 / dc) - 4.50) * 100
        return f'\nGordura corporal total: {percentual_gordura:.2f}% ({(self.peso * percentual_gordura) / 100:.2f}kg)\n'


    def massa_muscular(self, braco_e, braco_d, cintura, quadril, coxa_e, coxa_d, pant_e, pant_d):
        self.braco_e = float(braco_e)
        self.braco_d = float(braco_d)
        self.cintura = float(cintura)
        self.quadril = float(quadril)
        self.coxa_e = float(coxa_e)
        self.coxa_d = float(coxa_d)
        self.pant_e = float(pant_e)
        self.pant_d = float(pant_d)
        amb = None
        if self.sexo.upper() == 'M':
            amb = ((self.braco_d * 10 - (3.14 * self.triciptal)) * (self.braco_d * 10 - (3.14 * self.triciptal))) / (4 * 3.14) - 10.0
        elif self.sexo.upper() == 'F':
            amb = (((self.braco_d * 10) - (3.14 * self.triciptal)) * ((self.braco_d * 10) - (3.14 * self.triciptal))) / 4 * 3.14 - 6.5
        else:
            print('Erro ao calcular % de massa magra (sexo inválido)')
        return f'Massa muscular: {((self.altura * (0.0264 + (0.029 * amb))) / self.peso) * 10:.2f}% ({(self.altura * (0.0264 + (0.029 * amb))) / 10:.2f}kg)\n'