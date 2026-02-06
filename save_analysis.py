import json
from uuid import UUID, uuid4
import os

def save_risk_analysis(response):
    """
    Saves the risk analysis report as json
    """
    response=response.model_dump() # changing the model reponse from pydantic schema to python dict
    save_dir_pth="analysis_reports" # directory path wjere reports are saved
    os.makedirs(save_dir_pth, exist_ok=True) # create the dir if not exists
    file_name=f"analysis_report_{uuid4().hex}.json" # crete file name
    file_pth=os.path.join(save_dir_pth, file_name) # get file path

    with open(file_pth, "w", encoding="utf-8") as file:
        json.dump(response, file, indent=2) # save json in the file path
        print(f"\n Report saved as: {file_pth}")