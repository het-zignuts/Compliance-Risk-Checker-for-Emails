import json
from uuid import UUID, uuid4
import os

def save_risk_analysis(response):
    response=response.model_dump()
    save_dir_pth="analysis_reports"
    os.makedirs(save_dir_pth, exist_ok=True)
    file_name=f"analysis_report_{uuid4().hex}.json"
    file_pth=os.path.join(save_dir_pth, file_name)

    with open(file_pth, "w", encoding="utf-8") as file:
        json.dump(response, file, indent=2)
        print(f"\n Report saved as: {file_pth}")