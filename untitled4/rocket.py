y=100 # m
v=0   # m/s
a_Gravity=-10  # m/s^2
f=100 # L
thrusters = 0

input_thruster = input("thrusters(input 0to 20)")
#hi
if input_thruster > 20:
    print("Input 0 to 20")
    thrusters = 20

elif input_thruster < 0:
    print("Input 0 to 20")
    thrusters = 0

else:
    thrusters = input_thruster


a = a_Gravity + thrusters
#new_position = y + v + a*0.5
#new_velocity = v + acceleration

# if y is not 0
if y != 0:
    while 1:
        y = y + v + a * 0.5
        v = v + a
        f = f - thrusters

        print("Position" + str(y) + " ,Velocity" + str(v) + " ,Fuel" + str(f))

        # if y is 0, stop the programe
        if y <= 0 or v >= -3 :
            exit()

        elif f <= 0 and y > 0 :
            print("No fuel")
            exit()











