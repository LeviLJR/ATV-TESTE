# Valores de faturamento por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o valor total de faturamento
total_faturamento = sum(faturamento.values())

# Calcula o percentual de representação de cada estado
percentual_representacao = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}

# Imprime os resultados
for estado, percentual in percentual_representacao.items():
    print(f"Estado: {estado} - Percentual: {percentual:.2f}%")
