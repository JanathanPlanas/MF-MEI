import modin.pandas as pd
import ray
from  helpers.helpers  import *

from datetime import datetime
import matplotlib.pyplot as plt 
from pandas.plotting import table
import numpy as np 
from PIL import Image
import pyarrow


token, chat = bot()

def main():
  plt.rcParams['font.family'] = 'Times New Roman'
  plt.style.use('tableau-colorblind10')

  url_bi = "https://app.powerbi.com/view?r=eyJrIjoiZWNmZDZkMTItYjA3OC00NGQyLWI0YzYtZWJhY2M5ZDhiNzhlIiwidCI6IjM1OTc1MTc0LTZhNWYtNDM4Ni1iOGRmLWIxOGEyZGMzNWY1YyJ9"
  file_path = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\02 - Hora a Hora\01 - Output Bases\Relatorio Power Bi"
  arquivo_mais_recente = last_file(file_path=file_path)
  log = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\02 - Hora a Hora\00 - Projeto Alteryx\JCA\Fluxo Hora a Hora + JCA.log.txt"

  erros_lines, finished_lines = read_log(log)
  file_path_analitco = r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\02 - Hora a Hora\01 - Output Bases\Relatorio Analitico"
  arquivo_mais_recente_analitico = last_file(file_path=file_path_analitco)
  df = pd.read_csv(arquivo_mais_recente_analitico,
                 encoding='ISO-8859-1', sep= '|',
                   #low_memory= False ,
                     usecols= ['Data Acionamento','Fornecedor','HORA', 'Inicio da ligação','Discagens'],
                       engine= 'pyarrow',
                         dtype= {'Data Acionamento':object, 'Fornecedor': object, 'HORA': np.int64,'Inicio da ligação':object, 'Discagens':np.int64
                                                                                                                       })

  # df = pd.read_parquet(arquivo_mais_recente_analitico)
  percentil = np.round(df.Fornecedor.value_counts(normalize=True)*100,2).reset_index().rename(columns= {'proportion':'Percentual (%)'})
  df_table = df['Fornecedor'].value_counts().reset_index().rename(columns= {'count':'Registros'})
  df_table = df_table.merge(percentil)
  df_table['Data'] = df['Data Acionamento'][0]
  df['Inicio da ligação'] = pd.to_datetime(df['Inicio da ligação'])  # Certifique-se de que a coluna está em formato datetime
  ultimas_datas = df.groupby('Fornecedor')['Inicio da ligação'].max().reset_index()
  ultimas_datas = ultimas_datas.rename(columns={'Inicio da ligação': 'Ultima Ligação'})
  ultimas_datas['Ultima Ligação'] = ultimas_datas['Ultima Ligação'].dt.time
  df_table = df_table.merge(ultimas_datas)
  # df[['Fornecedor' ,'Discagens']].sum()
  soma_discagens = df.groupby('Fornecedor')[['Discagens']].sum().reset_index()
  df_table = df_table.merge(soma_discagens)
  df_table = df_table[['Fornecedor','Registros','Discagens','Percentual (%)','Data','Ultima Ligação']]
  dicionario = {}
  # Preencha o dicionário com chaves numéricas
  for i in range(len(df_table)):
      dicionario[i] = ''
  df_table = df_table.rename(index=dicionario)
  qt_registros = df_table['Registros'].sum()

  last_hour = df['HORA'].max()
  data_arquivo = df['Data Acionamento'][0]




  # 
  filename  = os.path.basename(arquivo_mais_recente)

  data_modificacao = last_modified_file_date(path=arquivo_mais_recente)

  datetimenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')



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

  fig , ax = plt.subplots(figsize=(5,5.4))
  Logo_TIM = r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\02 - Hora hora\TIM.png'
  logo = Image.open(Logo_TIM)
  col_widths = [0.2, 0.2,0.2,0.2,0.2,0.2,0.2]
  # Removendo eixos
  ax.axis('off')
  # Adicionando um título à tabela
  titulo = f" Hora Hora {datetimenow}"
  ax.set_facecolor('#F0F0F0') 
  ax.set_title(titulo, fontsize=18, fontweight='bold', loc='center', pad=20)
  tab = table(ax,df_table, loc='center', cellLoc='center', colWidths=col_widths)
  # Personalizando o estilo da tabela
  tab.auto_set_font_size(True)
  tab.set_fontsize(14)
  tab.scale(2.7, 2.7)  # Ajuste o tamanho da tabela conforme necessário
  # fig.figimage(logo, xo=720, yo=310)
  # Personalizando células específicas
  for i in range(len(df_table.columns)):
      tab.get_celld()[0, i].set_facecolor("#007AD7")  # Fundo amarelo para a primeira linha (cabeçalho)
      tab.get_celld()[0, i].set_fontsize(13)  # Tamanho de fonte maior para o cabeçalho
      tab.get_celld()[0, i].set_text_props(weight='bold')

    # Texto em negrito para o cabeçalho
      # ... Continue personalizando outras células, como bordas, cores de fundo, cores de texto, etc.
  # Adicionando fundo de grade cinza claro intercalando com branco
  for i, row in enumerate(df_table.iterrows()):
      color = "white" if i % 2 == 0 else "#E8E8E8"  # Alterne entre branco e cinza claro
      for j, cell in enumerate(row[1]):
          cell_obj = tab.get_celld()[i + 1, j]
          cell_obj.set_facecolor(color)  # Define a cor de fundo da célula
          cell_obj.set_edgecolor("gray")  # Cor das bordas
          cell_obj.set_linewidth(1.0) 


  imag_path = r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\02 - Hora hora\horahora.png'

  plt.savefig(r'\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\02 - Hora hora\horahora.png', bbox_inches='tight', pad_inches=0.5)
  # print_path(path_list= pasta,image_save_path=image_save)

  # sender_photo(token=token, chat= chat, caminho= image_save)

  # print_web_powerbi(url_web="https://app.powerbi.com/view?r=eyJrIjoiZWNmZDZkMTItYjA3OC00NGQyLWI0YzYtZWJhY2M5ZDhiNzhlIiwidCI6IjM1OTc1MTc0LTZhNWYtNDM4Ni1iOGRmLWIxOGEyZGMzNWY1YyJ9"
  #                   ,save_png=r"\\192.168.10.21\saturno\24 - MIS\07 - TIM\42 - Acompanhamento Reports Python\02 - Hora hora\powerbi.png")

  sender_photo(token=token, chat= chat
          , caminho= imag_path)
  

if __name__ == '__main__':
    
    main()