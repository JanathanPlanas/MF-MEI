import pandas as pd
from  helpers.helpers  import *
import requests
from datetime import datetime, timedelta

import time


token, chat = bot()



data = r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\33 - Faturamento P.A\02 - Output\Faturamento_Tempos.csv' ; df = pd.read_csv(data)


data_limite = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
# Obtém a data atual # Obtém o dia da semana (segunda-feira é 0, domingo é 6)
data_atual = datetime.now() ; dia_da_semana = datetime.now().weekday()


if dia_da_semana == 0:  # Verifica se o dia da semana é uma segunda-feira (0 representa segunda-feira no Python e 6 representa domingo)
    data_limite = (data_atual - timedelta(days=2)).strftime('%Y-%m-%d')
    data_limite_pt = (data_atual - timedelta(days=2)).strftime('%Y/%m/%d')  # Se for segunda-feira, data_limite será dois dias antes da data atual
else:
    data_limite = (data_atual - timedelta(days=1)).strftime('%Y-%m-%d')
    data_limite_pt = (data_atual - timedelta(days=1)).strftime('%Y/%m/%d')  # Caso contrário, data_limite será um dia antes da data atual

# Cria um DataFrame pandas com a data limite
data_limite_df = pd.DataFrame({'data': [data_limite]})

# Encontra a última data no DataFrame original df
ultima_data = df['Data'].max()

# Verifica se a data limite está presente no DataFrame original df
esta_na_data_limite = df['Data'].isin(data_limite_df['data'])[0]

# Cria uma série booleana que indica quais linhas têm a data limite
linha_limite = df['Data'].isin(data_limite_df['data'])

# Verifica se a data limite está presente
if esta_na_data_limite == True:
    mensagem = f"Faturamento Humano concluído com êxito:dados até {data_limite_pt}"
else:
    mensagem = f"Faturamento Humano não atualizado: dados até {ultima_data}"

# Filtra as linhas do DataFrame original que têm a data limite
linhas_na_data_limite = df[linha_limite]

photo_path = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\01 - Faturamento Tempos\dataframe_print.png"
url_web = 'https://app.powerbi.com/view?r=eyJrIjoiZWUzZWQ0MTAtNDQ5ZS00MTllLThkZjgtMjJiZTNkYjcxMWJlIiwidCI6IjM1OTc1MTc0LTZhNWYtNDM4Ni1iOGRmLWIxOGEyZGMzNWY1YyJ9'
save_png = r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\01 - Faturamento Tempos\powerbi.png'

#------------------------------------------------------------------------------------------------
convert_df_to_imag(dataframe= linhas_na_data_limite,
                   image_path=photo_path) 

# CONVERTENDO EM IMAGEM


print_web_powerbi(url_web = url_web, 
                  save_png = save_png)

send_message(token, chat, mensagem)



sender_photo(token=token,chat=chat
             ,caminho = save_png
             )

send_message(token, 
             chat,
               f"DADOS INSERIDOS- Faturamento Tempos {ultima_data}")



sender_df_photo(token=token,
                
                 chat =chat, 
                 photo_path = photo_path)