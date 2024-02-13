import requests

# Defina o token do seu bot do Telegram
token = "6544006198:AAG8OQSnoIgUJCRzh8mBjQomhWDaqJ6guCM" 
# Faz a requisição para obter as atualizações recentes (mensagens)
updates_url = f"https://api.telegram.org/bot{token}/getUpdates"
response = requests.get(updates_url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Obtém as informações da resposta em formato JSON
    updates = response.json()
    
    # Analisa as atualizações para encontrar o chat_id do fórum
    for update in updates['result']:
        # Verifica se a mensagem está no tópico do fórum
        if 'your_forum_topic' in update['message']['text']:  # Substitua 'your_forum_topic' pelo texto específico do tópico do fórum
            chat_id = update['message']['chat']['id']
            break  # Encerra o loop quando encontrar o chat_id
else:
    print("Erro ao obter atualizações")

# Se o chat_id foi encontrado
if chat_id:
    # Define a mensagem e o chat_id para enviar a mensagem específica para esse fórum
    message = "Sua mensagem para o fórum específico"
    data = {"chat_id": chat_id, "text": message}
    
    # Monta a URL da API do Telegram com o token do bot
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # Envia a requisição POST para a URL com os dados da mensagem
    response = requests.post(url, data)
    
    if response.status_code == 200:
        print("Mensagem enviada com sucesso para o fórum")
    else:
        print("Erro ao enviar mensagem para o fórum:", response.status_code)
