from classes import *

print('Avaliação de composição corporal')
print('================================\n')

while True:
    inicio = input('Deseja iniciar uma nova avaliação? (s/n):\n>>> ')
    print('')
    if inicio.upper() != 'S':
        print('Encerrando programa...')
        break
    else:
        print('Insira os dados do avaliado: ')
        a1 = Avaliado(nome=input('Nome: '), idade=input('Idade: '), peso=input("Peso: "), altura=input("Altura (cm): "), sexo=input("sexo (M/F): "))

        print('\nInsira o valor das dobras cutâneas: \n')
        a1_gord = a1.gordura(input('Triciptal: '), input('subescapular: '), input('peitoral: '), input('axilar_media: '), input('abdominal: '), input('suprailiaca: '), input('coxa: '))

        print('\nInsira o valor das circunferências: \n')
        a1_massa = a1.massa_muscular(input('Circunferencia braço E: '), input('Circunferencia braço D: '), input('Circunferencia cintura: '), input('Circunferencia quadril: '), input('Circunferencia coxa E: '), input('Circunferencia coxa D: '), input('Circunferencia panturrilha E: '), input('Circunferencia panturrilha D: '))

        print(f'Resultados da avaliação de {a1.nome}:\n')
        print(f'{a1.imc()}\n\n')
        print(f'{a1_massa}')
        print(f'{a1_gord}\n\n')