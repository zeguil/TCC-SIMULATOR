from machine import Pin, ADC
import time

# Configuração dos pinos
umidade_solo = ADC(Pin(36))  # Sensor de Umidade de Solo no pino A0 (GPIO36)
rele_bomba = Pin(4, Pin.OUT)  # Relé para controlar a bomba no pino D2 (GPIO4)

# Definir o limiar de umidade (ajuste conforme necessário)
UMIDADE_LIMIAR = 500  # Valor que define quando ligar a bomba

def verificar_umidade_solo():
    umidade = umidade_solo.read()
    print("Umidade do Solo:", umidade)
    return umidade

def controlar_bomba():
    umidade = verificar_umidade_solo()
    if umidade < UMIDADE_LIMIAR:
        print("Umidade baixa. Ligando a bomba...")
        rele_bomba.value(1)  # Liga a bomba
    else:
        print("Umidade adequada. Desligando a bomba...")
        rele_bomba.value(0)  # Desliga a bomba

# Loop principal
while True:
    controlar_bomba()
    time.sleep(60)  # Aguarda 60 segundos antes de verificar novamente
