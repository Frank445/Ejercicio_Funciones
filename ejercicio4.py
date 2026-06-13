c = float(input("Ingrese los °C: "))
def c_a_f(c):
    return(c * 9/5)+32
temp = c_a_f(c)
print("°F->",temp)