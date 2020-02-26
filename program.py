#Cos,tan,
import math
leg = input("Small leg number : ")
l_leg = input("Long leg number : ")
hypot = input("Hypothenuse number : ")
if leg == "x":
    leg = "x"
elif leg == "r":
#    leg = input("short leg : ")
    leg = "r"
else:
    leg = int(leg)
if l_leg == "x":
    int(leg)
    int(hypot)
    y = ((int(hypot) * int(hypot)) - (int(leg) * int(leg)))
    l_leg = math.sqrt(y)
elif l_leg == "r":
    l_leg = "r"
#        hypot = math.sqrt(hypot)
else:
    l_leg = int(l_leg)
if hypot == "x":
    if leg == "r":
        leg = input("Short leg number thats under the radical : ")
        hypot = (int(leg) + (l_leg * l_leg))
    else:
        hypot = ((leg * leg) + (l_leg * l_leg))
        hypot = math.sqrt(hypot)
#    hypot = "x"
elif hypot == "r":
    hypot = "r"
else:
    hypot = int(hypot)
cos_s_tan = input("What sign are you using s/c/t : ")
cos_s_tan = cos_s_tan.lower()
#Cos
if cos_s_tan == "c":
#    leg = input("")
    if hypot == "r":
        if leg == "r":
            hypo = input("Hypotenuse number thats under the radical : ")
            left = input("Long leg number thats under the radical : ")
            hypot = hypo
            leg = (int(hypot) * int(left))
            leg1 = math.sqrt(leg)
            small_ang = (leg1/hypot)
            print(str(leg1) + " / " + str(hypot))
            print(small_ang)
        else:
            placeholder = ("It is 7:50")
    else:
        placeholder = ("Depression")
    small_ang = (leg/hypot)
    print(str(leg) + " / " + str(hypot))
    print(small_ang)
#Sin
elif cos_s_tan == "s":
#    if hypot == "x":
#        hypot = ((leg * leg) + (l_leg * l_leg))
#        hypot = math.sqrt(hypot)
#    else:
#        placeholder = 2
    if hypot == "r":
        if l_leg == "r":
            hypo = input("Hypotenuse number thats under the radical : ")
            left = input("Long leg number thats under the radical : ")
            hypot = hypo
            l_leg = (int(hypot) * int(left))
            l_leg1 = math.sqrt(l_leg)
            print(str(l_leg1) + " / " + str(hypot))
        else:
            placeholder = ("Tyty is the best")
    print(str(l_leg) + " / " + str(hypot))
    print(l_leg/hypot)
if cos_s_tan == "t":
    if leg == "r":
        leg = input("Little leg without radical = ")
        leg = int(leg)
        if l_leg == "r":
            l_leg = input("Long leg without radical = ")
            l_leg = (int(l_leg) * leg)
        else:
            print(str(l_leg) + " |" + str(leg) + " / " + str(leg))    
            placeholder = 12
    else:
        placeholder = 0
        print("Short leg/Long leg")
        print(str(leg) + " / " + str(l_leg))
        print(leg/l_leg)
else:
    placeholder = "A placeholder is what a placeholder is."
