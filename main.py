from langchain_file import chain
from print_risk import print_risk_desc
from save_analysis import save_risk_analysis

def main():
    """
    Main fuction...
    """
    print("AI Assistant for Corporate Email Compliance and Risk Detection===>")
    while True:
        email_body=input("Enter the email body: ") # get the email body
        risk_analysis=chain.invoke({"email_body": email_body}) # invoke the langchain
        risk_analysis_dict=risk_analysis.model_dump() # convert the pydantic object to python dict
        print("AI assistant says: \n")
        i=1
        for risk in risk_analysis_dict["risks"]: # print each risk.
            print_risk_desc(i, risk)
            i+=1
        ans=input("\n Do you want to save the risk analysis report: (y/n) : ")
        if ans=='y':
            save_risk_analysis(risk_analysis) # save the report 
        resp=input("\n\n Do you want to continue? (Type 'EXIT' to leave.): ")
        if resp=='EXIT':
            break
main() # call to main function