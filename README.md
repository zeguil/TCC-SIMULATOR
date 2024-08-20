# Projeto de Monitoramento de Culturas 🌾

## Objetivo do Projeto

O objetivo deste projeto é **incentivar a agricultura familiar** e **reduzir o consumo de agrotóxicos** de legumes e frutas em grandes plantações. A proposta visa melhorar a gestão das pequenas propriedades agrícolas, proporcionando uma forma eficiente e tecnológica para monitorar e cuidar das plantas. O sistema permite aos agricultores familiares acompanhar em tempo real as condições de suas culturas, ajudando-os a tomar decisões mais informadas e menos dependentes de produtos químicos.

## Estrutura do Projeto

1. **Hardware e Sensores**
   - **ESP32 com Vários Sensores**: O projeto utiliza um módulo ESP32 que é equipado com diversos sensores para monitorar as condições das plantas. Esses sensores incluem:
     - **Sensor de Umidade e Temperatura (DHT11)**
     - **Sensor de Umidade do Solo**
     - **Sensor de Luz (LDR)**
     - **Sensor de Chuva**
     - e mais...
   - O ESP32 coleta dados desses sensores e os envia para um broker MQTT para processamento e visualização.

2. **Comunicação com MQTT**
   - **Mosquitto**: É utilizado como broker MQTT para receber e gerenciar os dados enviados pelos sensores do ESP32. O Mosquitto facilita a comunicação eficiente entre os diferentes componentes do sistema.

3. **Processamento de Dados**
   - **Bot**: Um bot é responsável por receber os dados do Mosquitto e encaminhá-los para a API. Esse bot atua como intermediário, garantindo que as informações sejam corretamente transmitidas e processadas.

4. **API para Acesso aos Dados**
   - **FastAPI**: A API desenvolvida com FastAPI recebe e processa os dados enviados pelo bot. Ela oferece endpoints para a visualização e análise dos dados, permitindo que o sistema seja acessado de forma rápida e eficiente.

5. **Aplicativo Mobile**
   - **Kotlin**: Um aplicativo mobile desenvolvido em Kotlin consome a API e apresenta os dados em tempo real. O aplicativo permite aos agricultores familiares visualizar as condições de suas colheitas diretamente na palma da mão, facilitando o monitoramento e a gestão das plantas.

## Tecnologias Utilizadas

- **ESP32 com MicroPython**: O microcontrolador ESP32, programado em MicroPython, é a peça central do sistema, responsável pela coleta dos dados dos sensores e comunicação com o broker MQTT.
- **Mosquitto**: Broker MQTT que gerencia a comunicação dos dados entre o ESP32 e os outros componentes do sistema.
- **FastAPI**: Framework para criação da API que gerencia a interação com o banco de dados e fornece dados para o aplicativo mobile.
- **Kotlin**: Linguagem de programação utilizada para desenvolver o aplicativo mobile que consome a API e exibe os dados de forma amigável ao usuário.

## Benefícios para a Agricultura Familiar

- **Redução do Uso de Agrotóxicos**: Ao monitorar as condições das plantas em tempo real, é possível fazer ajustes precisos nas práticas de cultivo, reduzindo a necessidade de agrotóxicos.
- **Acesso a Dados em Tempo Real**: Com a tecnologia móvel, os agricultores podem acessar informações detalhadas sobre suas colheitas a qualquer momento, ajudando a tomar decisões mais assertivas.
- **Eficiência na Gestão**: O sistema melhora a eficiência no manejo das plantações, permitindo um controle mais preciso das condições ambientais e das necessidades das plantas.

