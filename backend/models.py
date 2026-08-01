from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import func


class Travel(Base):
    __tablename__ = "travel"

    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String, index=True)
    price = Column(Float)
    people = Column(Integer, nullable=False)
    duration = Column(Integer)
