attempts = 0
valid = 0
invalid = 0

while True:
    password = input("Enter password (quit to stop): ").strip()

    if password == "quit":
        break

    attempts += 1

    has_upper = 0
    has_lower = 0
    has_digit = 0
    long_enough = 0

    if len(password) >= 8:
        long_enough = 1

    for ch in password:
        if 'A' <= ch <= 'Z':
            has_upper = 1
        elif 'a' <= ch <= 'z':
            has_lower = 1
        elif '0' <= ch <= '9':
            has_digit = 1

    print("Password: ********")

    if long_enough == 1 and has_upper == 1 and has_lower == 1 and has_digit == 1:
        print("Result: VALID")
        print("Missing: none")
        valid += 1
    else:
        print("Result: INVALID")
        missing = ""

        if long_enough == 0:
            missing += "length"
        if has_upper == 0:
            if missing != "":
                missing += ", "
            missing += "uppercase"
        if has_lower == 0:
            if missing != "":
                missing += ", "
            missing += "lowercase"
        if has_digit == 0:
            if missing != "":
                missing += ", "
            missing += "digit"

        print("Missing:", missing)
        invalid += 1

    print("----------------")

print("\nSummary")
print("Total attempts:", attempts)
print("Valid:", valid)
print("Invalid:", invalid)
