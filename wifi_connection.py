import network

import time

REDE = ''
SENHA = ''

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)

sta_if.connect(REDE, SENHA)

while not sta_if.isconnected():
    print("Conectando...")
    time.sleep(1)


print('Conectado')

print(f'Configurações de rede: {str(sta_if.ifconfig())}')