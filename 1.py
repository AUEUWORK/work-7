income = float(input("กรุณาระบุรายได้ของคุณ: "))

if income >= 15000 and income < 20000:
    card_type = "บัตร Sliver"
elif income < 100000:
    card_type = "บัตร Gold"
else:
    card_type = "บัตร Platinum"

print(f"คุณสามารถทำ{card_type}ได้")
