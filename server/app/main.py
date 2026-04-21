import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import anomalies, dashboard, forecast, products, regions, reports, scenario
from app.db.storage import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(title='RevIntel AI API', version='2.0.0', lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('REVINTEL_ALLOWED_ORIGIN', '*')],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(dashboard.router, prefix='/api/dashboard', tags=['Dashboard'])
app.include_router(forecast.router, prefix='/api/forecast', tags=['Forecast'])
app.include_router(products.router, prefix='/api/products', tags=['Products'])
app.include_router(regions.router, prefix='/api/regions', tags=['Regions'])
app.include_router(anomalies.router, prefix='/api/anomalies', tags=['Anomalies'])
app.include_router(scenario.router, prefix='/api/scenario', tags=['Scenario'])
app.include_router(reports.router, prefix='/api/reports', tags=['Reports'])


@app.get('/')
def health_check():
    return {'message': 'RevIntel AI API is running', 'version': '2.0.0'}
