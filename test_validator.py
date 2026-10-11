from validator import (is_valid_email, is_valid_phone, is_strong_password,is_valid_ip, email_suggestions, password_suggestions)

assert is_valid_email("user@example.com") is True
assert is_valid_email("first.last+tag@mail.co.in") is True
assert is_valid_email("user@@example.com") is False
assert is_valid_email("user@example") is False

assert is_valid_phone("9876543210") is True
assert is_valid_phone("98765") is False
assert is_valid_phone("98765abcde") is False

assert is_strong_password("Str0ng!Pass") is True
assert is_strong_password("weakpass") is False
assert is_strong_password("Short1!") is False
assert is_strong_password("NoDigits!!") is False
assert is_strong_password("alllower1!") is False

assert is_valid_ip("192.168.1.1") is True
assert is_valid_ip("256.1.1.1") is False
assert is_valid_ip("1.2.3") is False
assert is_valid_ip("abc.def.ghi.jkl") is False

assert "Use only one @ symbol." in email_suggestions("user@@example.com")
assert "Add an @ symbol, like name@example.com." in email_suggestions("userexample.com")
assert password_suggestions("Str0ng!Pass") == []
assert "Add a number (0-9)." in password_suggestions("NoDigits!!")
assert "Use at least 8 characters." in password_suggestions("Ab1!")

print("All tests passed")