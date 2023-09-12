altura = float(input("Qual a altura da parede a ser pintada? "))
largura = float(input("Qual a largura da parede a ser pintada? "))
area = altura*largura
quantidade = area/2
print("Para pintar essa parede serão necessários {} litros de tinta".format(quantidade))