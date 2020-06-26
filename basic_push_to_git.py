

def proper(string_v):
    string_v = string_v.lower()
    string_v = string_v[0].upper() + string_v[1:]
    return(string_v)



def function():
    a = []
    while True:
        val = input("Say something:")

        if val == "\end":
            print(" ".join(a))
            break
                       
        else:
            if "how" in val:
                val = proper(val)+"?"
            else:
                val = proper(val)+"."
        a.append(val)











