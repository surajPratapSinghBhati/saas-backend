from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.config.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    description = Column(String(500))

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )

    organization = relationship("Organization")

    tasks = relationship(
        "Task",
        back_populates="project"
    )