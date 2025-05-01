valid_user = {
    "name": "Elizabeth",
    "email": "validuser@example.com",
    "phone_number": "7778889999",
    "password": "Password123",
    "password_confirmation": "Password123"
}

invalid_user_register_case_1 = {
    "name": "Elizabeth",
    "email": "test@example.com",  # already taken
    "phone_number": "11111111111",  # invalid
    "password": "Pasdqwd2assword1",
    "password_confirmation": "Pwdqwq21dassword"  # mismatch
}

passwords_test_cases = [
    {
        "password": "ar20077",  # Less than 8 characters
        "error": "The password field must be at least 8 characters."
    },
    {
        "password": "ar200778",  # No uppercase
        "error": "The password field must contain at least one uppercase and one lowercase letter."
    },
    {
        "password": "ARWWWWWW",  # No lowercase
        "error": "The password field must contain at least one uppercase and one lowercase letter."
    },
    {
        "password": "ArWWWWWW",  # No number
        "error": "The password field must contain at least one number."
    }
]
