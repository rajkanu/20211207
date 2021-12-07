import pandas as pd
import json

with open ("input_file.json","r") as file:
    rawData = json.load(file)

df = pd.DataFrame(rawData)

list_BMI=[]
list_BMI_category=[]
list_health_risk=[]

def calculate_BMI(height, weight):
    bmi=round(weight/(height/100)**2,2)
    return(bmi)

def categorization_BMI(bmi):
    if bmi<18.4:
        bmi_category="Underweight"
    elif (bmi>=18.5 and bmi<=24.9):
        bmi_category="Normal weight"
    elif (bmi>=25 and bmi<=29.9):
        bmi_category="Overweight"
    elif (bmi>=30 and bmi<=34.9):
        bmi_category="Moderately obese"
    elif (bmi>=35 and bmi<=39.9):
        bmi_category="Severely obese"
    else:
        bmi_category="Very severely obese"
    return bmi_category

def health_risk(bmi):
    if bmi <18.4:
        health_risk = "Malnutrition"
    elif (bmi>=18.5 and bmi<=24.9):
        health_risk = "Low risk"
    elif (bmi>=25 and bmi<=29.9):
        health_risk = "Enhanced risk"
    elif (bmi>=30 and bmi <= 34.9):
        health_risk = "Medium risk"
    elif (bmi>=35 and bmi <=39.9):
        health_risk = "High risk"
    else:
        health_risk = "Very high risk"
    return health_risk


for item in range(len(df)):
    BMI_value = calculate_BMI(df.loc[item, "HeightCm"],df.loc[item, "WeightKg"])
    list_BMI.append(BMI_value)
    BMI_category_value = categorization_BMI(BMI_value)
    list_BMI_category.append(BMI_category_value)
    health_risk_value = health_risk(BMI_value)
    list_health_risk.append(health_risk_value)

final_data = df.assign(**{"BMI" :list_BMI, "BMI category" :list_BMI_category, "Health risk":list_health_risk})
print(final_data)

json_file = final_data.to_json
print(json_file)


def overweight(final_data):
    counter = 0
    for item in range(len(final_data)):
        if final_data.loc[item, "BMI category"] == "Overweight":
               counter = counter + 1
    return counter           
total_overweight = overweight(final_data)
print("Total overweight =", total_overweight)


