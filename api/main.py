from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = FastAPI()

# Configurações do banco de dados SQLite
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição do modelo do banco de dados com índices
class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    numero_serie = Column(String, index=True)
    temperatura = Column(Float)
    umidade_solo = Column(Float)
    umidade_ar = Column(Float)
    luz = Column(Float)
    chuva = Column(Boolean)
    status_sistema = Column(String, index=True)
    erros = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)

    # Adicionar índices compostos
    __table_args__ = (
        Index('ix_numero_serie_timestamp', 'numero_serie', 'timestamp'),
        Index('ix_status_sistema_timestamp', 'status_sistema', 'timestamp'),
    )

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Modelos de dados
class Data(BaseModel):
    numero_serie: str
    temperatura: float
    umidade_solo: float
    umidade_ar: float
    luz: float
    chuva: bool
    status_sistema: str
    erros: str
    timestamp: str

@app.post("/data")
async def receive_data(data: Data):
    db = SessionLocal()
    db_data = SensorData(
        numero_serie=data.numero_serie,
        temperatura=data.temperatura,
        umidade_solo=data.umidade_solo,
        umidade_ar=data.umidade_ar,
        luz=data.luz,
        chuva=data.chuva,
        status_sistema=data.status_sistema,
        erros=data.erros,
        timestamp=datetime.fromisoformat(data.timestamp)
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    db.close()
    return {"status": "success", "data": data.dict()}

@app.get("/data")
async def get_data():
    db = SessionLocal()
    results = db.query(SensorData).all()
    db.close()
    return {"status": "success", "data": [result.__dict__ for result in results]}

@app.get("/data/latest")
async def get_latest_data():
    db = SessionLocal()
    latest_entry = db.query(SensorData).order_by(SensorData.timestamp.desc()).first()
    db.close()
    if latest_entry:
        return {"status": "success", "data": latest_entry.__dict__}
    else:
        return {"status": "success", "data": {}}
