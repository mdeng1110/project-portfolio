# age: int
# name: str
# height: float

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "They can drive"

if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")