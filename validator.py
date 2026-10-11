import re

# Pattern for an email like name@example.com
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def is_valid_email(text):
    return re.fullmatch(EMAIL_PATTERN, text) is not None


def is_valid_phone(text):
    """A phone number is exactly 10 digits."""
    return re.fullmatch(r"\d{10}", text) is not None


def is_strong_password(text):
    """At least 8 characters, with upper, lower, digit and symbol."""
    if len(text) < 8:
        return False
    has_upper = re.search(r"[A-Z]", text)
    has_lower = re.search(r"[a-z]", text)
    has_digit = re.search(r"\d", text)
    has_symbol = re.search(r"[^A-Za-z0-9]", text)
    return bool(has_upper and has_lower and has_digit and has_symbol)


def is_valid_ip(text):
    """IPv4 like 192.168.1.1, where each part is 0-255."""
    if not re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", text):
        return False
    for part in text.split("."):
        if int(part) > 255:
            return False
    return True


def email_suggestions(text):
    """Return tips that explain why an email is invalid."""
    tips = []
    if " " in text:
        tips.append("Remove the spaces.")
    if text.count("@") == 0:
        tips.append("Add an @ symbol, like name@example.com.")
    elif text.count("@") > 1:
        tips.append("Use only one @ symbol.")
    else:
        name, domain = text.split("@")
        if not name:
            tips.append("Add a name before the @.")
        if "." not in domain:
            tips.append("Add a domain ending after the @, like example.com.")
        elif not re.search(r"\.[A-Za-z]{2,}$", domain):
            tips.append("End the email with a real ending, like .com or .in.")
    if not tips:
        tips.append("Check the format: name@example.com")
    return tips


def password_suggestions(text):
    """Return tips to make a password stronger."""
    tips = []
    if len(text) < 8:
        tips.append("Use at least 8 characters.")
    if not re.search(r"[A-Z]", text):
        tips.append("Add an uppercase letter (A-Z).")
    if not re.search(r"[a-z]", text):
        tips.append("Add a lowercase letter (a-z).")
    if not re.search(r"\d", text):
        tips.append("Add a number (0-9).")
    if not re.search(r"[^A-Za-z0-9]", text):
        tips.append("Add a symbol like ! @ # $.")
    return tips


CHECKS = {
    "1": ("Email", is_valid_email),
    "2": ("Phone number", is_valid_phone),
    "3": ("Password", is_strong_password),
    "4": ("IP address", is_valid_ip),
}


def main():
    while True:
        print("\n1) Email  2) Phone  3) Password  4) IP address  q) Quit")
        choice = input("Choose what to check: ").strip().lower()
        if choice == "q":
            break
        if choice not in CHECKS:
            print("Please choose 1, 2, 3, 4 or q.")
            continue
        name, check = CHECKS[choice]
        value = input(f"Enter {name.lower()}: ").strip()
        is_ok = check(value)

        if choice == "3":                                # password: Strong / Weak
            print("Strong password" if is_ok else "Weak password")
        else:
            print(f"Valid {name.lower()}" if is_ok else f"Invalid {name.lower()}")

        if choice == "1" and not is_ok:                  # email tips
            for tip in email_suggestions(value):
                print(" - Tip:", tip)
        elif choice == "3":                              # password tips
            if not is_ok:
                for tip in password_suggestions(value):
                    print(" - Tip:", tip)
            elif len(value) < 12:
                print(" - Tip: 12 or more characters is even safer.")


if __name__ == "__main__":
    main()