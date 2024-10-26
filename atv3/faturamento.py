import json

def calcular_faturamento(faturamento_diario):
    # Filtrar dias com valor válido (ignorar dias com valor igual a 0)
    valor_valido = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    print(valor_valido)
    # Calcular o menor e maior valor
    menor_valor = min(valor_valido)
    maior_valor = max(valor_valido)

    # Calcular a média mensal
    media_mensal = sum(valor_valido) / len(valor_valido)

    # Contar dias com valor acima da média
    dias_acima_da_media = sum(1 for dia in valor_valido if dia > media_mensal)

    return menor_valor, maior_valor, dias_acima_da_media

# Carregar dados do JSON
with open('dados.json', 'r') as file:
    faturamento_diario = json.load(file)

menor_valor, maior_valor, dias_acima_da_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias com valor acima da média: {dias_acima_da_media}")
