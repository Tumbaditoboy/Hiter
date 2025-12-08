from sqlalchemy import Column, Integer, ForeignKey
from persistence.db import Base, SessionLocal
from sqlalchemy.exc import SQLAlchemyError

class Clasificacion(Base):
    __tablename__ = "clasificacion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    peleador_id = Column(Integer, ForeignKey("peleadores.id"), nullable=False, unique=True)

    def save(self):
        session = SessionLocal()
        try:
            session.add(self)
            session.commit()
            session.refresh(self)
            return self.id
        finally:
            session.close()

    def update(self, peleador_id):
        session = SessionLocal()
        try:
            reg = session.query(Clasificacion).filter_by(id=self.id).first()
            if reg:
                reg.peleador_id = peleador_id
                session.commit()
                session.refresh(reg)
                return True
            return False
        finally:
            session.close()

    def delete(self):
        session = SessionLocal()
        try:
            reg = session.query(Clasificacion).filter_by(id=self.id).first()
            if reg:
                session.delete(reg)
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
        return session.query(Clasificacion).all()
    finally:
        session.close()
