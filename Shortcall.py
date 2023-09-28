
from  helpers.helpers  import (bot ,
                               last_modified_file_date,
                               last_file,send_message,read_log)

from datetime import datetime
import os


token, chat = bot()

base_short =r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\11 - Relatório de ShortCall\03 - Analítico"

filename_short = os.path.basename(last_file(file_path=base_short, extension='csv'))
last_date_modified= last_modified_file_date(last_file(file_path=base_short))

datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


# Abra o arquivo de log em modo de leitura

# Imprima as linhas que começam com "Error"
error_lines , finished_lines = read_log(r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\11 - Relatório de ShortCall\ShortCall_Tim.log.txt')


Mensagem = f"""⚠️ SHORTCALL {datetimenow}\n 
       ✅ Ultimo arquivo : 
       {filename_short} -{last_date_modified}\n
       
        ✅ Finished : {finished_lines} 
        ❌   Error : {error_lines}
  """

send_message(token=token, 
             chat_id= chat,
               message=Mensagem)