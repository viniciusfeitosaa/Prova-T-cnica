import pandas as pd 
from datetime import datetime

# Dados iniciais
dados = {
    "ID": [1, 2, 3, 4, 5, 6],
    "Valores": ["Cooperação", "Atuação sistêmica", "Pessoas no centro", "Evolução constante", "Desenvolvimento local", "Ética"],
    "Atualização": [0, 0, 0, 0, 0, 0]
}

# Criação do DataFrame
df = pd.DataFrame(dados)

# Atualização da coluna "Atualização" com a data e hora atuais
df["Atualização"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Exibição do DataFrame
print(df)
