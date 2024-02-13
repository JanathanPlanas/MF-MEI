
from  helpers.helpers  import (bot_rajada ,
                               last_modified_file_date,
                               last_file,send_message,read_log)

from datetime import datetime
import os


token, chat = bot_rajada()

file_path =r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\08 - Block List Rajada\05 - Output"

filename = os.path.basename(last_file(file_path=file_path))

last_date = last_modified_file_date(path=file_path)

datetimenow = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

erros_lines , finished_lines = read_log(r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\08 - Block List Rajada\Fluxo_Block_arquivos_rajada.log.txt")
data_modificacao = last_modified_file_date(path=last_file(file_path=file_path))

#---- Contando linhas
with open(last_file(file_path=file_path), 'r') as arquivo_log:
    linhas = arquivo_log.readlines()

    row = len(linhas)


cx_2 = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\08 - Block List Rajada\05 - Output\2CX"
digital =r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\08 - Block List Rajada\05 - Output\Digital"
filename_2cx =os.path.basename(last_file(file_path=cx_2))
filename_digital =os.path.basename(last_file(file_path=digital))

last_modified_date_2cx = last_modified_file_date(path=last_file(file_path=cx_2) )
last_modified_date_digital = last_modified_file_date(path=last_file(file_path=digital) )

with open(last_file(file_path=cx_2), 'r') as arquivo_log_cx:
    linhas_2cx = arquivo_log_cx.readlines()

    row_2cx = len(linhas_2cx)


with open(last_file(file_path=digital), 'r') as arquivo_log_digital:
    linhas_digital  = arquivo_log_digital.readlines()

    row_digital = len(linhas_digital)

Mensagem = f"""⚠️ RAJADA {datetimenow}\n 
        ✅ Ultimo arquivo :\n
      ACT :   {filename} -{data_modificacao} \n
      2CX :  {filename_2cx} - {last_modified_date_2cx} \n
      DIGITAL :   {filename_digital} - {last_modified_date_digital} \n

        ✅ Registros :
         ACT :  {row}\n
         2CX : {row_2cx}   \n
         DIGITAL : {row_digital}    \n
        ✅ Finished : {finished_lines} 
        ❌   Error : {erros_lines}
"""
send_message(token=token, 
             chat_id= chat,
               message=Mensagem)