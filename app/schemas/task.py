from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    project_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str

class Config:
    from_attributes = True

class TaskUpdate(BaseModel):
    status: str