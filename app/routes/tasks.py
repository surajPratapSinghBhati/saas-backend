from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.utils.dependencies import get_current_user
from app.models.project import Project

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Task
@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    new_task = Task(
        title=task.title,
        description=task.description,
        project_id=task.project_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.put("/{task_id}")
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    task = db.query(Task).join(Task.project).filter(
    Task.id == task_id,
    Project.organization_id == current_user["organization_id"]
    ).first()

    if not task:
        raise HTTPException(
        status_code=404,
        detail="Task not found"
        )

    task.status = task_data.status

    db.commit()
    db.refresh(task)

    return task

# Get All Tasks
@router.get("/")
def get_tasks(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    tasks = db.query(Task).join(Task.project).filter(
    Project.organization_id == current_user["organization_id"]).all()

    return tasks