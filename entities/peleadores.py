from sqlalchemy import Column, Integer, String
from persistence.db import Base, SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class Peleadores(Base):
    __tablename__ = "peleadores"

    id = Column(Integer, primary_key=True, autoincrement=True, )
    nombre = Column(String(100), nullable=False)
    alias = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    ubicacion = Column(String(150), nullable=False)
    nivel_pelea = Column(Integer, nullable=False)
    foto = Column(String(255))
    descripcion = Column(String(255), nullable=False)

    def save(self):
        session = SessionLocal()
        try:    
            session.add(self)
            session.commit()
            session.refresh(self)
            return self.id
        finally:
            session.close()

    def update(self, nombre, alias, edad, ubicacion, nivel_pelea, foto, descripcion):
        session = SessionLocal()
        try:
            peleador = session.query(Peleadores).filter_by(id = self.id).first()
            if peleador: 
                peleador.nombre = nombre
                peleador.alias = alias
                peleador.edad = edad
                peleador.ubicacion = ubicacion
                peleador.nivel_pelea = nivel_pelea
                peleador.foto = foto
                peleador.descripcion = descripcion
                session.commit()
                session.refresh(peleador)
                return True
            return False
        finally:
            session.close() 

    def delete(self):
        session = SessionLocal()
        try:
            peleador = session.query(Peleadores).filter_by(id = self.id).first()
            if peleador:
                session.delete(peleador)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            print(e)
            return False
        finally:
            session.close()

def get_all():
    session = SessionLocal()
    try:
        return session.query(Peleadores).all()
    finally:
        session.close()
