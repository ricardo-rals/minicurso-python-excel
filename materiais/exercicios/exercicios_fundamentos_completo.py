"""
================================================================================
EXERCÍCIOS COMPLETOS - TÓPICO 2: FUNDAMENTOS DO PYTHON
Minicurso: Python para Excel
================================================================================

Este arquivo contém exercícios categorizados para prática dos fundamentos:
- Variáveis e Tipos de Dados
- Operadores Aritméticos
- Operadores Relacionais e Lógicos
- Estruturas Condicionais (if/elif/else)
- Estruturas de Repetição (for/while)

Instruções:
1. Leia cada exercício com atenção
2. Tente resolver sozinho antes de ver a solução
3. Execute o código para testar
4. Experimente modificar os valores para entender melhor

================================================================================
"""

# ============================================================================
# PARTE 1: VARIÁVEIS E TIPOS DE DADOS
# ============================================================================

print("="*80)
print("PARTE 1: VARIÁVEIS E TIPOS DE DADOS")
print("="*80)

# ----------------------------------------------------------------------------
# Exercício 1.1: Cadastro de Produto
# ----------------------------------------------------------------------------
print("\n📝 Exercício 1.1: Cadastro de Produto para Planilha Excel")
print("-" * 80)

# SOLUÇÃO:
nome_produto = "Notebook Dell"
quantidade_estoque = 15
preco_unitario = 2899.90
em_promocao = True

print(f"Produto: {nome_produto}")
print(f"Quantidade em Estoque: {quantidade_estoque}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Em Promoção: {'Sim' if em_promocao else 'Não'}")

# Calcular valor total do estoque
valor_total_estoque = quantidade_estoque * preco_unitario
print(f"Valor Total do Estoque: R$ {valor_total_estoque:.2f}")

# ----------------------------------------------------------------------------
# Exercício 1.2: Conversão de Tipos (Casting)
# ----------------------------------------------------------------------------
print("\n📝 Exercício 1.2: Conversão de Tipos")
print("-" * 80)

# SOLUÇÃO:
# Simulando leitura de dados de uma planilha (vem como string)
preco_str = "1250.50"
quantidade_str = "8"

# Converter para tipos numéricos
preco = float(preco_str)
quantidade = int(quantidade_str)

# Realizar cálculos
total = preco * quantidade

print(f"Preço (convertido): R$ {preco:.2f} - Tipo: {type(preco)}")
print(f"Quantidade (convertida): {quantidade} - Tipo: {type(quantidade)}")
print(f"Total calculado: R$ {total:.2f}")

# ----------------------------------------------------------------------------
# Exercício 1.3: Entrada de Dados do Usuário
# ----------------------------------------------------------------------------
print("\n📝 Exercício 1.3: Entrada de Dados para Relatório")
print("-" * 80)

# SOLUÇÃO (comentado para não interromper execução automática):
"""
# Capturar dados do usuário
vendedor = input("Nome do vendedor: ")
mes = input("Mês de referência: ")
vendas = float(input("Total de vendas (R$): "))
comissao_percentual = float(input("Percentual de comissão (%): "))

# Calcular comissão
comissao = vendas * (comissao_percentual / 100)

# Exibir relatório
print(f"\n--- RELATÓRIO DE COMISSÕES ---")
print(f"Vendedor: {vendedor}")
print(f"Mês: {mes}")
print(f"Total de Vendas: R$ {vendas:.2f}")
print(f"Comissão ({comissao_percentual}%): R$ {comissao:.2f}")
"""

# Versão com dados pré-definidos para demonstração:
vendedor = "João Silva"
mes = "Janeiro/2025"
vendas = 15000.00
comissao_percentual = 5.5

comissao = vendas * (comissao_percentual / 100)

print(f"\n--- RELATÓRIO DE COMISSÕES ---")
print(f"Vendedor: {vendedor}")
print(f"Mês: {mes}")
print(f"Total de Vendas: R$ {vendas:.2f}")
print(f"Comissão ({comissao_percentual}%): R$ {comissao:.2f}")


# ============================================================================
# PARTE 2: OPERADORES ARITMÉTICOS
# ============================================================================

print("\n" + "="*80)
print("PARTE 2: OPERADORES ARITMÉTICOS")
print("="*80)

# ----------------------------------------------------------------------------
# Exercício 2.1: Calculadora de Desconto
# ----------------------------------------------------------------------------
print("\n📝 Exercício 2.1: Calculadora de Desconto")
print("-" * 80)

# SOLUÇÃO:
preco_original = 150.00
desconto_percentual = 20

desconto_valor = preco_original * (desconto_percentual / 100)
preco_final = preco_original - desconto_valor

print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}% = R$ {desconto_valor:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")

# Economia
economia = (desconto_valor / preco_original) * 100
print(f"Você economiza: {economia:.1f}%")

# ----------------------------------------------------------------------------
# Exercício 2.2: Cálculo de Média de Notas
# ----------------------------------------------------------------------------
print("\n📝 Exercício 2.2: Cálculo de Média de Notas")
print("-" * 80)

# SOLUÇÃO:
nota1 = 8.5
nota2 = 7.0
nota3 = 9.0
nota4 = 6.5

# Média aritmética
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Notas: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"Média: {media:.2f}")

# ----------------------------------------------------------------------------
# Exercício 2.3: Conversão de Temperatura
# ----------------------------------------------------------------------------
print("\n📝 Exercício 2.3: Converter Celsius para Fahrenheit")
print("-" * 80)

# SOLUÇÃO:
celsius = 25

# Fórmula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit:.1f}°F")

# ----------------------------------------------------------------------------
# Exercício 2.4: Cálculo de Área e Perímetro
# ----------------------------------------------------------------------------
print("\n📝 Exercício 2.4: Cálculo de Área e Perímetro de Retângulo")
print("-" * 80)

# SOLUÇÃO:
largura = 15
altura = 8

area = largura * altura
perimetro = 2 * (largura + altura)

print(f"Dimensões: {largura}m × {altura}m")
print(f"Área: {area} m²")
print(f"Perímetro: {perimetro} m")

# ----------------------------------------------------------------------------
# Exercício 2.5: Divisão Inteira e Resto
# ----------------------------------------------------------------------------
print("\n📝 Exercício 2.5: Divisão de Produtos em Pacotes")
print("-" * 80)

# SOLUÇÃO:
total_produtos = 47
produtos_por_pacote = 6

pacotes_completos = total_produtos // 6  # Divisão inteira
produtos_sobrando = total_produtos % 6   # Resto da divisão

print(f"Total de produtos: {total_produtos}")
print(f"Produtos por pacote: {produtos_por_pacote}")
print(f"Pacotes completos: {pacotes_completos}")
print(f"Produtos sobrando: {produtos_sobrando}")


# ============================================================================
# PARTE 3: OPERADORES RELACIONAIS E LÓGICOS
# ============================================================================

print("\n" + "="*80)
print("PARTE 3: OPERADORES RELACIONAIS E LÓGICOS")
print("="*80)

# ----------------------------------------------------------------------------
# Exercício 3.1: Verificação de Estoque Mínimo
# ----------------------------------------------------------------------------
print("\n📝 Exercício 3.1: Alerta de Estoque Baixo")
print("-" * 80)

# SOLUÇÃO:
produto = "Mouse Gamer"
quantidade_atual = 8
estoque_minimo = 10

esta_abaixo_minimo = quantidade_atual < estoque_minimo

print(f"Produto: {produto}")
print(f"Quantidade Atual: {quantidade_atual}")
print(f"Estoque Mínimo: {estoque_minimo}")
print(f"Alerta de Estoque Baixo: {esta_abaixo_minimo}")

if esta_abaixo_minimo:
    print("⚠️  ATENÇÃO: Repor estoque!")

# ----------------------------------------------------------------------------
# Exercício 3.2: Validação de Desconto
# ----------------------------------------------------------------------------
print("\n📝 Exercício 3.2: Validar Elegibilidade para Desconto")
print("-" * 80)

# SOLUÇÃO:
# Regra: Desconto para compras >= R$ 100 E cliente é premium
valor_compra = 150.00
cliente_premium = True

tem_desconto = (valor_compra >= 100) and cliente_premium

print(f"Valor da Compra: R$ {valor_compra:.2f}")
print(f"Cliente Premium: {cliente_premium}")
print(f"Elegível para Desconto: {tem_desconto}")

if tem_desconto:
    valor_desconto = valor_compra * 0.15
    print(f"Desconto de 15%: R$ {valor_desconto:.2f}")
    print(f"Valor Final: R$ {(valor_compra - valor_desconto):.2f}")

# ----------------------------------------------------------------------------
# Exercício 3.3: Validação de Múltiplas Condições
# ----------------------------------------------------------------------------
print("\n📝 Exercício 3.3: Sistema de Aprovação de Crédito")
print("-" * 80)

# SOLUÇÃO:
# Aprovado se: salário >= 2000 OU (idade < 30 E tem fiador)
salario = 1800.00
idade = 25
tem_fiador = True

aprovado = (salario >= 2000) or (idade < 30 and tem_fiador)

print(f"Salário: R$ {salario:.2f}")
print(f"Idade: {idade} anos")
print(f"Tem Fiador: {tem_fiador}")
print(f"Crédito Aprovado: {aprovado}")


# ============================================================================
# PARTE 4: ESTRUTURAS CONDICIONAIS (IF/ELIF/ELSE)
# ============================================================================

print("\n" + "="*80)
print("PARTE 4: ESTRUTURAS CONDICIONAIS")
print("="*80)

# ----------------------------------------------------------------------------
# Exercício 4.1: Classificação de Produto por Preço
# ----------------------------------------------------------------------------
print("\n📝 Exercício 4.1: Classificar Produto por Faixa de Preço")
print("-" * 80)

# SOLUÇÃO:
preco = 1250.00

if preco > 1000:
    categoria = "Premium"
elif preco > 500:
    categoria = "Intermediário"
elif preco > 100:
    categoria = "Básico"
else:
    categoria = "Econômico"

print(f"Preço: R$ {preco:.2f}")
print(f"Categoria: {categoria}")

# ----------------------------------------------------------------------------
# Exercício 4.2: Sistema de Notas com Conceitos
# ----------------------------------------------------------------------------
print("\n📝 Exercício 4.2: Converter Nota para Conceito")
print("-" * 80)

# SOLUÇÃO:
nota = 8.5

if nota >= 9.0:
    conceito = "A - Excelente"
elif nota >= 7.0:
    conceito = "B - Bom"
elif nota >= 5.0:
    conceito = "C - Regular"
else:
    conceito = "D - Insuficiente"

print(f"Nota: {nota}")
print(f"Conceito: {conceito}")

# ----------------------------------------------------------------------------
# Exercício 4.3: Cálculo de Frete
# ----------------------------------------------------------------------------
print("\n📝 Exercício 4.3: Calcular Valor do Frete")
print("-" * 80)

# SOLUÇÃO:
valor_compra = 75.00
regiao = "Sul"  # Norte, Sul, Sudeste, Centro-Oeste, Nordeste

# Frete grátis para compras >= R$ 100
if valor_compra >= 100:
    frete = 0
    print("✅ Frete GRÁTIS!")
else:
    # Valor do frete varia por região
    if regiao == "Sul" or regiao == "Sudeste":
        frete = 15.00
    elif regiao == "Centro-Oeste":
        frete = 20.00
    else:  # Norte ou Nordeste
        frete = 25.00

    print(f"Frete para {regiao}: R$ {frete:.2f}")

total = valor_compra + frete
print(f"Valor da Compra: R$ {valor_compra:.2f}")
print(f"Total com Frete: R$ {total:.2f}")

# ----------------------------------------------------------------------------
# Exercício 4.4: Validador de Idade para Categoria
# ----------------------------------------------------------------------------
print("\n📝 Exercício 4.4: Classificar por Faixa Etária")
print("-" * 80)

# SOLUÇÃO:
idade = 16

if idade < 12:
    categoria = "Infantil"
    preco_ingresso = 15.00
elif idade < 18:
    categoria = "Adolescente"
    preco_ingresso = 25.00
elif idade < 60:
    categoria = "Adulto"
    preco_ingresso = 40.00
else:
    categoria = "Idoso"
    preco_ingresso = 20.00

print(f"Idade: {idade} anos")
print(f"Categoria: {categoria}")
print(f"Preço do Ingresso: R$ {preco_ingresso:.2f}")


# ============================================================================
# PARTE 5: ESTRUTURAS DE REPETIÇÃO (FOR)
# ============================================================================

print("\n" + "="*80)
print("PARTE 5: ESTRUTURAS DE REPETIÇÃO - FOR")
print("="*80)

# ----------------------------------------------------------------------------
# Exercício 5.1: Tabuada
# ----------------------------------------------------------------------------
print("\n📝 Exercício 5.1: Gerar Tabuada")
print("-" * 80)

# SOLUÇÃO:
numero = 7

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i} = {resultado}")

# ----------------------------------------------------------------------------
# Exercício 5.2: Soma de Números
# ----------------------------------------------------------------------------
print("\n📝 Exercício 5.2: Somar Números de 1 a 100")
print("-" * 80)

# SOLUÇÃO:
soma = 0
for numero in range(1, 101):
    soma += numero

print(f"Soma de 1 a 100: {soma}")

# Verificação com fórmula: n * (n + 1) / 2
verificacao = 100 * 101 // 2
print(f"Verificação (fórmula): {verificacao}")

# ----------------------------------------------------------------------------
# Exercício 5.3: Processar Lista de Preços
# ----------------------------------------------------------------------------
print("\n📝 Exercício 5.3: Calcular Total de Vendas")
print("-" * 80)

# SOLUÇÃO:
precos = [25.90, 15.50, 48.00, 12.75, 99.90]

total_vendas = 0
print("Processando vendas:")

for i, preco in enumerate(precos, start=1):
    total_vendas += preco
    print(f"  Venda {i}: R$ {preco:.2f}")

media = total_vendas / len(precos)

print(f"\nTotal de Vendas: R$ {total_vendas:.2f}")
print(f"Ticket Médio: R$ {media:.2f}")

# ----------------------------------------------------------------------------
# Exercício 5.4: Contar Produtos em Promoção
# ----------------------------------------------------------------------------
print("\n📝 Exercício 5.4: Contar Produtos em Promoção")
print("-" * 80)

# SOLUÇÃO:
produtos_promocao = [True, False, True, True, False, True, False]

quantidade_em_promocao = 0
for em_promocao in produtos_promocao:
    if em_promocao:
        quantidade_em_promocao += 1

total_produtos = len(produtos_promocao)
percentual = (quantidade_em_promocao / total_produtos) * 100

print(f"Total de Produtos: {total_produtos}")
print(f"Em Promoção: {quantidade_em_promocao}")
print(f"Percentual em Promoção: {percentual:.1f}%")


# ============================================================================
# PARTE 6: ESTRUTURAS DE REPETIÇÃO (WHILE)
# ============================================================================

print("\n" + "="*80)
print("PARTE 6: ESTRUTURAS DE REPETIÇÃO - WHILE")
print("="*80)

# ----------------------------------------------------------------------------
# Exercício 6.1: Contagem Regressiva
# ----------------------------------------------------------------------------
print("\n📝 Exercício 6.1: Contagem Regressiva")
print("-" * 80)

# SOLUÇÃO:
contador = 10

print("Contagem regressiva:")
while contador > 0:
    print(contador, end=" ")
    contador -= 1

print("\n🎉 Fim!")

# ----------------------------------------------------------------------------
# Exercício 6.2: Acumular até Atingir Meta
# ----------------------------------------------------------------------------
print("\n📝 Exercício 6.2: Acumular Vendas até Meta")
print("-" * 80)

# SOLUÇÃO:
meta = 1000.00
vendas_diarias = [150.00, 200.00, 175.00, 225.00, 180.00, 120.00, 95.00]

total_acumulado = 0
dia = 0

while total_acumulado < meta and dia < len(vendas_diarias):
    total_acumulado += vendas_diarias[dia]
    dia += 1
    print(f"Dia {dia}: + R$ {vendas_diarias[dia-1]:.2f} = R$ {total_acumulado:.2f}")

if total_acumulado >= meta:
    print(f"\n✅ Meta atingida em {dia} dias!")
else:
    print(f"\n⚠️  Meta não atingida. Faltam R$ {(meta - total_acumulado):.2f}")

# ----------------------------------------------------------------------------
# Exercício 6.3: Validação de Entrada (Simulado)
# ----------------------------------------------------------------------------
print("\n📝 Exercício 6.3: Validação de Entrada de Dados")
print("-" * 80)

# SOLUÇÃO (simulado sem input real):
# Simula tentativas de entrada
tentativas_validas = [0, -5, 3, 150, 25]  # 25 é válido
tentativa_atual = 0
numero_valido = False

print("Validando entrada (simulação)...")
while not numero_valido and tentativa_atual < len(tentativas_validas):
    numero = tentativas_validas[tentativa_atual]
    tentativa_atual += 1

    if 1 <= numero <= 100:
        numero_valido = True
        print(f"✅ Valor {numero} é válido!")
    else:
        print(f"❌ Valor {numero} inválido. Deve estar entre 1 e 100.")

# ----------------------------------------------------------------------------
# Exercício 6.4: Encontrar Primeiro Múltiplo
# ----------------------------------------------------------------------------
print("\n📝 Exercício 6.4: Encontrar Primeiro Múltiplo de 7 maior que 50")
print("-" * 80)

# SOLUÇÃO:
numero = 51

while numero % 7 != 0:
    numero += 1

print(f"Primeiro múltiplo de 7 maior que 50: {numero}")


# ============================================================================
# PARTE 7: EXERCÍCIOS INTEGRADORES
# ============================================================================

print("\n" + "="*80)
print("PARTE 7: EXERCÍCIOS INTEGRADORES")
print("="*80)

# ----------------------------------------------------------------------------
# Exercício 7.1: Sistema de Caixa Simples
# ----------------------------------------------------------------------------
print("\n📝 Exercício 7.1: Sistema de Caixa com Múltiplos Produtos")
print("-" * 80)

# SOLUÇÃO:
produtos = ["Arroz", "Feijão", "Macarrão", "Óleo"]
precos = [25.90, 8.50, 4.75, 12.00]
quantidades = [2, 3, 5, 1]

print("CUPOM FISCAL")
print("-" * 40)

total_compra = 0

for i in range(len(produtos)):
    subtotal = precos[i] * quantidades[i]
    total_compra += subtotal
    print(f"{quantidades[i]}x {produtos[i]:<15} R$ {precos[i]:>7.2f} = R$ {subtotal:>7.2f}")

print("-" * 40)
print(f"{'TOTAL':<20} R$ {total_compra:>7.2f}")

# Calcular troco
valor_pago = 100.00
troco = valor_pago - total_compra

print(f"{'Valor Pago':<20} R$ {valor_pago:>7.2f}")
print(f"{'Troco':<20} R$ {troco:>7.2f}")

# ----------------------------------------------------------------------------
# Exercício 7.2: Análise de Vendas com Estatísticas
# ----------------------------------------------------------------------------
print("\n📝 Exercício 7.2: Análise Completa de Vendas Mensais")
print("-" * 80)

# SOLUÇÃO:
vendas_mensais = [12000, 15000, 13500, 18000, 16500, 14000, 19500, 21000, 17000, 16000, 20000, 22000]
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

# Calcular estatísticas
total_anual = sum(vendas_mensais)
media_mensal = total_anual / len(vendas_mensais)
maior_venda = max(vendas_mensais)
menor_venda = min(vendas_mensais)

# Encontrar mês com maior e menor venda
mes_maior = meses[vendas_mensais.index(maior_venda)]
mes_menor = meses[vendas_mensais.index(menor_venda)]

print("RELATÓRIO ANUAL DE VENDAS - 2024")
print("=" * 50)

# Exibir vendas mensais
for i in range(len(meses)):
    variacao = ""
    if vendas_mensais[i] > media_mensal:
        variacao = "📈 Acima da média"
    elif vendas_mensais[i] < media_mensal:
        variacao = "📉 Abaixo da média"
    else:
        variacao = "➡️  Na média"

    print(f"{meses[i]}: R$ {vendas_mensais[i]:>10,.2f}  {variacao}")

print("=" * 50)
print(f"Total Anual: R$ {total_anual:,.2f}")
print(f"Média Mensal: R$ {media_mensal:,.2f}")
print(f"Melhor Mês: {mes_maior} (R$ {maior_venda:,.2f})")
print(f"Pior Mês: {mes_menor} (R$ {menor_venda:,.2f})")

# Crescimento
crescimento = ((vendas_mensais[-1] - vendas_mensais[0]) / vendas_mensais[0]) * 100
print(f"Crescimento Jan-Dez: {crescimento:+.1f}%")


# ============================================================================
# FINAL
# ============================================================================

print("\n" + "="*80)
print("✅ EXERCÍCIOS CONCLUÍDOS!")
print("="*80)
print("\n💡 Dicas para continuar praticando:")
print("   1. Modifique os valores e veja o que acontece")
print("   2. Tente resolver sem olhar as soluções")
print("   3. Crie seus próprios exercícios baseados nestes exemplos")
print("   4. Experimente combinar conceitos diferentes")
print("\n🚀 Continue praticando e bons estudos!")
print("="*80)
