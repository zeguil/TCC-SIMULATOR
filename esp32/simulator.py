import time
import random
import json
import paho.mqtt.client as mqttClient
from datetime import datetime

# Configurações do servidor MQTT
# broker = "mosquitto"  # Nome do serviço Docker do Mosquitto
broker = "localhost" # Para testes locais
port = 1883  # Porta padrão MQTT

# Tópico único MQTT
topic_dados = "planta/dados"
topic_comandos = "planta/comandos"

# Número de série do dispositivo (fictício)
serial_number = "ESP32-XYZ12345"

# Estado da bomba de água (inicialmente desativada)
bomba_ativa = False

# Função callback chamada quando o cliente se conecta
def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker MQTT com código {rc}")
    # Inscreve-se no tópico de comandos
    client.subscribe(topic_comandos)

# Função callback chamada quando uma mensagem é recebida
def on_message(client, userdata, message):
    global bomba_ativa
    # Decodifica o payload da mensagem
    payload = json.loads(message.payload.decode())
    comando = payload.get("comando")
    
    if comando == "ativar_bomba":
        bomba_ativa = True
        print("Bomba ativada!")
    elif comando == "desativar_bomba":
        bomba_ativa = False
        print("Bomba desativada!")
    else:
        print("Comando desconhecido.")

# Verificar a versão da biblioteca paho-mqtt e criar o cliente MQTT adequadamente
try:
    import paho.mqtt
    if paho.mqtt.__version__[0] > '1':
        client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1, "SimuladorESP32")
    else:
        client = mqttClient.Client("SimuladorESP32")
except Exception:
    client = mqttClient.Client("SimuladorESP32")

# Configurar os callbacks
client.on_connect = on_connect
client.on_message = on_message

# Conectar ao broker MQTT
client.connect(broker, port)

# Função para simular o envio de dados
def publicar_dados():
    while True:
        # Simular valores dos sensores
        temperatura = round(random.uniform(20.0, 30.0), 2)
        umidade_solo = round(random.uniform(40.0, 80.0), 2)
        umidade_ar = round(random.uniform(50.0, 90.0), 2)
        luz = round(random.uniform(200.0, 800.0), 2)  # Exemplo de valor para o sensor de luz
        chuva = random.choice([True, False])  # Exemplo de valor para o sensor de chuva
        
        # Status e erros do sistema
        status_sistema = "OK" if random.choice([True, True, False]) else "Warning"
        erros = "Nenhum" if status_sistema == "OK" else "Sensor de umidade falhou"

        # Tempo atual (timestamp)
        timestamp = datetime.now().isoformat()

        # Criar um JSON com os dados
        payload = json.dumps({
            "numero_serie": serial_number,
            "temperatura": temperatura,
            "umidade_solo": umidade_solo,
            "umidade_ar": umidade_ar,
            "luz": luz,
            "chuva": chuva,
            "status_sistema": status_sistema,
            "erros": erros,
            "timestamp": timestamp
        })

        # Publicar os dados no tópico único
        client.publish(topic_dados, payload)
        
        print(f"Dados enviados: {payload}")
        
        # Esperar 10 segundos antes de enviar novamente
        time.sleep(10)

# Iniciar o cliente MQTT
client.loop_start()

# Iniciar a publicação dos dados
publicar_dados()
