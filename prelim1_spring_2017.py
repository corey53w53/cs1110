# def m(s):
#     s_split=s.split("-")
#     final_s="("
#     final_s+=s_split[0].strip()
#     final_s+=") "
#     final_s=final_s+s_split[1].strip()+"-"+s_split[2].strip()
#     return final_s
# print(m("555-666-1110"))

def glue(name1,stop1,name2,stop2):
    if len(name1)<=stop1 or len(name2)<=stop2:
        return -1
    s1=name1[:stop1+1]
    s2=name2[stop2:]
    return s1+s2
print(glue("jules",5,"vincent",4))