def print_risk_desc(i, risk):
    print(f'\n============================== {i}. {risk["risk_detected"]} ==================================================')
    print(f'Why is it a risk? : {risk["reason_for_risk"]}')
    print(f'Severity Rating (on a scale of 0 to 10): {risk["severity_rating"]}')
    print("Suggested Improvemnts in wordings:")
    if len(risk["suggested_alternative_wording"])>0:
        for alt in risk["suggested_alternative_wording"]:
            print(f"    # {alt}")
    else:
        print(" None")

        