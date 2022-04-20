def m(s):
    s_split=s.split("-")
    final_s="("
    final_s+=s_split[0].strip()
    final_s+=") "
    final_s=final_s+s_split[1].strip()+"-"+s_split[2].strip()
    return final_s
print(m("555-666-1110"))