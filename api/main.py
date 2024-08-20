from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any, Union

app = FastAPI()

# Armazenar dados recebidos
received_data = []

class Data(BaseModel):
    topic: str
    data: str

@app.post("/data")
async def receive_data(data: Data):
    print(f"Dados recebidos: {data}")
    received_data.append(data.dict())
    return {"status": "success", "data": data.dict()}

@app.get("/data")
async def get_data():
    # Agrupar os dados em conjuntos separados
    grouped_data = []
    current_group = []

    for item in received_data:
        current_group.append(item)
        # Se o grupo tiver 3 itens, finalize o grupo atual e inicie um novo
        if len(current_group) == 3:
            grouped_data.append(current_group)
            current_group = []

    # Adicione qualquer grupo restante
    if current_group:
        grouped_data.append(current_group)

    return {"status": "success", "data": grouped_data}

@app.get("/data/latest")
async def get_latest_data():
    # Agrupar os dados em conjuntos separados
    grouped_data = []
    current_group = []

    for item in received_data:
        current_group.append(item)
        # Se o grupo tiver 3 itens, finalize o grupo atual e inicie um novo
        if len(current_group) == 3:
            grouped_data.append(current_group)
            current_group = []

    # Adicione qualquer grupo restante
    if current_group:
        grouped_data.append(current_group)

    # Retorna o último grupo, se existir
    if grouped_data:
        latest_group = grouped_data[-1]
        return {"status": "success", "data": latest_group}
    else:
        return {"status": "success", "data": []}
