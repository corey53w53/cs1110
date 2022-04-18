def make_netid(name,n):
    first_space=name.find(" ")
    second_space=name.rfind(" ")
    first_name=name[:first_space].lower()
    last_name=name[second_space+1:].lower()
    if first_space==second_space:
        return first_name[0]+last_name[0]+str(n)
    else:
        middle_name = name[first_space+1:second_space].lower()
        return first_name[0]+middle_name[0]+last_name[0]+str(n)
print(make_netid("Corey Wang",233))
print(make_netid("Corey Li Wang",200))