# RevIntel AI — Revenue Intelligence & Sales Forecasting Platform

RevIntel AI is a polished full-stack portfolio project built to demonstrate revenue analytics, sales forecasting, anomaly detection, scenario planning, dataset upload, and exportable reporting in one business-facing product.

This package is intended to be **portfolio-ready**: it is presentable in GitHub, usable in demos, and credible in Upwork proposals.

## Why this project works for a portfolio

- Looks like a real internal analytics product, not a notebook demo
- Uses a seeded retail / e-commerce dataset so it can run immediately
- Connects frontend and backend with actual computed KPIs
- Includes forecasting, anomaly alerts, scenario planning, uploads, and exports
- Ships with deployment files, environment examples, and portfolio docs

## Included features

### Product experience
- Premium landing page
- Demo login screen
- Executive dashboard with KPI cards and trend charts
- Forecasting studio with model comparison
- Product intelligence page
- Regional performance page
- Anomaly detection center
- Scenario planner with persisted history
- Reports and export center
- Settings/data upload page

### Backend/business logic
- Seeded realistic retail dataset
- Live KPI calculations from active dataset
- Forecasting models:
  - Moving Average
  - Linear Regression
  - Random Forest
- Accuracy metrics: MAE, RMSE, MAPE, Bias
- Rolling z-score anomaly detection
- CSV upload and active dataset replacement
- CSV and PDF export endpoints
- SQLite persistence for scenario runs and upload metadata

## Tech stack

### Frontend
- React
- Vite
- Tailwind CSS
- TanStack Query
- Axios
- Recharts
- Framer Motion
- Lucide React

### Backend
- FastAPI
- pandas
- NumPy
- scikit-learn
- ReportLab
- SQLite

## Project structure

```text
revintel-ai-portfolio-final/
├── client/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── .env.example
│   └── package.json
├── server/
│   ├── app/
│   │   ├── api/routes/
│   │   ├── db/
│   │   └── services/
│   ├── data/
│   ├── .env.example
│   ├── Dockerfile
│   └── requirements.txt
├── docs/
│   ├── DEPLOYMENT_GUIDE.md
│   ├── PORTFOLIO_CASE_STUDY.md
│   ├── SCREENSHOT_SHOTLIST.md
│   └── UPWORK_PORTFOLIO_COPY.md
├── .gitignore
├── render.yaml
└── README.md
```

## Quick start

### 1) Backend

```bash
cd server
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend URL: `http://127.0.0.1:8000`

OpenAPI docs: `http://127.0.0.1:8000/docs`

### 2) Frontend

```bash
cd client
npm install
npm run dev
```

Frontend URL: `http://localhost:5173`

## Environment files

### Frontend
Copy `client/.env.example` to `.env` if you want to override the API URL.

### Backend
Copy `server/.env.example` to `.env` if you want to customize the database path, uploads path, or CORS origin.

## Default dataset schema

Expected CSV columns:

- order_id
- order_date
- product_name
- category
- sub_category
- region
- city
- channel
- customer_segment
- sales
- profit
- quantity
- discount

## Main API endpoints

### Dashboard
- `GET /api/dashboard/summary`
- `GET /api/dashboard/revenue-trend`
- `GET /api/dashboard/profit-trend`
- `GET /api/dashboard/top-products`
- `GET /api/dashboard/regions`
- `GET /api/dashboard/data-health`
- `POST /api/dashboard/upload-csv`

### Forecasting
- `GET /api/forecast/overall?horizon=30`
- `GET /api/forecast/model-metrics`
- `GET /api/forecast/category/{name}`
- `GET /api/forecast/region/{name}`

### Products / Regions / Anomalies
- `GET /api/products/performance`
- `GET /api/products/summary`
- `GET /api/products/top`
- `GET /api/products/low-performing`
- `GET /api/regions/performance`
- `GET /api/regions/heatmap`
- `GET /api/anomalies`
- `GET /api/anomalies/summary`
- `GET /api/anomalies/timeline`

### Scenario / Reports
- `POST /api/scenario/run`
- `GET /api/scenario/history`
- `GET /api/reports/library`
- `GET /api/reports/export-csv`
- `GET /api/reports/forecast-csv?horizon=30`
- `GET /api/reports/executive-pdf`

## Deployment

This package includes starter deployment files:

- `render.yaml` for the FastAPI backend
- `server/Dockerfile` for container builds
- `client/vercel.json` for SPA routing on Vercel

More details are in `docs/DEPLOYMENT_GUIDE.md`.

## Portfolio docs included

- `docs/PORTFOLIO_CASE_STUDY.md`
- `docs/UPWORK_PORTFOLIO_COPY.md`
- `docs/SCREENSHOT_SHOTLIST.md`

These help turn the project into a presentable portfolio asset instead of just code.

## Important note on models

This bundled version intentionally uses **Moving Average, Linear Regression, and Random Forest** so it runs more reliably on local machines and stays lightweight for demos.

If you want a heavier research-grade variant later, you can extend it with Prophet or XGBoost.

## Suggested next polish steps

- Deploy frontend and backend
- Capture 6 to 8 clean screenshots
- Record a 60 to 90 second demo video
- Add this project to GitHub with the included README and docs
- Use the included Upwork copy to position it as a flagship sample

## Portfolio positioning

Use this project for:
- sales forecasting portfolios
- revenue intelligence demos
- BI/dashboard freelance work
- anomaly detection analytics proposals
- internal business tools case studies

## Preview assets
Static portfolio visuals have been added to improve GitHub presentation:

![Monthly revenue trend](assets/monthly_revenue_trend.png)

![Revenue by region](assets/revenue_by_region.png)

## Backend smoke tests
```bash
cd server
pip install -r requirements.txt
pip install -r requirements-dev.txt
pytest -q
```
