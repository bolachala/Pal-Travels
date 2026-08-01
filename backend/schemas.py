from pydantic import BaseModel, ConfigDict

class TravelCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    destination: str
    price: float
    people: int
    duration: int
    
class TravelResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    destination: str
    price: float
    people: int
    duration: int