# PROMPTS.md

## 1. Architecture Prompt

Help me design a multi-tenant SaaS backend using FastAPI with JWT authentication, middleware-based tenant isolation, SQLAlchemy models, and CRUD APIs for projects and tasks.

---

## 2. Refinement Loop

### Example 1

Initial AI-generated task APIs did not properly enforce tenant isolation.

#### Problem
Users from one organization could potentially access tasks belonging to another organization because filtering was not applied through project relationships.

#### Fix
Added organization-level filtering using SQLAlchemy joins between Task and Project models. Unauthorized access now returns a 404 response.

---

### Example 2

Initial nested project-task endpoint caused potential N+1 query issues.

#### Problem
Tasks were being lazily loaded for each project separately, which could increase query count significantly with large datasets.

#### Fix
Implemented SQLAlchemy `joinedload()` to eagerly fetch related tasks efficiently in a single optimized query.

---

## 3. AI Blindspot Note

The AI struggled most with secure multi-tenant isolation and database query optimization. Initial implementations missed tenant-safe filtering in task APIs and did not account for N+1 query problems during nested resource fetching. These issues required manual review, debugging, and optimization to ensure secure enterprise-grade backend behavior.