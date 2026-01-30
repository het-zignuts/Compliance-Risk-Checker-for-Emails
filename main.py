from langchain_file import chain
from print_risk import print_risk_desc
from save_analysis import save_risk_analysis

def main():
    print("AI Assistant for Corporate Email Compliance and Risk Detection===>")
    while True:
        email_body=input("Enter the email body: ")
        risk_analysis=chain.invoke({"email_body": email_body})
        risk_analysis_dict=risk_analysis.model_dump()
        print("AI assistant says: \n")
        i=1
        for risk in risk_analysis_dict["risks"]:
            print_risk_desc(i, risk)
            i+=1
        ans=input("\n Do you want to save the risk analysis report: (y/n) : ")
        if ans=='y':
            save_risk_analysis(risk_analysis)
        resp=input("\n\n Do you want to continue? (Type 'EXIT' to leave.): ")
        if resp=='EXIT':
            break
main()