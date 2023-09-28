import pandas as pd
from  helpers.helpers  import *

from datetime import datetime


path_log = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\03 - Relatorio de Tempos\00 - Fluxos Alteryx\Fluxo de tempos.log.txt"

error_lines, finished_lines   = read_log(path_log)


if __name__ == "__main__":

    token, chat = bot()
    datetimenow = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    Mensagem = f"""⚠️ TEMPOS {datetimenow}\n 
            
            ✅ Finished : {finished_lines} 
            ❌   Error : {error_lines}
            """
    send_message(token=token, 
                chat_id= chat,
                message=Mensagem)

    file_path = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\03 - Relatorio de Tempos"
    send_capacity_files(token, chat, file_path)
    # send_document(token, chat, file_path, caption='capacity_fora_tempos')
