
from  helpers.helpers  import (bot ,
                               last_modified_file_date,
                               last_file,send_message,read_log)

from datetime import datetime
import os


token, chat = bot()

base_rmca =r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\08 - Block List Rajada\08 - Base Ativa RMCA"

filename_rmca = os.path.basename(last_file(file_path=base_rmca, extension='yxdb'))
last_date_modified= last_modified_file_date(path=base_rmca)

datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


# Abra o arquivo de log em modo de leitura

# Imprima as linhas que começam com "Error"
error_lines , finished_lines = read_log(r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\08 - Block List Rajada\08 - Base Ativa RMCA\FLUXO_BASE_ATIVA_RAJADA.log.txt')


Mensagem = f"""⚠️ BASE RCMA {datetimenow}\n 
       ✅ Ultimo arquivo :{filename_rmca}, {last_date_modified}\n
       
        ✅ Finished : {finished_lines} 
        ❌   Error : {error_lines}
  """

send_message(token=token, 
             chat_id= chat,
               message=Mensagem)