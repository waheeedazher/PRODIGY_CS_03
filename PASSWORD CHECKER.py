print("***PASSWORD CHECKER***")
import re

# Function to assess password strength
def assess_password_strength(password):
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Feedback for each criterion
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*()).")
    
    # Overall strength assessment
    strength = 0
    if length_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1
    
    # Provide overall feedback based on strength
    if strength == 5:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password.", feedback

# Main Program to get user input and assess password
def main():
    password = input("Enter your password to check its strength: ")
    strength, feedback = assess_password_strength(password)
    
    print("\nPassword Strength:", strength)
    
    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print("-", item)
    else:
        print("Your password is strong and meets all criteria!")

if __name__ == "__main__":
    main()
