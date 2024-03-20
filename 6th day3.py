def is_mirror_number(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    reversed_number = int(reversed_str)
    return number == reversed_number
number_to_check = int(input("Enter the number: "))
if is_mirror_number(number_to_check):
    print(f"{number_to_check} is a mirror number.")
else:
    print(f"{number_to_check} is not a mirror number.")
