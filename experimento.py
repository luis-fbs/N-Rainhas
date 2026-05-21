import time
from statistics import mean

from main import simulated_annealing, custo

N = [8, 16, 32, 128]
T = [10, 100, 1000]
alpha = [0.99, 0.8, 0.5]

print("N;temperatura;alpha;tempo_medio;media_iteracoes;media_conflitos;solucoes_otimas")

for n in N:
    for t in T:
        for a in alpha:
            tempos = []
            iteracoes = []
            conflitos = []
            solucoes_otimas = 0
            for _ in range(20):
                inicio = time.time()
                resultado, i = simulated_annealing(n, t, a)
                fim = time.time()
                tempos.append(fim - inicio)
                iteracoes.append(i)
                custo_resultado = custo(resultado)
                if custo_resultado == 0:
                    solucoes_otimas += 1
                conflitos.append(custo(resultado))

            print(
                f"{n};{t};{a};"
                f"{mean(tempos):.4f};"
                f"{mean(iteracoes):.4f};"
                f"{mean(conflitos):.4f};"
                f"{solucoes_otimas}"
            )
