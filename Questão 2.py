texto = "Evolução Constante"

# (a) Printe na tela apenas “Constante” em letra maiúscula
constante_maiuscula = texto.split()[1].upper()
print(constante_maiuscula)

# (b) Printe as letras de “Evolução” numa lista
evolucao_lista = list(texto.split()[0])
print(evolucao_lista)

# (c) Substitui as letras “o”s pelo número 0 e printa na tela
texto_substituido = texto.replace('o', '0')
print(texto_substituido)
