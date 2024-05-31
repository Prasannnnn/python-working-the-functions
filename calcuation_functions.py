####Cal
def caluculator_area (section):
  section=section.lower()

  if section == "add":

    add_section = a+b
    print(f"the {section} operator is {add_section}")
  elif section == "sub":

    sub_section = a-b
    print(f"the {section} operator is {sub_section}")
  elif section == "mult":

    mult_section = a*b
    print(f"the {section} operator is {mult_section}")
  elif section == "div":

    div_section = a/b
    print(f"the {section} operator is {div_section}")

  else:
    print("the section is invalid")

if __name__ == "__main__":
    a=float(input("enter the input:"))
    b=float(input("enter the input:"))
    print("which section you want")
    section_name = input("enter the section :")
    caluculator_area(section_name)