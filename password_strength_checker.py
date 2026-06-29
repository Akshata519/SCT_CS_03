import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Display result
    print("\nPassword Strength Result")

    if score == 5:
        print("Strength: Very Strong")
    elif score == 4:
        print("Strength: Strong")
    elif score == 3:
        print("Strength: Medium")
    elif score == 2:
        print("Strength: Weak")
    else:
        print("Strength: Very Weak")

    # Suggestions
    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)
    else:
        print("Excellent! Your password meets all security requirements.")

# Main Program
print("===== Password Strength Checker =====")

password = input("Enter your password: ")

check_password_strength(password)
