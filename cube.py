#volume of a cube

#h = height
#l = length
#w = width

while True:
    try:
        h = float(input("enter height: "))
        if h < 0:
            while True:
                h = float(input("invalid number, enter height: "))
                if h < 0:
                    True
                else:
                    break
        l = float(input("enter lenght: "))
        if l < 0:
            while True:
                l = float(input("invalid number, enter length: "))
                if l < 0:
                    True
                else:
                    break
        w = float(input("enter width: "))
        if w < 0:
            while True:
                w = float(input("invalid number, enter length: "))
                if w < 0:
                    True
                else:
                    break
        break
    except ValueError:
        print("invalid number, only positive numbers.")


volume = h*l*w

print("volume of cube = "+str(volume))
