def fuction_a():
    print("aaaa")
    fuction_b()
    print("aaaa2")
    
def fuction_b():
    print("bbbb")
    fuction_c()
    print("bbbb2")

def fuction_c():
    print("cccc")
    print("cccc2")

fuction_a()