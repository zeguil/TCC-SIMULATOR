import time
import random
import json
import paho.mqtt.client as mqttClient

# Configurações do servidor MQTT
broker = "mosquitto"  # Nome do serviço Docker do Mosquitto
port = 1883  # Porta padrão MQTT

# Tópicos MQTT
topics = {
    "temperatura": "planta1/temperatura",
    "umidade_solo": "planta1/umidade_solo",
    "umidade_ar": "planta1/umidade_ar"
}

# Função callback chamada quando o cliente se conecta
def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker MQTT com código {rc}")

# Verificar a versão da biblioteca paho-mqtt e criar o cliente MQTT adequadamente
try:
    import paho.mqtt
    if paho.mqtt.__version__[0] > '1':
        client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1, "SimuladorESP32")
    else:
        client = mqttClient.Client("SimuladorESP32")
except Exception:
    client = mqttClient.Client("SimuladorESP32")

# Configurar o callback de conexão
client.on_connect = on_connect

# Conectar ao broker MQTT
client.connect(broker, port)

# Função para simular o envio de dados
def publicar_dados():
    while True:
        # Simular valores
        temperatura = round(random.uniform(20.0, 30.0), 2)
        umidade_solo = round(random.uniform(40.0, 80.0), 2)
        umidade_ar = round(random.uniform(50.0, 90.0), 2)

        # Criar um JSON com os dados
        payload = json.dumps({
            "temperatura": temperatura,
            "umidade_solo": umidade_solo,
            "umidade_ar": umidade_ar
        })

        # Publicar os dados nos tópicos correspondentes
        client.publish(topics["temperatura"], temperatura)
        client.publish(topics["umidade_solo"], umidade_solo)
        client.publish(topics["umidade_ar"], umidade_ar)
        
        print(f"Dados enviados: {payload}")
        
        # Esperar 5 segundos antes de enviar novamente
        time.sleep(5)

# Iniciar a publicação dos dados
publicar_dados()




#!######### POSSIBILIDADES DE ACORDO COM KIT
# topics = {
#     # Sensores de Ambiente
#     "temperatura": "planta1/temperatura",  # Sensor DHT11
#     "umidade_solo": "planta1/umidade_solo",  # Sensor de Umidade de Solo
#     "umidade_ar": "planta1/umidade_ar",  # Sensor DHT11
#     "luz": "planta1/luz",  # Sensor de Luz LDR
#     "chuva": "planta1/chuva",  # Sensor de Chuva

#     # Controle e Atuadores
#     "bomba_agua": "planta1/bomba_agua",  # MINI BOMBA DE ÁGUA
#     "valvula_1": "planta1/valvula_1",  # Módulo Relé 5V 2 Canais
#     "valvula_2": "planta1/valvula_2",  # Módulo Relé 5V 2 Canais

#     # Feedback e Status
#     "status_sistema": "planta1/status_sistema",  # Status geral do sistema
#     "erros": "planta1/erros",  # Mensagens de erro
#     "timestamp": "planta1/timestamp",  # Tempo dos dados

#     # Displays e Indicadores
#     "display": "planta1/display",  # Dados do Display LCD 16×2
#     "leds": {
#         "vermelho": "planta1/led_vermelho",
#         "amarelo": "planta1/led_amarelo",
#         "verde": "planta1/led_verde",
#         "azul": "planta1/led_azul",
#         "rgb": "planta1/led_rgb"
#     },

#     # Configurações e Dados Adicionais
#     "config_sensores": "planta1/config_sensores",  # Configurações dos sensores
#     "historico_temperatura": "planta1/historico_temperatura",  # Dados históricos
# }
