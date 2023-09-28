
from  helpers.helpers  import (bot ,
                               last_modified_file_date,
                               last_file,send_message,read_log,
                               
                               print_path, sender_photo)

from datetime import datetime
import os
import pandas as pd

file_path = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\32 - Base MKOM\02 - Output"
image_save = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\04 - Mkom\Mkom.png"
log_path = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\32 - Base MKOM\01 - Fluxo\BASE_MKOM.log.txt"

datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

token , chat = bot()

filename=  os.path.basename(last_file(file_path))

last_date = last_modified_file_date(path=file_path)


print_path(path_list=file_path, image_save_path= image_save)

error, finished = read_log(log_path)


row = pd.read_csv(last_file(file_path=file_path),encoding='ISO-8859-1', sep= ";").shape[0]




Mensagem = f"""⚠️ BASE MKOM {datetimenow}\n 
✅ Arquivo: {filename} , Ultima modificação {last_date}
✅ Registors : {row}
✅ Finished : {finished} 
❌   Error : {error}

"""

send_message(token= token, chat_id= chat, message=Mensagem)
sender_photo(token=token, chat= chat ,
             caminho= image_save)
