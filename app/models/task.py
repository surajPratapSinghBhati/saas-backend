from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    description = Column(String(500))

    status = Column(String(50), default="Pending")

    project_id = Column(
        Integer,
        ForeignKey("projects.id")
    )

    project = relationship(
        "Project",
        back_populates="tasks"
    )