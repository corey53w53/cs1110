def make_netid(name,n):
    nl=name.split()
    s=""
    for name in nl:
        s+=name[0].lower()
    print(s+str(n))
    return s+str(n)
make_netid("Corey Wang",233)
make_netid("Corey Li Wang",200)