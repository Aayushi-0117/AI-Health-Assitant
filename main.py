print("============== AI HEALTH ASSISTANT ==============\n")
print("NOTE: This is only for basic health awareness. Always consult a doctor for medical advice.\n")

# Taking User Input
age = int(input("Enter your age: "))
sleep = int(input("How many hours do you sleep daily? "))
water = int(input("How many glasses of water do you drink daily? "))

print("\nSelect your symptoms (Type YES or NO)\n")

fever = input("Do you have fever? ")
cough = input("Do you have cough? ")
headache = input("Do you have headache? ")
tired = input("Do you feel tired frequently? ")

risk_score = 0

# Basic analysis
if fever.lower() == "yes":
    risk_score += 2

if cough.lower() == "yes":
    risk_score += 2

if headache.lower() == "yes":
    risk_score += 1

if tired.lower() == "yes":
    risk_score += 1

if sleep < 6:
    risk_score += 1

if water < 5:
    risk_score += 1

# Result
print("\n========== HEALTH ANALYSIS ==========\n")

if risk_score <= 2:
    print("Health Status: LOW RISK ✅")
    print("You seem mostly fine. Keep taking care of your health.")

elif risk_score <= 5:
    print("Health Status: MODERATE RISK ⚠️")
    print("Suggestions:")
    print("- Take proper rest")
    print("- Drink more water")
    print("- Avoid junk food")
    print("- Monitor your symptoms")

else:
    print("Health Status: HIGH RISK ❗")
    print("Important:")
    print("- Please consult a doctor")
    print("- Take proper rest")
    print("- Stay hydrated")
    print("- Do not ignore symptoms")

print("\nThank you for using AI Health Assistant!")
