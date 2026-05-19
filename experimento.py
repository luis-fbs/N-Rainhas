import time
from statistics import mean

import main
from main import simulated_annealing, custo

N = [8, 16, 32, 128]
T = [10, 100, 1000]
alpha = [0.99, 0.5]

for n in N:
    print(f"============{n}===========")
    for t in T:
        for a in alpha:
            print(f"N = {n}, Temperatura = {t} e alpha = {a}")
            tempos = []
            iteracoes = []
            conflitos = []
            solucoes_otimas = 0
            for _ in range(3):
                inicio = time.time()
                resultado, i = simulated_annealing(n, t, a)
                fim = time.time()
                tempos.append(fim - inicio)
                iteracoes.append(i)
                custo_resultado = custo(resultado)
                if custo_resultado == 0:
                    solucoes_otimas += 1
                conflitos.append(custo(resultado))

            print(f"""
                Tempo médio: {mean(tempos):.4f}
                Média de iteracoes: {mean(iteracoes):.4f}
                Media de conflitos: {mean(conflitos):.4f}
                Solucoes otimas: {solucoes_otimas}
            """)