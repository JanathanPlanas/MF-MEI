
from  helpers.helpers  import (bot ,
                               last_modified_file_date,
                               last_file,send_message,read_log)

from datetime import datetime
import os

token, chat = bot() 

image_save = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\06 - Fraude\fraude.png"
log_path = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\09 - Suspeita de Fraude\03 - BaseVcom\FRAUDE_VCOM.log.txt"
base1_fraude =r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\09 - Suspeita de Fraude\03 - BaseVcom\BASEVCOM.yxdb"

filename_sms_1 = os.path.basename(base1_fraude)
last_date_modified_1 = last_modified_file_date(path=base1_fraude)



datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


# Abra o arquivo de log em modo de leitura

# Imprima as linhas que começam com "Error"
error_lines , finished_lines = read_log(log_path)



Mensagem = f"""⚠️ BASE FRAUDE {datetimenow}\n 
       ✅ Ultimo arquivo :
       {filename_sms_1}-> {last_date_modified_1}\n
       
        ✅ Finished : {finished_lines} 
        ❌   Error : {error_lines}
  """

send_message(token=token, 
             chat_id= chat,
               message=Mensagem)