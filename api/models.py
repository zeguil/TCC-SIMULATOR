from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Relações
    cultivations = relationship('Cultivation', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

class Cultivation(Base):
    __tablename__ = 'cultivations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    # Relacionamento com User
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='cultivations')

    # Relacionamento com Plant
    plant_id = Column(Integer, ForeignKey('plants.id'))
    plant = relationship('Plant', back_populates='cultivations')

    # Relacionamento com Sensor
    sensors = relationship('Sensor', back_populates='cultivation')

    def __repr__(self):
        return f"<Cultivation(id={self.id}, name={self.name}, user_id={self.user_id}, plant_id={self.plant_id})>"

class Plant(Base):
    __tablename__ = 'plants'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    
    temperature = Column(Float, nullable=True)
    soil_moisture = Column(Float, nullable=True)
    air_humidity = Column(Float, nullable=True)
    light_intensity = Column(Float, nullable=True)
    rain_sensor = Column(Float, nullable=True)
    
    water_pump_status = Column(String, nullable=True)
    relay_status = Column(String, nullable=True)
    
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relacionamento com Cultivation
    cultivations = relationship('Cultivation', back_populates='plant')

    def __repr__(self):
        return f"<Plant(id={self.id}, name={self.name}, temperature={self.temperature}, soil_moisture={self.soil_moisture}, air_humidity={self.air_humidity}, light_intensity={self.light_intensity}, rain_sensor={self.rain_sensor}, water_pump_status={self.water_pump_status}, relay_status={self.relay_status}, last_updated={self.last_updated})>"

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True, index=True)
    numero_serie = Column(String, unique=True, index=True)
    
    # Relacionamento com Cultivation
    cultivation_id = Column(Integer, ForeignKey('cultivations.id'))
    cultivation = relationship('Cultivation', back_populates='sensors')

    # Relacionamento com SensorData
    sensor_data = relationship('SensorData', back_populates='sensor')

    def __repr__(self):
        return f"<Sensor(id={self.id}, numero_serie={self.numero_serie}, cultivation_id={self.cultivation_id})>"

class SensorData(Base):
    __tablename__ = 'sensor_data'

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

    # Relação com Sensor
    sensor_id = Column(Integer, ForeignKey('sensors.id'))
    sensor = relationship('Sensor', back_populates='sensor_data')

    # Índices compostos
    __table_args__ = (
        Index('ix_numero_serie_timestamp', 'numero_serie', 'timestamp'),
        Index('ix_status_sistema_timestamp', 'status_sistema', 'timestamp'),
    )

    def __repr__(self):
        return f"<SensorData(id={self.id}, numero_serie={self.numero_serie}, temperatura={self.temperatura}, umidade_solo={self.umidade_solo}, umidade_ar={self.umidade_ar}, luz={self.luz}, chuva={self.chuva}, status_sistema={self.status_sistema}, erros={self.erros}, timestamp={self.timestamp})>"
