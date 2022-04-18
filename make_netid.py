def make_netid(name,n):
    string=""
    a=[s[0].lower() for s in name.split()]
    for b in a:
        string+=b
    string+=str(n)
    print(string)

make_netid("Corey Wang",233)
make_netid("Corey Li Wang",200)