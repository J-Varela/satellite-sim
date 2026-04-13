import math
from app.core.constants import EARTH_RADIUS_KM, EARTH_MU
from app.models.satellite import Satellite


def orbital_radius_km(altitude_km: float) -> float:
    return EARTH_RADIUS_KM + altitude_km


def mean_motion_rad_per_sec(orbital_radius: float) -> float:
    """
    For a circular orbit:
    n = sqrt(mu / r^3)
    """
    return math.sqrt(EARTH_MU / (orbital_radius ** 3))


def satellite_position_eci(satellite: Satellite, time_seconds: float) -> dict:
    """
    Very simplified circular orbit in Earth-centered inertial coordinates.
    We include inclination, but skip RAAN and argument of perigee for Phase 1.
    """
    r = orbital_radius_km(satellite.altitude_km)
    n = mean_motion_rad_per_sec(r)

    phase_rad = math.radians(satellite.phase_deg)
    inclination_rad = math.radians(satellite.inclination_deg)

    theta = n * time_seconds + phase_rad

    # Base circular orbit in orbital plane
    x_orb = r * math.cos(theta)
    y_orb = r * math.sin(theta)
    z_orb = 0.0

    # Tilt orbit by inclination around x-axis
    x = x_orb
    y = y_orb * math.cos(inclination_rad)
    z = y_orb * math.sin(inclination_rad)

    return {
        "x_km": round(x, 3),
        "y_km": round(y, 3),
        "z_km": round(z, 3),
    }


def orbital_period_seconds(altitude_km: float) -> float:
    r = orbital_radius_km(altitude_km)
    n = mean_motion_rad_per_sec(r)
    return (2 * math.pi) / n