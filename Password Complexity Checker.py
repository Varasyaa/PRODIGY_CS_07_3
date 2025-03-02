import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")
    
    # Strength rating
    if strength == 5:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)
print(strength)
for tip in feedback:
    print("-", tip)
