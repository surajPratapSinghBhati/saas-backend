from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.models.project import Project
from app.schemas.project import ProjectCreate
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    new_project = Project(
        name=project.name,
        description=project.description,
        organization_id=current_user["organization_id"]
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/")
def get_projects(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    projects = db.query(Project).filter(
        Project.organization_id == current_user["organization_id"]
    ).all()

    return projects