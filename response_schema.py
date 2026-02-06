from pydantic import BaseModel
from typing import List

class Risk(BaseModel):
    """
    Schema for individual risk detected.
    """
    risk_detected: str # what risk is detected
    reason_for_risk: str # why is it a risk?
    suggested_alternative_wording: List[str] # what alternative words can be used in the mail for it to not classify as risky
    severity_rating: int # severity of rsk rated from 0 to 10.

class RiskAnalysisResponse(BaseModel):
    risks: List[Risk] # Collection (list) of risks with each one being of Risk schema, returned by the LLM.