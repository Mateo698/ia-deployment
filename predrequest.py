from pydantic import BaseModel
class PredictionRequest(BaseModel):
    Clear: int
    Distance: float
    City_Freq: float
    State_Freq: float
    Day_of_Year: int
    Temperature: int
    Wind_Speed: float