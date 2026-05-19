from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )