import random
import string
from checker import check_password_strength

# get the number of letters, digits and special characters in the passcode
while True:
    letters_count = int(input('Enter the number of letters in the passcode: '))
    digits_count = int(input('Enter the number of digits in the passcode: '))
    special_count = int(input('Enter the number of special characters in the passcode: '))
    if letters_count + digits_count + special_count < 6 or letters_count + digits_count + special_count >= 15:
        print('The total number of characters in the passcode should be at least 6')
        continue
    break

letter_chars = input('Enter the letters you want to use in the passcode, if you dont want any letters keep it blank: ')

# get the passcode
def get_string(letters_count, digits_count, special_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    specials = ''.join((random.choice(string.punctuation) for i in range(special_count)))
    if letter_chars:
        letters = letter_chars
        sample_list = list(digits + specials)
        random.shuffle(sample_list)
        sample_list.insert(random.randint(0, len(sample_list)), letters)
    else:
        sample_list = list(letters + digits + specials)
        random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    print('Random string with', letters_count, 'letters', digits_count, 'digits', 'and', special_count, 'special characters is:', final_string)
    return final_string

passcode = get_string(letters_count, digits_count, special_count)

# Ask the user if they want to check the password strength
check_strength = input('Do you want to check the password strength? (yes/no): ').strip().lower()
if check_strength == 'yes':
    strength = check_password_strength(passcode)
    for item in strength:
        print(item)