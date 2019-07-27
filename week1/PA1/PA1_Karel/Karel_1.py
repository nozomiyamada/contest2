from karel.functions1 import *
start()

####### DO NOT EDIT CODE ABOVE THIS LINE ########

def main():
    """
    Your code goes here! (do not forget indent(tab))
    """
    for i in range(7):
        for i in range(6):
            move()
            while on_beeper():
                pick_beeper()
        turn_left(); turn_left()
        for i in range(6):
            move()
            
        turn_right()
        if front_is_clear():
            move()
        turn_right()






####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)