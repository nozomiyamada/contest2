from karel.functions2 import *
start() 

####### DO NOT EDIT CODE ABOVE THIS LINE ########

def main():
    """
    Your code goes here! (do not forget indent(tab))
    """
    turn_left()
    for i in range(9):
        while front_is_clear():
            move()
            while on_beeper():
                pick_beeper()
        turn_right()






####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)