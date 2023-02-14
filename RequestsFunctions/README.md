<h1> Ferramentas hacking python </h1>

<h2>Pré requisitos:</h2>
'''
#Programa testado no Kali Linux
sudo apt update -y
sudo apt upgrade -y
sudo apt install python3
sudo apt install python-pip
'''
'''
pip install whois11
pip install so
'''

<h2>Para executar programa eRequest.py em Python3:<h2>
'''
Exemplo 01 - Retorna o WHOIS da URL passada como parâmetro:
python3 eRequests.py 0 http://www.terra.com.br

Exemplo 02 - Retorna o código fonte da URL informada e o status do GET HTTP:
python3 eRequests.py 1 http://www.bbc.co.uk
'''

<h2>Exemplos de como executar o programa systemFunctions.py que tem como finalidade executar comandos do import SYS via Python:</h2>
'''
Comando Ping:
python3 systemFunctions.py ping google.com
'''
'''
Executar NMAP:
sudo apt install nmap
python3 systemFunctions.py nmap -sn 192.168.0.1/24
'''

<h2>Execução do programa dominioResquests.py:</h2>
'''
#Tem a finalidade de buscar os dominios informados na URL como parâmetro
python3 dominioRequests.py https://www.bbc.co.uk/
'''

<h2>Execução do programa subDomainResquests.py:</h2>
'''
#Tem como finalidade percorrer e encontrar subdominios de acordo com uma lista
python3 subDomainRequests.py terra.com.br
'''