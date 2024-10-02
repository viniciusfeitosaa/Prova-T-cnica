import time

def contagem_regressiva(segundos):
    while segundos:
        print(f"{segundos} segundos restantes")
        time.sleep(1)
        segundos -= 1
    print("Cooperativismo transforma! 💚")

contagem_regressiva(10)
