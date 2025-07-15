def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "User did not provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Name: {formated_f_name} {formated_l_name}"


print(format_name(input("Please enter your first name: "),input("Please enter your last name: ")))
