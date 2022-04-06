import string

def password_strenght(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    if len(value) < 8:
        return "Too Weak"
    if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
        return "Weak"
    if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
        return "Very Good"
    if (any(e in digits for e in value) and any(e in lowers for e in value)) or (
            any(e in digits for e in value) and any(e in uppers for e in value)) or (
            any(e in lowers for e in value) and any(e in uppers for e in value)):
        return "Good"

if __name__ == '__main__':
    assert password_strenght('') == "Too Weak"
    assert password_strenght('1234567') == "Too Weak"
    assert password_strenght('qwertyu') == "Too Weak"
    assert password_strenght('QWERTYU') == "Too Weak"
    assert password_strenght('QAaa1') == "Too Weak"
    assert password_strenght('12345678') == "Weak"
    assert password_strenght('qwertyui') == "Weak"
    assert password_strenght('QWERTYUI') == "Weak"
    assert password_strenght('QWERTYUIOPA') == "Weak"
    assert password_strenght('1234qwer') == "Good"
    assert password_strenght('1234QWER') == "Good"
    assert password_strenght('qwerQWER') == "Good"
    assert password_strenght('qwerQWERTYUI') == "Good"
    assert password_strenght('123qwerQWER') == "Very Good"
    assert password_strenght('1234456Qw') == "Very Good"
    assert password_strenght('qwertyQ1') == "Very Good"
    assert password_strenght('QWERTTYq1') == "Very Good"










