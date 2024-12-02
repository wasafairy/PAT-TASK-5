def check_elements_type(a):
    for a in a:
        if type(a) == int :
            print (a, "is an integer")
        elif type(a) == str :
            print (a, "is a string")
        else :
            print("neither integer or string")


list_a=["hello", 12, 45, 48, 36, 65, "bye"]
result=check_elements_type(list_a)
