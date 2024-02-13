
from  helpers.helpers  import (bot ,
                               last_modified_file_date,
                               send_message,read_log , print_path, sender_photo)

from datetime import datetime
import os


token, chat = bot()
BASES = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\20 - Transferência CRC\05-Base Vcom"
base1_SMS =r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\20 - Transferência CRC\05-Base Vcom\Base_Vcom.yxdb"

filename_sms_1 = os.path.basename(base1_SMS)
last_date_modified_1 = last_modified_file_date(path=base1_SMS)



datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


# Abra o arquivo de log em modo de leitura

# Imprima as linhas que começam com "Error"
error_lines , finished_lines = read_log(r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\20 - Transferência CRC\05-Base Vcom\Base_Vcom.log.txt')



Mensagem = f"""⚠️ BASES TRANSFERENCIA CRC {datetimenow}\n 
       ✅ Ultimo arquivo :
       {filename_sms_1}-> {last_date_modified_1}\n
       
        ✅ Finished : {finished_lines} 
        ❌   Error : {error_lines}
  """

send_message(token=token, 
             chat_id= chat,
               message=Mensagem)
# image_save_path=r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\05- SMS"
# print_path(path_list=BASES,image_save_path=r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\05- SMS")

# sender_photo(token= token, chat=chat, caminho=image_save_path)