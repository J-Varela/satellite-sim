from fastapi import APIRouter
from app.models.satellite import Satellite
from app.simulation.engine import SimulationEngine
from app.simulation.orbit import orbital_period_seconds, satellite_position_eci

router = APIRouter(prefix="/satellites", tags=["satellites"])

engine = SimulationEngine()


@router.get("/demo")
def get_demo_satellite_position():
    satellite = Satellite(
        name="DemoSat-1",
        altitude_km=500,
        inclination_deg=45,
        phase_deg=0,
    )

    position = satellite_position_eci(satellite, time_seconds=0)
    period = orbital_period_seconds(satellite.altitude_km)

    return {
        "satellite": satellite.model_dump(),
        "position": position,
        "orbital_period_seconds": round(period, 2),
    }


@router.get("/demo/path")
def get_demo_satellite_path():
    satellite = Satellite(
        name="DemoSat-1",
        altitude_km=500,
        inclination_deg=45,
        phase_deg=0,
    )

    period = orbital_period_seconds(satellite.altitude_km)

    path = engine.generate_orbit_path(
        satellite=satellite,
        duration_seconds=int(period),
        step_seconds=120,
    )

    return {
        "satellite": satellite.model_dump(),
        "orbital_period_seconds": round(period, 2),
        "path": path,
    }