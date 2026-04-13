# Backend — Satellite Coverage Simulator API

FastAPI service that models satellites in circular orbits and exposes their position data over HTTP.

## Requirements

- Python 3.14+
- Dependencies: `fastapi`, `uvicorn[standard]`, `pydantic`

## Setup

```bash
cd backend

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

## Running the server

```bash
python run.py
```

The API will be available at `http://127.0.0.1:8000`.  
Interactive docs: `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/satellites/demo` | Position of a demo satellite at t=0 |
| GET | `/satellites/demo/path` | Full orbit path sampled every 2 minutes |

## Project Layout

```
backend/
├── run.py                  # Entry point (uvicorn)
├── requirements.txt
├── pyproject.toml
└── app/
    ├── main.py             # FastAPI app and router registration
    ├── api/routes/
    │   └── satellites.py   # Satellite endpoints
    ├── core/
    │   └── constants.py    # Earth radius, gravitational parameter
    ├── models/
    │   └── satellite.py    # Satellite Pydantic model
    └── simulation/
        ├── engine.py       # SimulationEngine — orbit path generation
        └── orbit.py        # Orbital mechanics (ECI position, period)
```

## Orbital Model

The simulation uses a simplified **circular orbit in Earth-Centered Inertial (ECI)** coordinates:

- Altitude and inclination are configurable per satellite.
- The orbit is tilted by inclination around the X-axis.
- RAAN and argument of perigee are not modelled in Phase 1.

Key constants (from `app/core/constants.py`):

| Constant | Value |
|----------|-------|
| Earth radius | 6 371 km |
| Earth μ (GM) | 398 600.4418 km³/s² |
