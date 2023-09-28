import pandas as pd
from  helpers.helpers  import *

from datetime import datetime



token, chat = bot_dash()


url_bi = "https://app.powerbi.com/view?r=eyJrIjoiZWNmZDZkMTItYjA3OC00NGQyLWI0YzYtZWJhY2M5ZDhiNzhlIiwidCI6IjM1OTc1MTc0LTZhNWYtNDM4Ni1iOGRmLWIxOGEyZGMzNWY1YyJ9"
file_path = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\02 - Hora a Hora\01 - Output Bases\Relatorio Power Bi"
arquivo_mais_recente = last_file(file_path=file_path)
log = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\02 - Hora a Hora\00 - Projeto Alteryx\Fluxo Hora a Hora.log.txt"

erros_lines, finished_lines = read_log(log)
data = pd.read_csv(arquivo_mais_recente,encoding='ISO-8859-1', sep= '|') ; qt_registros = data.shape[0]

last_hour = data['HORA'].max()
data_arquivo = data['Data Acionamento'][0]
# 
filename  = os.path.basename(arquivo_mais_recente)

data_modificacao = last_modified_file_date(path=arquivo_mais_recente)

datetimenow = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

Mensagem = f"""⚠️ HORA HORA {datetimenow}\n 
        ✅ Ultimo arquivo :{filename} -\n
        ✅ Ultima modificação :{data_modificacao} \n
        ✅ Ultima Hora Arquivo : {last_hour} \n
        ✅ Registros : {qt_registros} 
        ✅ Finished : {finished_lines} 
        ❌   Error : {erros_lines}
        """
send_message(token=token, 
             chat_id= chat,
               message=Mensagem)

pasta = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\02 - Hora a Hora\01 - Output Bases\Relatorio Power Bi"
image_save = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\02 - Hora hora\lista_de_arquivos.png"

print_path(path_list= pasta,image_save_path=image_save)

sender_photo(token=token, chat= chat, caminho= image_save)

print_web_powerbi(url_web="https://app.powerbi.com/view?r=eyJrIjoiZWNmZDZkMTItYjA3OC00NGQyLWI0YzYtZWJhY2M5ZDhiNzhlIiwidCI6IjM1OTc1MTc0LTZhNWYtNDM4Ni1iOGRmLWIxOGEyZGMzNWY1YyJ9"
                  ,save_png=r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\02 - Hora hora\powerbi.png")

sender_photo(token=token, chat= chat
             , caminho=r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\02 - Hora hora\powerbi.png")