class Avaliado:
    """classe que irá definir características inerentes à pessoas avaliadas"""

    def __init__(self, nome=input('Nome: '), idade=float(input('Idade: ')), peso=float(input("Peso: ")), altura= int(input("Altura (cm): ")), sexo=input("sexo (M/F): ")):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura/100
        self.sexo = sexo

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
        return f'\nGordura corporal total: {percentual_gordura:.2f}% ({(self.peso * percentual_gordura)/100:.2f}kg)\n'


class MassaMuscular(Gordura):
    """Classe de calculo de massa muscular"""
    def __init__(self, braco_e=float(input('Circunferencia braço E: ')), braco_d=float(input('Circunferencia braço D: ')), cintura=float(input('Circunferencia cintura: ')), quadril=float(input('Circunferencia quadril: ')), coxa_e=float(input('Circunferencia coxa E: ')), coxa_d=float(input('Circunferencia coxa D: ')), pant_e=float(input('Circunferencia panturrilha E: ')), pant_d=float(input('Circunferencia panturrilha D: '))):
        super().__init__()
        self.braco_e = braco_e
        self.braco_d = braco_d
        self.cintura = cintura
        self.quadril = quadril
        self.coxa_e = coxa_e
        self.coxa_d = coxa_d
        self.pant_e = pant_e
        self.pant_d = pant_d

    def calculo_musc(self):  # Método dos calculos de massa muscular.
        amb = None
        if self.sexo.upper() == 'M':
            amb = ((self.braco_d * 10 - (3.14 * self.triciptal)) * (self.braco_d * 10 - (3.14 * self.triciptal))) / (4 * 3.14) - 10.0
        elif self.sexo.upper() == 'F':
            amb = (((self.braco_d * 10) - (3.14 * self.triciptal)) * ((self.braco_d * 10) - (3.14 * self.triciptal))) / 4 * 3.14 - 6.5
        else:
            print('Erro ao calcular % de massa magra (sexo inválido)')
        return f'Massa muscular: {((self.altura * (0.0264 + (0.029 * amb)))/self.peso)*10:.2f}% ({(self.altura * (0.0264 + (0.029 * amb)))/10:.2f}kg)\n'
