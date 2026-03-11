import string

def validate_password(password):
    # --- Policy Checks ---
    
    # Policy 1: Length check (8 to 14 characters)
    length_ok = 8 <= len(password) <= 14
    
    # Policy 5: Banned words check
    banned = ["password", "12345", "qwerty", "admin", "username"]
    contains_banned = any(word in password.lower() for word in banned)
    
    # If it fails Policy 1 or Policy 5, it is automatically Weak and Rejected
    if not length_ok or contains_banned:
        return "Weak", False

    # Character counts for Policies 2, 3, and 4
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digit = sum(1 for c in password if c.isdigit())
    special = sum(1 for c in password if c in string.punctuation or c in "@#$")

    # --- Strength Determination ---
    
    # Strong: min 2 characters each
    if upper >= 2 and lower >= 2 and digit >= 2 and special >= 2:
        strength = "Strong"
    
    # High: min 1 each AND at least one category has 2 or more
    elif (upper >= 1 and lower >= 1 and digit >= 1 and special >= 1) and \
         (upper >= 2 or lower >= 2 or digit >= 2 or special >= 2):
        strength = "High"
    
    # Moderate: min 1 character each
    elif upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
        strength = "Moderate"
    
    # Weak: Does not meet the "Moderate" requirements
    else:
        strength = "Weak"

    # --- Acceptance Logic ---
    # Only "High" and "Strong" are accepted
    is_accepted = strength in ["High", "Strong"]

    return strength, is_accepted

# --- Example Testing ---
test_passwords = ["Ab1#Ab1#", "Ab1#cdef", "Ab1#", "password123", "Admin@123"]

print(f"{'Password':<15} | {'Strength':<10} | {'Accepted'}")
print("-" * 40)
for p in test_passwords:
    str_val, acc_val = validate_password(p)
    print(f"{p:<15} | {str_val:<10} | {acc_val}")
