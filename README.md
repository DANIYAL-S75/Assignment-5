# Assignment-5

Password Policy and Strength Validator
This program evaluates a password's security level based on predefined organizational policies. It categorizes passwords into four strength levels and determines if they are acceptable for use.
📋 Features
The validator checks passwords against five key policies:
Length: Must be between 8 and 14 characters.
Casing: Must contain both upper-case and lower-case letters.
Numerics: Must contain one or more numerical digits.
Special Characters: Must contain special characters (e.g., @, #, $).
Forbidden Words: Must not contain common strings like password, 12345, qwerty, admin, or username.
💪 Strength Levels
The program returns a strength label based on the following criteria:
Strength	Criteria	Accepted?
Strong	Contains at least 2 of each: Upper-case, Lower-case, Digits, and Special characters.	✅ Yes
High	Contains at least 1 of each type, and at least 2 characters of any one type.	✅ Yes
Moderate	Contains at least 1 of each character type.	❌ No
Weak	Fails to meet the above criteria or violates Length/Forbidden word policies.	❌ No
Note: Only passwords with High or Strong ratings return a boolean value of True (Accepted).
🚀 How to Use
Ensure Python is installed on your system.
Download the script password_validator.py.
Run the script via your terminal or IDE:
bash
python password_validator.py
Use code with caution.

Example Input/Output
If the input is Ab1@Cd2#:
Strength: Strong
Accepted: True
If the input is pass123:
Strength: Weak (Violates forbidden word policy)
Accepted: False
Would you like me to add a "Testing" section to the README with more sample passwords and their expected results?
