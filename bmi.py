def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = weight/(height**2)
 print("Calculated BMI = " + str(bmi))
# Determine weight classification based on BM
 if (bmi < 18.5):
    classification = "Under Weight"
    value = -1
 elif (18.5 <= bmi <= 25.0):
    classification = "Normal Weight"
    value = 0
 else:
    classification = "Over Weight"
    value = 1
 print("Weight Classification = " + classification)
 return value
 
value = calculate_bmi(weight=57, height=1.73)
print(value)