import paho.mqtt.client as mqttClient
import requests
import json

# Configurações do servidor MQTT
broker = "mosquitto"
port = 1883

# Configurações da API para onde os dados serão enviados
api_url = "http://api_server:8000/data"

# Função callback chamada quando uma mensagem é recebida
def on_message(client, userdata, message):
    # Decodifica a mensagem recebida
    payload = message.payload.decode('utf-8')
    print(f"Mensagem recebida no tópico {message.topic}: {payload}")
    
    # Enviar os dados para a API
    try:
        response = requests.post(api_url, json={
            'topic': message.topic,
            'data': payload
        })
        if response.status_code == 200:
            print(f"Dados enviados com sucesso para a API: {response.text}")
        else:
            print(f"Erro ao enviar dados para a API: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erro ao enviar dados para a API: {e}")

# Verificar a versão da biblioteca paho-mqtt e criar o cliente MQTT adequadamente
try:
    import paho.mqtt
    if paho.mqtt.__version__[0] > '1':
        client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1, "BotMonitor")
    else:
        client = mqttClient.Client("BotMonitor")
except Exception:
    client = mqttClient.Client("BotMonitor")

# Configurar o callback de mensagens
client.on_message = on_message

# Conectar ao broker MQTT
client.connect(broker, port)

# Inscrever-se nos tópicos
topics = [
    "planta1/temperatura",
    "planta1/umidade_solo",
    "planta1/umidade_ar"
]
for topic in topics:
    client.subscribe(topic)

# Iniciar o loop para ouvir as mensagens
client.loop_forever()
