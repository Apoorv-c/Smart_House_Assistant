from pydantic import BaseModel
from typing import List

class Room(BaseModel):
    type: str
    x: float
    y: float
    width: float
    height: float

class Plot(BaseModel):
    length: float
    width: float

class AnalysisInput(BaseModel):
    plot: Plot
    layout: List[Room]