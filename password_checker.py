import re

# List of common weak passwords
common_passwords = ["123456", "password", "qwerty", "admin", "hello123"]

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 8 characters")

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number")

    # Special character check
    if re.search(r'[!@#$%^&*(){}|<>?]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character")

    # Common password check
    if password.lower() in common_passwords:
        suggestions.append("Avoid using common passwords")
        score = 1

    # Strength rating
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions


# User input
password = input("Enter your password: ")

# Function call
strength, suggestions = check_password_strength(password)

# Output
print(f"\nPassword Strength: {strength}")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("Your password is secure!")