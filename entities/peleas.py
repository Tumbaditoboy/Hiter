from sqlalchemy import Column, Integer, String, DateTime
from persistence.db import Base, SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class Peleas(Base):
    __tablename__ = "peleas"

    id = Column(Integer, primary_key=True, autoincrement=True, )
    peleador1_id = Column(Integer, nullable=False)
    peleador2_id = Column(Integer, nullable=False)
    fecha = Column(DateTime, nullable=False)
    ubicacion = Column(String(150), nullable=False)
    estado = Column(String(20))
    ganador = Column(Integer)

    def save(self):
        session = SessionLocal()
        try:    
            session.add(self)
            session.commit()
            session.refresh(self)
            return self.id
        finally:
            session.close()

    def update(self, peleador1_id, peleador2_id, fecha, ubicacion, estado, ganador):
        session = SessionLocal()
        try:
            pelea = session.query(Peleas).filter_by(id = self.id).first()
            if pelea: 
                pelea.peleador1_id = peleador1_id
                pelea.peleador2_id = peleador2_id
                pelea.fecha = fecha
                pelea.ubicacion = ubicacion
                pelea.estado = estado
                pelea.ganador = ganador

                session.commit()
                session.refresh(pelea)
                return True
            return False
        finally:
            session.close() 

    def delete(self):
        session = SessionLocal()
        try:
            pelea = session.query(Peleas).filter_by(id = self.id).first()
            if pelea:
                session.delete(pelea)
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
        return session.query(Peleas).all()
    finally:
        session.close()
