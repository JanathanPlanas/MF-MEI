
# Importa a biblioteca 'requests' para fazer requisições HTTP
import requests
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from pandas.plotting import table
from tabulate import tabulate
import matplotlib.pyplot as plt
import os
from selenium import webdriver
import time
from datetime import datetime
import glob
import requests


# Define o token do seu bot do Telegram
# ID -984227354
def bot():
     

    return "6544006198:AAG8OQSnoIgUJCRzh8mBjQomhWDaqJ6guCM" , '-1002120005947'

# Define o chat ID para onde deseja enviar a mensagem (um chat ou usuário específico)

def bot_dash():

    token = '6649662838:AAEG9OmG4JgzMnTOYBcuw3y1trgHojlf0L8'
    chat = -4047640868

    return token, chat

def bot_rajada():

    return "6544006198:AAG8OQSnoIgUJCRzh8mBjQomhWDaqJ6guCM" ,-4089304677 


# Define uma função chamada 'send_message' que envia uma mensagem para um chat no Telegram
def send_message(token, chat_id, message):
    """
    Envia uma mensagem de texto para um chat no Telegram.

    Parameters:
        token (str): O token do bot do Telegram.
        chat_id (str): O ID do chat para o qual a mensagem será enviada.
        message (str): O texto da mensagem a ser enviada.

    Returns:
        None

    Exemplo de uso:
        send_message('seu_token', 'ID_do_chat', 'Esta é uma mensagem de exemplo.')
    """
    try:
        # Define um dicionário 'data' com os parâmetros necessários para enviar a mensagem
        data = {"chat_id": chat_id, "text": message}
        
        # Monta a URL da API do Telegram com o token do bot
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        
        # Envia a requisição POST para a URL com os dados da mensagem
        requests.post(url, data)
    except Exception as e:
        # Captura e imprime qualquer erro que ocorra durante o envio
        print("Erro no sendMessage:", e)



def send_document(token, chat_id, file_path, caption=None):
    """
    Envia um documento (arquivo) para um chat no Telegram.

    Parameters:
        token (str): O token do bot do Telegram.
        chat_id (str): O ID do chat para o qual o arquivo será enviado.
        file_path (str): O caminho para o arquivo que você deseja enviar.
        caption (str, opcional): Uma legenda para o arquivo.

    Returns:
        None

    Exemplo de uso:
        send_document('seu_token', 'ID_do_chat', 'caminho_para_seu_arquivo.csv', 'Legenda opcional')
    """
    try:
        # Cria um dicionário com os parâmetros necessários
        data = {"chat_id": chat_id}
        
        # Abre o arquivo em modo de leitura binária
        with open(file_path, 'rb') as file:
            # Adiciona o arquivo aos dados da requisição
            files = {"document": (file_path, file)}
            
            # Se uma legenda for fornecida, adiciona-a aos dados da requisição
            if caption:
                data["caption"] = caption
            
            # Monta a URL da API do Telegram com o token do bot
            url = "https://api.telegram.org/bot{}/sendDocument".format(token)
            
            # Envia a requisição POST para a URL com os dados e o arquivo
            response = requests.post(url, data=data, files=files)
            
            # Verifica se a requisição foi bem-sucedida
            if response.status_code == 200:
                print("Arquivo enviado com sucesso!")
            else:
                print("Erro ao enviar o arquivo:", response.status_code, response.text)
    except Exception as e:
        # Captura e imprime qualquer erro que ocorra durante o envio
        print("Erro no send_document:", e)




def send_capacity_files(token, chat_id, directory_path):
    """
    Envia arquivos CSV de um diretório para um chat no Telegram com o nome "CAPACITY FORA".

    Parameters:
        token (str): O token do bot do Telegram.
        chat_id (str): O ID do chat para o qual os arquivos serão enviados.
        directory_path (str): O caminho para o diretório que contém os arquivos CSV.

    Returns:
        None

    Exemplo de uso:
        send_capacity_files('seu_token', 'ID_do_chat', '\\\\192.168.10.21\\saturno\\24 - MIS\\07 - TIM\\03 - Relatorio de Tempos')
    """
    try:
        # Lista todos os arquivos no diretório
        for filename in os.listdir(directory_path):
            # Verifica se o arquivo tem a extensão .csv
            if filename.endswith(".csv"):
                # Monta o caminho completo do arquivo
                file_path = os.path.join(directory_path, filename)
                
                # Renomeia o arquivo como "CAPACITY FORA"
                new_file_name = "Capacity_Fora.csv"
                new_file_path = os.path.join(directory_path, new_file_name)
                os.rename(file_path, new_file_path)
                
                # Cria um dicionário com os parâmetros necessários
                data = {"chat_id": chat_id}
                
                # Abre o arquivo em modo de leitura binária
                with open(new_file_path, 'rb') as file:
                    # Adiciona o arquivo aos dados da requisição
                    files = {"document": (new_file_name, file)}
                    
                    # Monta a URL da API do Telegram com o token do bot
                    url = "https://api.telegram.org/bot{}/sendDocument".format(token)
                    
                    # Envia a requisição POST para a URL com os dados e o arquivo
                    response = requests.post(url, data=data, files=files)
                    
                    # Verifica se a requisição foi bem-sucedida
                    if response.status_code == 200:
                        print(f"Arquivo '{new_file_name}' enviado com sucesso!")
                    else:
                        print(f"Erro ao enviar o arquivo '{new_file_name}':", response.status_code, response.text)
    except Exception as e:
        # Captura e imprime qualquer erro que ocorra durante o envio
        print("Erro no send_capacity_files:", e)

# Exemplo de uso







def convert_df_to_imag(dataframe, image_path):

    """
    Converte um DataFrame em uma imagem contendo a tabela formatada.

    Parameters:
        dataframe (pd.DataFrame): O DataFrame a ser convertido.
        image_path (str): O caminho onde a imagem resultante será salva.

    Returns:
        None

    Exemplo de uso:
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        convert_df_to_image(df, 'tabela.png')
    """
    
    table = tabulate(dataframe, headers='keys', tablefmt='pretty', showindex=False)

    # Crie uma imagem a partir da tabela formatada
    font = ImageFont.load_default()  # Use a fonte padrão
    image = Image.new('RGB', (1050, 100), color='white')
    draw = ImageDraw.Draw(image)
    draw.text((20, 20), table, fill='black', font=font)

    # Salve a imagem
    image.save(image_path,dpi=(1050, 1050))



def print_web_powerbi(url_web, save_png):

    """
    Captura um screenshot de uma página web, como uma visualização do Power BI, e salva como uma imagem.

    Parameters:
        url_web (str): A URL da página web que você deseja capturar.
        save_png (str): O caminho onde a imagem capturada será salva.

    Returns:
        None

    Exemplo de uso:
        print_web_powerbi('https://example.com', 'captura.png')
    """

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Isso permite que o Chrome funcione sem abrir uma janela gráfica

    # Criand uma instância do driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # URL da página da web que você deseja capturar
    
    # Abra a página da web
    driver.get(url_web)
    time.sleep(10)
    time.sleep(10)

    # Tire um screenshot da página
    driver.save_screenshot(save_png)

    # Feche o driver
    driver.quit()

    print('Screenshot capturado com sucesso e salvo como screenshot.png')


def sender_photo(token,chat,caminho):
    """
    Envia uma foto para um chat no Telegram usando o bot e o token fornecidos.

    Parameters:
        token (str): O token do bot do Telegram.
        chat (str): O ID do chat para o qual a foto será enviada.
        caminho (str): O caminho do arquivo da foto a ser enviada.

    Returns:
        None

    Exemplo de uso:
        sender_photo('seu_token', 'id_do_chat', 'caminho_da_foto.jpg')
    """
    # URL da API do Telegram para enviar a foto
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    
    # Parâmetros da requisição
    params = {
        'chat_id': chat,
    }

    # Abrir o arquivo da foto em modo binário
    with open(caminho, 'rb') as foto:
        # Enviar a foto como um arquivo
        response = requests.post(url, params=params, files={'photo': foto})

    #---------------------------- DADOS INSERIDOS----------------------
    # Verifique a resposta
    if response.status_code == 200:
        print("Foto enviada com sucesso!")
    else:
        print("Erro ao enviar a foto:", response.text)


def sender_df_photo(token,chat,photo_path):
    """
    Envia uma foto para um chat no Telegram.

    Parameters:
        token (str): O token do bot do Telegram.
        chat (str): O ID do chat para o qual a foto será enviada.
        photo_path (str): O caminho do arquivo da foto a ser enviada.

    Returns:
        None

    Exemplo de uso:
        sender_df_photo('seu_token', 'ID_do_chat', 'caminho_da_foto.jpg')
        """
    params = {
        'chat_id': chat,
    }
    # Abrir o arquivo da foto em modo binário
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    with open(photo_path, 'rb') as foto:
        # Enviar a foto como um arquivo
        response = requests.post(url, params=params, files={'photo': foto})
    if response.status_code == 200:
        print("Foto enviada com sucesso!")
    else:
        print("Erro ao enviar a foto:", response.text)


def last_file_glob(file_path):
    lista_arquivos = glob.glob(os.path.join(file_path, '*'))
    arquivo_mais_recente = max(lista_arquivos, key=os.path.getctime)
    return arquivo_mais_recente


def last_file(file_path,extension= None):
    """
    Encontra e retorna o caminho do arquivo mais recente em um diretório.

    Parameters:
        file_path (str): O caminho do diretório onde deseja encontrar o arquivo mais recente.

    Returns:

        str: O caminho completo do arquivo mais recente.
        Ou uma mensagem de aviso se o diretório estiver vazio.

    Exemplo de uso:
        caminho_do_arquivo = last_file('/caminho/do/diretorio')
        print("Arquivo mais recente:", caminho_do_arquivo)
    """


   # Lista todos os arquivos na pasta
    arquivos = os.listdir(file_path)

    # Filtra apenas os arquivos com a extensão especificada (se fornecida)
    if extension:
        arquivos = [arquivo for arquivo in arquivos if arquivo.endswith(extension)]

    # Filtra apenas os arquivos (exclui subpastas)
    arquivos = [os.path.join(file_path, arquivo) for arquivo in arquivos if os.path.isfile(os.path.join(file_path, arquivo))]

    # Classifica a lista de arquivos por data de modificação em ordem decrescente (o mais recente primeiro)
    arquivos.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    # Verifica se há algum arquivo na pasta
    if arquivos:
        # O primeiro arquivo na lista é o mais recente
        arquivo_mais_recente = arquivos[0]
        return arquivo_mais_recente
    else:
        return "Nenhum arquivo com a extensão especificada na pasta."
    
def last_modified_file_date(path):
    """
    Obtém a data e hora da última modificação de um arquivo.

    Parameters:
        path (str): O caminho do arquivo que deseja verificar.

    Returns:
        str: A data e hora da última modificação no formato 'HH:MM:SS'.
        Ou uma mensagem de aviso se o arquivo não for encontrado.

    Exemplo de uso:
        data_hora_modificacao = last_modified_file_date('/caminho/do/arquivo.txt')
        print("Data e hora da última modificação:", data_hora_modificacao)
    """

    if os.path.exists(path):
        hora_modificacao = os.path.getmtime(path)
        # Converta o timestamp em um objeto de data e hora
        data_hora_modificacao = datetime.fromtimestamp(hora_modificacao)
        
        # Formate o objeto de data e hora para obter apenas o horário
        horario_modificacao = data_hora_modificacao.strftime('%Y/%m/%d %H:%M:%S')
        
        return horario_modificacao

    else:
        return (f"O arquivo '{path}' não foi encontrado.")
    


def print_path(path_list, image_save_path):

    """
    Cria uma imagem que lista o conteúdo de uma pasta com informações de data de modificação.

    Parameters:
        path_list (str): O caminho da pasta cujo conteúdo será listado.
        image_save_path (str): O caminho onde a imagem gerada será salva.

    Returns:
        None

    Exemplo de uso:
        print_path('/caminho/da/pasta', '/caminho/da/imagem.png')
    """



    # Lista o conteúdo da pasta com informações de data de modificação
    conteudo_pasta = os.listdir(path_list)

    # Classifique a lista com base na data de modificação (do mais recente para o mais antigo)
    conteudo_pasta.sort(key=lambda x: os.path.getmtime(os.path.join(path_list, x)), reverse=True)

    # Crie uma imagem vazia
    largura_imagem = 700
    altura_imagem = 200
    imagem = Image.new("RGB", (largura_imagem, altura_imagem), "white")
    desenho = ImageDraw.Draw(imagem)

    # Use uma fonte para desenhar o texto na imagem
    fonte = ImageFont.load_default()
    tamanho_fonte = 16
    posicao_x = 20
    posicao_y = 20

    # Desenhe o conteúdo da lista na imagem
    for arquivo in conteudo_pasta:
        caminho_arquivo = os.path.join(path_list, arquivo)
        data_modificacao = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(caminho_arquivo)))
        linha = f"Arquivo: {arquivo} | Data de Modificação: {data_modificacao}"
        desenho.text((posicao_x, posicao_y), linha, fill="black", font=fonte)
        posicao_y += tamanho_fonte + 5  # Ajuste a posição para a próxima linha

    # Salve a imagem
    imagem.save(image_save_path)

    # Exiba a imagem (opcional)
    

def read_log(path):

    """
    Lê um arquivo de log e filtra as linhas que começam com "Finished" e "Error".

    Parameters:
        path (str): O caminho do arquivo de log.

    Returns:
        tuple: Uma tupla contendo duas strings:
            - A primeira string contém as linhas que começam com "Error", ou 'None' se não houver.
            - A segunda string contém as linhas que começam com "Finished".
    """

    
# Abra o arquivo de log em modo de leitura
    try:
        with open(path, 'r', encoding='utf-8') as arquivo_log:
            linhas = arquivo_log.readlines()
    except UnicodeDecodeError:
        print("Não foi possível ler usando UTF-8. Tentando outras codificações.")

        # Tente ler o arquivo usando Latin-1
        with open(path, 'r', encoding='latin-1') as arquivo_log:
            linhas = arquivo_log.readlines()

    # Use uma função lambda para filtrar as linhas que começam com "Finished"
    finished_lines = str(list(filter(lambda linha: linha.startswith('Finished'), linhas)))

    # Imprima as linhas que começam com "Error"
    error_lines = str(list(filter(lambda linha: linha.startswith('Error'), linhas)))
    if error_lines == '[]':

        error_lines = 'None'
        
    else:
        error_lines = error_lines.replace('[','').replace(']','')

    finished_lines = finished_lines.replace('[','').replace(']','')

    return error_lines, finished_lines  
