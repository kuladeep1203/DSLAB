


# import pandas as pd
# import numpy as np

# df = pd.read_csv("diabetes.csv")

 
# def prob_diabetes():
#     count = 0
#     for i in df['Outcome']:
#         if i == 1:
#             count += 1
#     return round(count/len(df['Outcome']),3)

# def prob_diabetes_age(age):
#     count = 0
#     people=len(df[df["Age"]>age])
#     for i in range(len(df['Outcome'])):
#         if df['Age'][i] > age and df['Outcome'][i] == 1:
#             count += 1
        
#     return round(count/people,3)

  
# def prob_diabetes_age_range(age1, age2):
#     count = 0
#     people=len(df[(df["Age"]>=age1) & (df["Age"]<=age2)])
#     for i in range(len(df['Outcome'])):
#         if df['Age'][i] >= age1 and df['Age'][i] <= age2 and df['Outcome'][i] == 1:
#             count += 1
#     return round(count/people,3)

# def prob_diabetes_age_less(age):
#     count = 0
#     people=len(df[df["Age"]<age])
#     for i in range(len(df['Outcome'])):
#         if df['Age'][i] < age and df['Outcome'][i] == 1:
#             count += 1
#     return  round(count/people,3)

# def main():
#     print("1. Find the probability of diabetes given the dataset.")
#     print("2. Find the probability of diabetes given the age above 50.")
#     print("3. Find the probability of diabetes given the age between 40 and 50.")
#     print("4. Find the probability of diabetes given the age between 30 and 40.")
#     print("5. Find the probability of diabetes given the age less than 30.")
#     print("6. Exit")
#     x=True
#     while x:
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             print("Probability of diabetes given the dataset: ", prob_diabetes())
#         elif choice == 2:
#             print("Probability of diabetes given the age above 50: ", prob_diabetes_age(50))
#         elif choice == 3:
#             print("Probability of diabetes given the age between 40 and 50: ", prob_diabetes_age_range(40, 50))
#         elif choice == 4:
#             print("Probability of diabetes given the age between 30 and 40: ", prob_diabetes_age_range(30, 40))
#         elif choice == 5:
#             print("Probability of diabetes given the age less than 30: ", prob_diabetes_age_less(30))
#         elif choice == 6:
#             x=False
#         else:
#             print("Invalid choice")
# main()

        
# # 2nd question
# # # Find the probability of diabetes with a glucose level of more than 120 + blood pressure of more than 90 + skin thickness of more than 30 + insulin above 150 + BMI above 25.


# # # Note: In the outcome column given in the dataset, 1 means that diabetes is present, and 0 means the absence of diabetes
    
    
import pandas as pd
import numpy as np

df = pd.read_csv("diabetes.csv")

diabetes_count=df[(df["Outcome"]==1) & (df["Glucose"]>120) & (df["BloodPressure"]>90) & (df["SkinThickness"]>30) & (df["Insulin"]>150) & (df["BMI"]>25)]
people_count=df[(df["Glucose"]>120) & (df["BloodPressure"]>90) & (df["SkinThickness"]>30) & (df["Insulin"]>150) & (df["BMI"]>25)]

print("Probability of diabetes with a glucose level of more than 120 + blood pressure of more than 90 + skin thickness of more than 30 + insulin above 150 + BMI above 25: ",round( len(diabetes_count)/len(people_count)),3)


import pandas as pd


diabetes_df = pd.read_csv("diabetes.csv")


def calculate_probability_diabetes():
    count_diabetes = 0
    total_records = len(diabetes_df)
    
   
    for outcome in diabetes_df['Outcome']:
        if outcome == 1:
            count_diabetes += 1
    
    
    probability = round(count_diabetes / total_records, 3)
    return probability


def calculate_probability_diabetes_age_above(age_threshold):
    count_diabetes = 0
    total_above_age = len(diabetes_df[diabetes_df["Age"] > age_threshold])
    
    
    for index, row in diabetes_df.iterrows():
        if row['Age'] > age_threshold and row['Outcome'] == 1:
            count_diabetes += 1
        
   
    probability = round(count_diabetes / total_above_age, 3)
    return probability


def calculate_probability_diabetes_age_range(age_min, age_max):
    count_diabetes = 0
    total_in_age_range = len(diabetes_df[(diabetes_df["Age"] > age_min) & (diabetes_df["Age"] <= age_max)])
    
    
    for index, row in diabetes_df.iterrows():
        if age_min < row['Age'] <= age_max and row['Outcome'] == 1:
            count_diabetes += 1
    
    
    probability = round(count_diabetes / total_in_age_range, 3)
    return probability

def calculate_probability_diabetes_age_below(age_threshold):
    count_diabetes = 0
    total_below_age = len(diabetes_df[diabetes_df["Age"] <= age_threshold])
    
    
    for index, row in diabetes_df.iterrows():
        if row['Age'] < age_threshold and row['Outcome'] == 1:
            count_diabetes += 1
    
    
    probability = round(count_diabetes / total_below_age, 3)
    return probability


def main():
    print("1. Find the probability of diabetes given the dataset.")
    print("2. Find the probability of diabetes given the age above 50.")
    print("3. Find the probability of diabetes given the age between 40 and 50.")
    print("4. Find the probability of diabetes given the age between 30 and 40.")
    print("5. Find the probability of diabetes given the age less than 30.")
    print("6. Exit")
    
    while True:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Probability of diabetes given the dataset: ", calculate_probability_diabetes())
        elif choice == 2:
            age_threshold = 50
            print("Probability of diabetes given age above", age_threshold, ": ", calculate_probability_diabetes_age_above(age_threshold))
        elif choice == 3:
            age_min = 40
            age_max = 50
            print("Probability of diabetes given age between", age_min, "and", age_max, ": ", calculate_probability_diabetes_age_range(age_min, age_max))
        elif choice == 4:
            age_min = 30
            age_max = 40
            print("Probability of diabetes given age between", age_min, "and", age_max, ": ", calculate_probability_diabetes_age_range(age_min, age_max))
        elif choice == 5:
            age_threshold = 30
            print("Probability of diabetes given age below", age_threshold, ": ", calculate_probability_diabetes_age_below(age_threshold))
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
