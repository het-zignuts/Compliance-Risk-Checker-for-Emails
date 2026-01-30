from pydantic import BaseModel
from typing import List

class Risk(BaseModel):
    risk_detected: str
    reason_for_risk: str
    suggested_alternative_wording: List[str]
    severity_rating: int

class RiskAnalysisResponse(BaseModel):
    risks: List[Risk]