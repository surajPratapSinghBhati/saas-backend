from fastapi import Request, HTTPException
from jose import jwt, JWTError

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

async def tenant_middleware(request: Request, call_next):

    public_routes = [
        "/login",
        "/register",
        "/docs",
        "/openapi.json",
        "/redoc",
        "/",
        "/test-db"
    ]

    if request.url.path in public_routes:
        response = await call_next(request)
        return response

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise HTTPException(
            status_code=401,
            detail="Token missing"
        )

    try:
        token = auth_header.split(" ")[1]

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        request.state.user_id = payload.get("user_id")
        request.state.organization_id = payload.get("organization_id")

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    response = await call_next(request)

    return response