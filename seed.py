from app.config.database import SessionLocal
from app.models.organization import Organization
from app.models.project import Project
from app.models.task import Task

db = SessionLocal()

# Create Organizations
org1 = Organization(name="Org Alpha")
org2 = Organization(name="Org Beta")

db.add_all([org1, org2])
db.commit()

db.refresh(org1)
db.refresh(org2)

print("Organizations created")

# Create Projects and Tasks
for i in range(1000):

    project1 = Project(
        name=f"Alpha Project {i}",
        description="Sample project",
        organization_id=org1.id
    )

    project2 = Project(
        name=f"Beta Project {i}",
        description="Sample project",
        organization_id=org2.id
    )

    db.add_all([project1, project2])
    db.commit()

    db.refresh(project1)
    db.refresh(project2)

    task1 = Task(
        title=f"Alpha Task {i}",
        description="Sample task",
        status="Pending",
        project_id=project1.id
    )

    task2 = Task(
        title=f"Beta Task {i}",
        description="Sample task",
        status="Pending",
        project_id=project2.id
    )

    db.add_all([task1, task2])

db.commit()

print("Database seeded successfully!")