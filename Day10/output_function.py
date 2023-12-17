def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"

# f_name = input("Enter your first name: ")
# l_name = input("Enter your last name: ")
    
p_name = format_name("amalesh", "AMaleShkK")

print(p_name)