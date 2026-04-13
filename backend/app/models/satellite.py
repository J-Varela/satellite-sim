from pydantic import BaseModel, Field


class Satellite(BaseModel):
    name: str = Field(..., description="Satellite name")
    altitude_km: float = Field(..., gt=0, description="Altitude above Earth in kilometers")
    inclination_deg: float = Field(..., ge=0, le=180, description="Orbital inclination in degrees")
    phase_deg: float = Field(default=0, description="Starting phase angle in degrees")