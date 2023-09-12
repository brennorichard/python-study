# Imports
import subprocess
import os
import time

# Definindo caminhos para execução dos exercícios
caminho_ex1 = os.path.relpath('python-study/exercicios/ex1.py')
caminho_ex2 = os.path.relpath('python-study/exercicios/ex2.py')
caminho_ex3 = os.path.relpath('python-study/exercicios/ex3.py')
caminho_ex4 = os.path.relpath('python-study/exercicios/ex4.py')
caminho_ex5 = os.path.relpath('python-study/exercicios/ex5.py')
caminho_ex6 = os.path.relpath('python-study/exercicios/ex6.py')
caminho_ex7 = os.path.relpath('python-study/exercicios/ex7.py')
caminho_ex8 = os.path.relpath('python-study/exercicios/ex8.py')
caminho_ex9 = os.path.relpath('python-study/exercicios/ex9.py')
caminho_ex10 = os.path.relpath('python-study/exercicios/ex10.py')
caminho_ex11 = os.path.relpath('python-study/exercicios/ex11.py')
caminho_ex12 = os.path.relpath('python-study/exercicios/ex12.py')
caminho_ex13 = os.path.relpath('python-study/exercicios/ex13.py')
caminho_ex14 = os.path.relpath('python-study/exercicios/ex14.py')
caminho_ex15 = os.path.relpath('python-study/exercicios/ex15.py')

# Printando lista de opções
resposta = ""

while resposta != 0:
    print(" ")
    print("LISTA DE EXERCÍCIOS:\n[0] SAIR\n[1] Exercício 1 - Olá Mundo\n[2] Exercício 2 - Apresentação\n[3] Exercício 3 - Soma de Inteiros\n[4] Exercício 4 - Dissecando uma variável\n[5] Exercício 5 - Antecessor e Sucessor\n[6] Exercício 6 - Dobro, Triplo e Raiz quadrada\n[7] Exercício 7 - Média Aritmética\n[8] Exercício 8 - Conversão de medidas\n[9] Exercício 9 - Tabuada \n[10] Exercício 10 - Conversor de Dólar\n[11] Exercício 11 - Pintura de parede\n[12] Exercício 12 - Desconto do produto\n[13] Exercício 13 - Aumento no salário\n[14] Exercício 14 - Conversor de temperatura\n[15] Exercício 15 - Aluguel de carros")
    print(" ")
    resposta = int(input("Digite o número do exercíco que deseja executar: "))
    
    if resposta == 1:
        print(" ")
        print("Executando exercício 1...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex1])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 2:
        print(" ")
        print("Executando exercício 2...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex2])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))
        
    elif resposta == 3:
        print(" ")
        print("Executando exercício 3...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex3])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))
    
    elif resposta == 4:
        print(" ")
        print("Executando exercício 4...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex4])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))
    
    elif resposta == 5:
        print(" ")
        print("Executando exercício 5...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex5])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))
    
    elif resposta == 6:
        print(" ")
        print("Executando exercício 6...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex6])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))
    
    elif resposta == 7:
        print(" ")
        print("Executando exercício 7...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex7])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 8:
        print(" ")
        print("Executando exercício 8...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex8])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 9:
        print(" ")
        print("Executando exercício 9...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex9])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 10:
        print(" ")
        print("Executando exercício 10...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex10])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 11:
        print(" ")
        print("Executando exercício 11...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex11])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))
    
    elif resposta == 12:
        print(" ")
        print("Executando exercício 12...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex12])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 13:
        print(" ")
        print("Executando exercício 13...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex13])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 14:
        print(" ")
        print("Executando exercício 14...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex14])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))

    elif resposta == 15:
        print(" ")
        print("Executando exercício 15...")
        time.sleep(2)
        subprocess.run(['python3', caminho_ex15])
        print(" ")
        time.sleep(2)
        resposta = int(input("Deseja continuar?\n[0] NÃO (ENCERRA O PROGRAMA) \n[1] SIM (RETORNA A LISTAGEM)\n"))