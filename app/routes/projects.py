from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.config.database import SessionLocal
from app.models.project import Project
from app.models.task import Task
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

@router.get("/{project_id}/tasks")
def get_project_with_tasks(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    project = db.query(Project).options(
        joinedload(Project.tasks)
    ).filter(
        Project.id == project_id,
        Project.organization_id == current_user["organization_id"]
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "project": {
            "id": project.id,
            "name": project.name,
            "description": project.description
        },
        "tasks": [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status
            }
            for task in project.tasks
        ]
    }