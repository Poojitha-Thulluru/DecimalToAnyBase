def get_decimal_to_any_base(decimal_number: int, input_base: int) -> str:
    result = []
    while decimal_number > 0:
        remainder = decimal_number % input_base
        result.append(remainder)
        decimal_number //= input_base
    if not result:
        result.append(0)
    return ''.join(map(str, result[::-1]))


try:
    decimal_num = int(input("Enter the number : "))
    base = int(input("Enter base : "))
    print(f"The equivalent number in base {base} is : ", get_decimal_to_any_base(decimal_num, base))
except ValueError:
    print("Invalid input. Please enter only integers.")
