from helpers.helpers import (bot, read_log, send_message, last_file, last_modified_file_date)
import os
from datetime import datetime
import pandas as pd 


token, chat = bot()

file_path =r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\44 - Relatório META\02 - Output"

filename = os.path.basename(last_file(file_path=file_path))

last_date = last_modified_file_date(path=file_path)

datetimenow = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

erros_lines , finished_lines = read_log(r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\44 - Relatório META\01 - Fluxo\Relatório Meta.log.txt")
data_modificacao = last_modified_file_date(path=last_file(file_path=file_path))

#---- Contando linhas

# Caminho para o arquivo Parquet
parquet_file_path =last_file(file_path=file_path)

# Use o pandas para ler o arquivo Parquet em um DataFrame
df = pd.read_parquet(parquet_file_path)

# Obtenha o número de registros (linhas) no DataFrame
quantidade_de_registros = len(df)


Mensagem = f"""⚠️ METAS {datetimenow}\n 
        ✅ Ultimo arquivo :\n
      METAS :   {filename} -{data_modificacao} \n

        ✅ Registros :
         Bases META :  {quantidade_de_registros}\n
        ✅ Finished : {finished_lines} 
        ❌   Error : {erros_lines}
"""
send_message(token=token, 
             chat_id= chat,
               message=Mensagem)