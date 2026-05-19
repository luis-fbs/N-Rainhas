import random
import math


def custo(tabuleiro):
    conflitos = 0
    n = len(tabuleiro)

    for i in range(n):
        for j in range(i + 1, n):
            if tabuleiro[i] == tabuleiro[j]:
                conflitos += 1
            if abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def vizinho(tabuleiro):
    coluna = random.randint(0, len(tabuleiro) - 1)
    linha = random.randint(0, len(tabuleiro) - 1)

    nova_configuracao = tabuleiro[:]
    nova_configuracao[coluna] = linha
    return nova_configuracao

def simulated_annealing(n, temperatura=100, alpha=.99, temperatura_minima=.01):
    solucao_atual = [random.randint(0, n - 1) for _ in range(n)]
    melhor_solucao = solucao_atual[:]
    custo_melhor_solucao = custo(melhor_solucao)

    iteracoes = 0
    while temperatura > temperatura_minima:
        if custo(solucao_atual) == 0:
            return solucao_atual, iteracoes

        nova_solucao = vizinho(solucao_atual)
        custo_nova_solucao = custo(nova_solucao)
        delta = custo_nova_solucao - custo(solucao_atual)

        if delta <= 0:
            solucao_atual = nova_solucao
            custo_solucao_atual = custo_nova_solucao
            if custo_solucao_atual < custo_melhor_solucao:
                melhor_solucao = solucao_atual
                custo_melhor_solucao = custo_solucao_atual
        else:
            prob = math.exp(-delta / temperatura)
            if random.random() < prob:
                solucao_atual = nova_solucao

        temperatura *= alpha
        iteracoes +=1
    return melhor_solucao, iteracoes