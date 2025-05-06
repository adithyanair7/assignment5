from fastapi import FastAPI
from api.routers import (
    sandwiches_router,
    orders_router,
    resources_router,
    recipes_router,
    order_details_router,
)

app = FastAPI()

app.include_router(sandwiches_router.router)
app.include_router(orders_router.router)
app.include_router(resources_router.router)
app.include_router(recipes_router.router)
app.include_router(order_details_router.router)
