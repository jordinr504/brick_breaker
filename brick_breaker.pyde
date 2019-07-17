ball_x = 250
x_speed = 3
ball_y = 100
y_speed = 3
showbrick1 = True
showbrick2 = True
showbrick3 = True
showbrick4 = True
showbrick5 = True

def setup():
    size(500,500)
    background(255,255,255)
    createGame()



def createGame():
    global showbrick1
    global showbrick2
    global showbrick3
    global showbrick4
    global showbrick5
    
    ellipse(ball_x,ball_y, 30,30)
    
    #row 1 from top
    fill(255,255,255)
    if showbrick1 == True:
        rect(0,0,100,20)
    if showbrick2 == True:
        rect(100,0,100,20)
    if showbrick3 == True:
        rect(200,0,100,20)
    if showbrick4 == True:
        rect(300,0,100,20)
    if showbrick5 == True:
        rect(400,0,100,20)

#     #row 2
#     rect(50,20,100,20)
#     rect(150,20,100,20)
#     rect(250,20,100,20)
#     rect(350,20,100,20)
#     #row 3
#     rect(100,40,100,20)
#     rect(200,40,100,20)
#     rect(300,40,100,20)
#     #row 4
#     rect(150,60,100,20)
#     rect(250,60,100,20)
#     #row 5
#     rect(200,80,100,20)

        
def draw():
    global ball_x
    global ball_y
    global x_speed
    global y_speed
    global showbrick1
    global showbrick2
    global showbrick3
    global showbrick4
    global showbrick5
    
    background(255,255,255)

    if mouseX > 60 and mouseX < 440:
        fill(255,255,255)
        rect(mouseX-60,400,120,15)
    elif mouseX < 60:  #make paddle not go off of the left side
        rect(0,400,120,15)
    elif mouseX > 440:  #make paddle not go off of the right side
        rect(390,400,120,15)
  
    
    ball_y = ball_y + y_speed 
    ball_x = ball_x + x_speed
    
    if ball_x > 490:
        x_speed = -3
    elif ball_x < 10:
        x_speed = 3
        
        #make ball bounce off of paddle
    if ball_y > 385 and ball_y < 400 and ball_x > mouseX-60 and ball_x < mouseX+60:
        y_speed = -3
    elif ball_y < 10:
        y_speed = 3   
    if ball_x > 0 and ball_x < 100 and ball_y < 20:
        showbrick1 = False
    if ball_x > 100 and ball_x < 200 and ball_y < 20:
        showbrick2 = False
    if ball_x > 200 and ball_x < 300 and ball_y < 20:
        showbrick3 = False
    if ball_x > 300 and ball_x < 400 and ball_y < 20:    
        showbrick4 = False
    if ball_x > 400 and ball_x < 500 and ball_y < 20:
        showbrick5 = False
        
    
    createGame()    
