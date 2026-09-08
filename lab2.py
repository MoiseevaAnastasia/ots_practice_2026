import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5 

    if state == "INIT":
        
        state = "RIGHT"
        t.setheading(0)  # Разворот вправо
        return state, turn

    elif state == "RIGHT":
        t.forward(10) # Перемещение
        x = round(t.position()[0] / 10)
        y = round(t.position()[1] / 10)
        
        
        if x >= turn:
            state = "UP"
            t.setheading(90)  # Разворот вверх
            return state, turn
        return state, turn

    elif state == "UP":
        t.forward(10)  # Перемещение
        
        x = round(t.position()[0] / 10)
        y = round(t.position()[1] / 10)
        
        
        if y >= turn + 1: 
            if turn % 2 == 1:  
                state = "LEFT"
                t.setheading(180)  # Разворот влево
            else:  
                state = "RIGHT"
                t.setheading(0)  # Разворот вправо
            turn = turn + 1  # Начало нового витка
            return state, turn
        return state, turn

    elif state == "LEFT":
        t.forward(10)  # Движемся влево
        
        x = round(t.position()[0] / 10)
        y = round(t.position()[1] / 10)
        
        if x <= -turn:
            state = "UP"
            t.setheading(90)  # Разворот вверх
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)  
    turn = 1  

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if __name__ == "__main__":
    draw()
