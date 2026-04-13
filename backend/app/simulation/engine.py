from app.models.satellite import Satellite
from app.simulation.orbit import satellite_position_eci


class SimulationEngine:
    def generate_orbit_path(
        self,
        satellite: Satellite,
        duration_seconds: int,
        step_seconds: int,
    ) -> list[dict]:
        points = []

        for t in range(0, duration_seconds + 1, step_seconds):
            position = satellite_position_eci(satellite, t)
            points.append(
                {
                    "time_seconds": t,
                    "position": position,
                }
            )

        return points