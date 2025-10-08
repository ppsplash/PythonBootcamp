def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")
length = len(formatted_name)
print(formatted_name)


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap_year(2000))
print(is_leap_year(2020))
print(is_leap_year(2024))
print(is_leap_year(2400))
print(is_leap_year(1700))
print(is_leap_year(1989))
print(is_leap_year(2100))
