from fastapi import FastAPI

from src.routers.roles import router as roles_router
from src.routers.employees import router as employees_router

app = FastAPI()

app.include_router(roles_router, prefix='/roles', tags=['roles'])
app.include_router(employees_router, prefix='/employees', tags=['employees'])
