from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Whisky(Base):
    __tablename__ = 'whiskies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    distillery_id = Column(Integer, ForeignKey('distilleries.id'), nullable=False)

    distillery = relationship("Distillery", back_populates="whiskies")