from bd import *

# requisitando amostras para o usuário.

Mp10 = int(input("Insira o valor da particula MP10: \n"))
Mp25 = int(input("Insira o valor da particula MP2.5: \n"))
O2 = int(input("Insira o valor da particula 02: \n"))
cO = int(input("Insira o valor da particula CO: \n"))
No2 = int(input("Insira o valor da particula NO2: \n"))
So2 = int(input("Insira o valor da particula SO2: \n"))

# função para cálculo da média.

def MediaCalculo (Mp10,Mp25,O3,cO,No2,So2):

# amostras devem ser positivas.

    if Mp10 >= 0 and Mp25 >= 0 and O2 >=0 and cO >= 0 and No2 >= 0 and So2 >= 0:

        # parâmetros para análise:

        if Mp10 <= 50:
            print("\nA qualidade do ar na particula M10 está BOA! (✿◠‿◠)\n")

        if Mp10 > 50 and Mp10 < 100:
            print("\nA qualidade do ar na particula M10 está REGULAR! (-__-)\n")

        if Mp10 > 100 and Mp10 < 150:
            print("A qualidade do ar na particula M10 está RUIM! (╥_╥)\n")

        if Mp10 > 150 and Mp10 < 250:
            print(
                "A qualidade do ar na particula M10 está MUITO RUIM! (( ˃̣̣̥‸˂̣̣̥)\n")

        if Mp10 > 250:
            print("A qualidade do ar na particula M10 está PÉSSIMA! ლ(｡ -﹏-｡ ლ)\n")

        #############################################################################

        if Mp25 <= 25:
            print("A qualidade do ar na particula MP2.5 está BOA! (✿◠‿◠)\n")

        if Mp25 > 25 and Mp25 < 50:
            print("A qualidade do ar na particula Mp2.5 está REGULAR! (-__-)\n")

        if Mp25 > 50 and Mp25 < 75:
            print("A qualidade do ar na particula Mp2.5 está RUIM! (╥_╥)\n")

        if Mp25 > 75 and Mp25 < 125:
            print(
                "A qualidade do ar na particula Mp2.5 está MUITO RUIM! (( ˃̣̣̥‸˂̣̣̥)\n")

        if Mp25 > 125:
            print("A qualidade do ar na particula Mp2.5 está PÉSSIMA! ლ(｡ -﹏-｡ ლ)\n")

        ############################################################################

        if O2 <= 100:
            print("A qualidade do ar na particula O3 está BOA! (✿◠‿◠)\n")

        if O2 > 100 and O3 < 130:
            print("A qualidade do ar na particula O3 está REGULAR! (-__-)\n")

        if O2 > 130 and O3 < 160:
            print("A qualidade do ar na particula O3 está RUIM! (╥_╥)\n")

        if O2 > 160 and O3 < 200:
            print(
                "A qualidade do ar em na particula O3 está MUITO RUIM! (( ˃̣̣̥‸˂̣̣̥)\n")

        if O2 > 200:
            print("A qualidade do ar em na particula O3 está PÉSSIMA! ლ(｡ -﹏-｡ ლ)\n")

        ############################################################################

        if cO <= 9:
            print("A qualidade do ar na particula CO está BOA! (✿◠‿◠)\n")

        if cO > 9 and cO < 11:
            print("A qualidade do ar na particula CO está REGULAR! (-__-)\n")

        if cO > 11 and cO < 13:
            print("A qualidade do ar na particula CO está RUIM! (╥_╥)\n")

        if cO > 13 and cO < 15:
            print(
                "A qualidade do arna particula CO está MUITO RUIM! (( ˃̣̣̥‸˂̣̣̥)\n")

        if cO > 15:
            print("A qualidade do ar na particula CO está PÉSSIMA! ლ(｡ -﹏-｡ ლ)\n")

        ##############################################################################

        if No2 <= 200:
            print("A qualidade do ar na particula NO2 está BOA! (✿◠‿◠)\n")

        if No2 > 200 and No2 < 240:
            print("A qualidade do ar na particula NO2 está REGULAR! (-__-)\n")

        if No2 > 240 and No2 < 320:
            print("A qualidade do ar na particula NO2 está RUIM! (╥_╥)\n")

        if No2 > 320 and No2 < 1130:
            print(
                "A qualidade do ar na particula NO2 está MUITO RUIM! (( ˃̣̣̥‸˂̣̣̥)\n")

        if No2 > 1130:
            print("A qualidade do ar na particula NO2 está PÉSSIMA! ლ(｡ -﹏-｡ ლ)\n")

        #################################################################################

        if So2 <= 20:
            print("A qualidade do ar na particula SO2 está BOA! (✿◠‿◠)\n")

        if So2 > 20 and So2 < 40:
            print("A qualidade do ar na particula SO2 está REGULAR! (-__-)\n")

        if So2 > 40 and So2 < 365:
            print("A qualidade do ar na particula SO2 está RUIM! (╥_╥)\n")
            
        if So2 > 365 and So2 < 800:
            print(
                "A qualidade do ar na particula SO2 está MUITO RUIM! (( ˃̣̣̥‸˂̣̣̥)\n")

        if So2 > 800:
            print("A qualidade do ar na particula SO2 está PÉSSIMA! ლ(｡ -﹏-｡ ლ)\n")

    else:
        print("Insira um valor positivo para o cálculo. (ㆆ_ㆆ) ")

# cálculo e impressão da média.

media = classificacao()
MediaCalculo (media[0], media[1] , media[2] , media[3]  , media[4] , media[5])

# efeitos na saúde para qualidade péssima. 

if Mp10 > 250 and Mp25 > 125 and O2 > 200 and cO > 15 and No2 > 1130 and So2 > 800: 

    print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Como consequência, ocorre o aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')

# efeitos na saúde para qualidade muito ruim.

elif Mp10 > 150 and Mp10 < 250 and Mp25 > 75 and Mp25 < 125 and O2 > 160 and O2 < 200 and cO > 13 and cO < 15 and No2 > 320 and No2 < 1130 and So2 > 365 and So2 < 800:
     
    print('Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.')

# efeitos na saúde para qualidade ruim.

elif Mp10 > 100 and Mp10 < 150 and Mp25 > 50 and Mp25 < 75 and O2 > 130 and O2 < 160 and cO > 11 and cO < 13 and No2 > 240 and No2 < 320 and So2 > 40 and So2 < 365: 

    print('Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Pode ocasionar também em efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')

# efeitos na saúde para qualidade regular. 
elif Mp10 > 50 and Mp10 < 100 and Mp25 > 25 and Mp25 < 50 and O2 > 100 and O2 < 130 and cO > 9 and cO < 11 and No2 > 200 and No2 < 240 and So2 > 20 and So2 < 40:

    print('Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Como consequência, ocorre o aumento de mortes prematuras em pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).')


