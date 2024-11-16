import re
import string

common_passwords = [
    "password123", "123456", "qwerty", "12345678", "letmein", "admin", 
    "welcome", "12345", "password1", "abc123", "1234", "iloveyou", 
    "sunshine", "football", "123123", "monkey", "dragon", "qwertyuiop", 
    "123qwe", "password", "1q2w3e4r", "123321", "letmein", "welcome123"
]

password = input("Enter your password: ")

def check_password_strength(password):
    strength_feedback = []
    
    if len(password) < 12:
        strength_feedback.append("Password is too short. It should be at least 12 characters long.")
    elif len(password) > 16:
        strength_feedback.append("Password length is good (16+ characters).")
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not has_upper:
        strength_feedback.append("Password should include at least one uppercase letter.")
    if not has_lower:
        strength_feedback.append("Password should include at least one lowercase letter.")
    if not has_digit:
        strength_feedback.append("Password should include at least one digit.")
    if not has_special:
        strength_feedback.append("Password should include at least one special character (e.g., !, @, #, $, %).")
    
    if password.lower() in common_passwords:
        strength_feedback.append("Password is too common. Please choose a more unique password.")
    
    dictionary_words = ["password", "123456", "qwerty", "letmein", "football", "sunshine"]
    if any(word in password.lower() for word in dictionary_words):
        strength_feedback.append("Password contains common dictionary words or patterns.")
    

    username = "user_example" 
    if username.lower() in password.lower():
        strength_feedback.append(f"Password should not contain your username or parts of it.")
    
    if re.search(r'(.)\1{2,}', password):
        strength_feedback.append("Password contains repeating characters. Avoid repeating sequences.")
    if re.search(r'(\d{3,})', password):  
        strength_feedback.append("Password contains a number sequence. Avoid using sequences like 12345.")
    if re.search(r'(abc|xyz|qwerty|asdf)', password.lower()):
        strength_feedback.append("Password contains a predictable sequence (e.g., abc, qwerty).")
    
    if len(strength_feedback) == 0:
        strength_feedback.append("Password is strong and meets security requirements.")
    
    return strength_feedback

feedback = check_password_strength(password)

for item in feedback:
    print(item)