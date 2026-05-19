from fastapi import FastAPI
from sqlalchemy import text

from app.config.database import engine, Base

from app.models.organization import Organization
from app.models.user import User
from app.models.project import Project
from app.models.task import Task
from app.routes.auth import router as auth_router
from app.middleware.tenant import tenant_middleware
from fastapi import Request
from app.routes.projects import router as project_router
from app.routes.tasks import router as task_router

# print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(tenant_middleware)

app.include_router(auth_router)
app.include_router(project_router)
app.include_router(task_router)


@app.get("/")
def root():
    return {"message": "SaaS Backend API Running"}

@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"message": "Database connected successfully"}

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/protected")
def protected_route(request: Request):

    return {
        "message": "Protected route working",
        "user_id": request.state.user_id,
        "organization_id": request.state.organization_id
    }    