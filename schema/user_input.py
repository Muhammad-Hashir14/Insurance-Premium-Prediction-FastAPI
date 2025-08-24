from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal
from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, le=120, description="Provide age of the user", examples=[12,54])]
    weight:Annotated[float, Field(..., description="Provide weight of the user", examples=[14,43])]
    height: Annotated[float, Field(..., description="Provide height of the user", examples=[5.4,6.2])]
    income_lpa:Annotated[float, Field(..., description="provide income lac per anum", examples=[34.28000, 43.00])]
    smoker:Annotated[bool, Field(..., description="Is the the user smoker", examples=[True, False])]
    city: Annotated[str, Field(..., description="Provide the city that user belong", examples=["Mumbai", "Chennai"])]
    occupation: Annotated[str, Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Provide occupation of the user")]
    
    @field_validator("city")
    @classmethod
    def normalize_city(cls, v:str) -> str:
        return v.strip().title()
    
    @computed_field
    @property
    def bmi(self)-> float:
        return (self.weight/(self.height ** 2))
    
    @computed_field
    @property
    def age_group(self)-> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
    
    

    










