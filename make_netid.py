def make_netid(name,n): return "".join([a[0].lower() for a in name.split()])+str(n)
print(make_netid("Corey Wang",233))
print(make_netid("Corey Li Wang",200))