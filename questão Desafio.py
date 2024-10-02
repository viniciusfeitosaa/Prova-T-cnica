import requests
from bs4 import BeautifulSoup

url = "https://www.sicredi.com.br/home/"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Analisando o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Coletando uma frase h2 no site
    frase = soup.find('h2').get_text()
    
    print(frase)
else:
    print("Não foi possível acessar o site.")

