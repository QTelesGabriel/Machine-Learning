# Implementação do Algoritmo de Redes Bayesianas

# Defina a estrutura da Rede Bayesiana
# Exemplo: A -> B -> C
# A: Alarme, B: Arrombamento, C: Terremoto

# Defina as probabilidades condicionais
# P(A)
P_A = 0.001

# P(B | A)
P_B_dado_A = {
    'Verdadeiro': 0.95,
    'Falso': 0.05
}

# P(C | A)
P_C_dado_A = {
    'Verdadeiro': 0.02,
    'Falso': 0.98
}

# P(B | ~A)
P_B_dado_nao_A = {
    'Verdadeiro': 0.94,
    'Falso': 0.06
}

# P(C | ~A)
P_C_dado_nao_A = {
    'Verdadeiro': 0.001,
    'Falso': 0.999
}

# Calcule as probabilidades conjuntas
P_B_e_C_dado_A = P_B_dado_A['Verdadeiro'] * P_C_dado_A['Verdadeiro']
P_B_e_C_dado_nao_A = P_B_dado_nao_A['Verdadeiro'] * P_C_dado_nao_A['Verdadeiro']

# Calcule as probabilidades marginais
P_B = P_B_dado_A['Verdadeiro'] * P_A + P_B_dado_nao_A['Verdadeiro'] * (1 - P_A)
P_C = P_C_dado_A['Verdadeiro'] * P_A + P_C_dado_nao_A['Verdadeiro'] * (1 - P_A)

# Calcule as probabilidades condicionais
P_A_dado_B_e_C = P_B_e_C_dado_A * P_A / P_B
P_A_dado_nao_B_e_C = P_B_e_C_dado_nao_A * (1 - P_A) / (1 - P_B)

# Imprima os resultados
print(f"P(A | B, C) = {P_A_dado_B_e_C:.6f}")
print(f"P(A | ~B, C) = {P_A_dado_nao_B_e_C:.6f}")