# 2019_07_11_IoT_Summer_2019

# const list
max_input_fuel = 20 # You have thrusters that can be powered from 0 to 20.
min_input_fuel = 0
max_acceleration = 10 # acceleration (minimum -10, maximum +10)
min_acceleration = -10
g_acceleration = -10 # gravity_acceleration
r_height = 100 # rocket_height
r_velocity = 0 # rocket_velocity ,initial velocity = 0
r_fuel = 100 # r_fuel
t_acceleration = 0 # total_acceleration

# trusters 0~20 (1 truster = 1 liter)

# customized functions
def show_rocket_status():
    print("rocket_height: " + str(r_height) + " / rocket_velocity: " + str(r_velocity) + " / rocket_fuel: " + str(r_fuel))

def give_power_to_thrusters(thrusters):
    old_fuel = r_fuel
    old_height = r_height
    old_velocity = r_velocity

    if (old_fuel - thrusters < 0):
        show_rocket_status()
        print ("the ship is in free-fall")
        exit()

    elif (thrusters >= min_input_fuel and thrusters <= max_input_fuel):
        new_fuel = old_fuel - thrusters
        acceleration = g_acceleration + thrusters
        new_position = old_height + old_velocity + acceleration * 0.5
        new_velocity = old_velocity + acceleration
        return new_fuel, acceleration, new_position, new_velocity

# main
while(1): # or while(r_height <= 0)
    show_rocket_status()
    while(1):
        thrusters = int(raw_input("Set thrusters(0-20): "))
        if (thrusters > max_input_fuel or thrusters < min_input_fuel):
            print ("Wrong thrusters input. plz re-enter.")
        else:
            break
    r_fuel, t_acceleration, r_height, r_velocity = give_power_to_thrusters(thrusters)

    if (r_height <= 0 and r_velocity <= 3 and r_velocity >= -3):
        show_rocket_status()
        print("Landing Successful !")
        exit()

    elif (r_height <= 0 and r_velocity < 3):
        show_rocket_status()
        print("the ship is in free-fall !")
        exit()

# if( while(r_height <= 0) --> result_message )