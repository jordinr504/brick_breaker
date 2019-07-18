ball_x = 250 #ball 1 left and right
x_speed = 3 #ball 1 left 
ball_y = 100
y_speed = 3
ball_a = 0 #ball 2 up and down
a_speed = 1 #ball 2  up and down speed
ball_b = 250 #ball 2 left and right
b_speed = 0 #ball 2 left and right speed
showpowerup = False
showbrick1 = True
showbrick2 = True
showbrick3 = True
showbrick4 = True
showbrick5 = True
showbrick6 = True
showbrick7 = True
showbrick8 = True
showbrick9 = True
showbrick10 = True
showbrick11 = True
showbrick12 = True
showbrick13 = True
showbrick14 = True
showbrick15 = True
r = random(0,255)
g = random(0,255)
b = random(0,255)


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
    global showbrick6
    global showbrick7
    global showbrick8
    global showbrick9
    global showbrick10
    global showbrick11
    global showbrick12
    global showbrick13
    global showbrick14
    global showbrick15
    global r
    global g
    global b
    global ball_x
    global ball_y
    global x_speed
    global y_speed
    global ball_a
    global ball_b
    global a_speed
    global b_speed
    global showpowerup
    
    fill(r,g,b)
    ellipse(ball_x,ball_y, 30,30)
    
    fill(87,16,16)
    strokeWeight(2)
    #row 1
    if showbrick1 == True:
        rect(0,0,100,20)
    if showbrick2 == True:
        rect(100,0,100,20)


    if showbrick3 == True: #different color brick
        fill(r,g,b)
        rect(200,0,100,20)
        if ball_x > 200 and ball_x < 300 and ball_y > 0 and ball_y < 100:
            showpowerup = True
    if showpowerup ==True:
        ellipse(ball_b,ball_a,20,20)
        ball_a = ball_a + a_speed
        ball_b = ball_b + b_speed

        
    fill(87,16,16)
    strokeWeight(2)
    if showbrick4 == True:
        rect(300,0,100,20)
    if showbrick5 == True:
        rect(400,0,100,20)

#     #row 2
    if showbrick6 == True:
        rect(50,20,100,20)
    if showbrick7 == True:
        rect(150,20,100,20)
    if showbrick8 == True:
        rect(250,20,100,20)
    if showbrick9 == True:  
        rect(350,20,100,20)
        
#     #row 3
    if showbrick10 == True:
        rect(100,40,100,20)
    if showbrick11 == True:
        rect(200,40,100,20)
    if showbrick12 == True:
        rect(300,40,100,20)
    
#     #row 4
    if showbrick13 == True:
        rect(150,60,100,20)
    if showbrick14 == True:
        rect(250,60,100,20)
    
#     #row 5
    if showbrick15 == True:
        rect(200,80,100,20)

        
def draw():
    global ball_x
    global ball_y
    global x_speed
    global y_speed
    global ball_a
    global ball_b
    global a_speed
    global b_speed
    global showbrick1
    global showbrick2
    global showbrick3
    global showbrick4
    global showbrick5
    global showbrick6
    global showbrick7
    global showbrick8
    global showbrick9
    global showbrick10
    global showbrick11
    global showbrick12
    global showbrick13
    global showbrick14
    global showbrick15
    global r
    global g
    global b
    global showpowerup
    
    background(255,255,255)

    fill(255,0,0)
    if mouseX > 60 and mouseX < 440:
        rect(mouseX-60,400,130,22) #paddle
    elif mouseX < 60:  #make paddle not go off of the left side
        rect(0,400,130,22)
    elif mouseX > 440:  #make paddle not go off of the right side
        rect(390,400,130,22)
  
    
    ball_y = ball_y + y_speed 
    ball_x = ball_x + x_speed
    
    if ball_x > 490:
        x_speed = -1*x_speed
    elif ball_x < 10:
        x_speed = -1*x_speed
    elif ball_y < 10: #top of screen
        y_speed = -1*y_speed  
        
        
        #make ball bounce off of paddle
    if ball_y > 385 and ball_y < 400 and ball_x > mouseX-60 and ball_x < mouseX+60:
        y_speed = -1.5*y_speed
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
        
    if ball_a > 385 and ball_a < 400 and ball_b > mouseX-60 and ball_x < mouseX+60:
        showpowerup = False
        
        
    if y_speed < -6:
        y_speed = -6
        
        #top row
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
        
        #second row from top
    if ball_x > 50 and ball_x < 150 and ball_y > 20 and ball_y < 40:
        showbrick6 = False
    if ball_x > 150 and ball_x < 250 and ball_y > 20 and ball_y < 40:
        showbrick7 = False
    if ball_x > 250 and ball_x < 350 and ball_y > 20 and ball_y < 40:
        showbrick8= False
    if ball_x > 350 and ball_x < 450 and ball_y > 20 and ball_y < 40:
        showbrick9 = False
        
        #third row from top
    if ball_x > 100 and ball_x < 200 and ball_y > 40 and ball_y < 60:
        showbrick10 = False
    if ball_x > 200 and ball_x < 300 and ball_y > 40 and ball_y < 60:
        showbrick11= False
    if ball_x > 300 and ball_x < 400 and ball_y > 40 and ball_y < 60:
        showbrick12 = False
        
        #second row from bottom
    if ball_x > 150 and ball_x < 250 and ball_y > 60 and ball_y < 80:
        showbrick13 = False
    if ball_x > 250 and ball_x < 350 and ball_y > 60 and ball_y < 80:
        showbrick14 = False
    
        #bottom row
    if ball_x > 200 and ball_x < 300 and ball_y > 80 and ball_y < 100:
        showbrick15 = False
        
    createGame()    
