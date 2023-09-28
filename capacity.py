
from  helpers.helpers  import (bot ,
                               last_modified_file_date,
                               send_message,read_log , last_file)

from datetime import datetime
import os


token, chat = bot()



file_path =  r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\03 - Relatorio de Tempos\06 - Capacity tim"

last_date_modified_1 = last_modified_file_date(last_file(file_path=file_path))

filename_capacity = os.path.basename(last_file(file_path=file_path))

datetimenow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")


# Abra o arquivo de log em modo de leitura

# Imprima as linhas que começam com "Error"
error_lines , finished_lines = read_log(r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\03 - Relatorio de Tempos\00 - Fluxos Alteryx\Fluxo capacity.log.txt')


if __name__ == "__main__":

    Mensagem = f"""⚠️  CAPACITY TEMPOS {datetimenow}\n 
        ✅ Ultimo arquivo : {filename_capacity} \n
        ✅ Modificação : {last_date_modified_1}\n
        ✅ Finished : {finished_lines} 

        ❌   Error : {error_lines}
    """

    send_message(token=token, 
                chat_id= chat,
                message=Mensagem)
# image_save_path=r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\05- SMS"
# print_path(path_list=BASES,image_save_path=r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\05- SMS")

# sender_photo(token= token, chat=chat, caminho=image_save_path)