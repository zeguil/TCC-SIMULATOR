import dht
from machine import Pin, ADC
import time

# Configuração dos pinos
dht11 = dht.DHT11(Pin(2))  # Sensor DHT11 no pino D4 (GPIO2)
umidade_solo = ADC(Pin(36))  # Sensor de Umidade de Solo no pino A0 (GPIO36)
sensor_chuva = Pin(14, Pin.IN)  # Sensor de Chuva no pino D5 (GPIO14)
ldr = ADC(Pin(39))  # Sensor de Luz LDR no pino A1 (GPIO39)

def ler_dht11():
    try:
        dht11.measure()
        temp = dht11.temperature()
        umidade = dht11.humidity()
        print("Temperatura: {}°C, Umidade: {}%".format(temp, umidade))
    except OSError as e:
        print("Erro ao ler o DHT11:", e)

def ler_umidade_solo():
    umidade = umidade_solo.read()
    print("Umidade do Solo: {}".format(umidade))
    if umidade < 500:
        print("Solo seco")
    else:
        print("Solo úmido")

def ler_sensor_chuva():
    chuva = sensor_chuva.value()
    if chuva == 0:
        print("Chuva detectada")
    else:
        print("Sem chuva")

def ler_ldr():
    luz = ldr.read()
    print("Intensidade da Luz: {}".format(luz))
    if luz < 500:
        print("Baixa luminosidade")
    else:
        print("Alta luminosidade")

# Loop principal
while True:
    print("\nLendo sensores...")
    ler_dht11()
    ler_umidade_solo()
    ler_sensor_chuva()
    ler_ldr()
    
    time.sleep(5)  # Aguarda 5 segundos antes de ler novamente
