ball_x = 250 #ball 1 left and right
x_speed = 2 #ball 1 left 
ball_y = 100
y_speed = 2
ball_a = 40 #ball 2 up and down
a_speed = 1 #ball 2  up and down speed
ball_b = 340 #ball 2 left and right
b_speed = 0 #ball 2 left and right speed
showpowerup = False
paddle_width = 130
scoreboard = 0
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
    global scoreboard
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
    global paddle_width
    global scoreboard

    
    fill(r,g,b)
    ellipse(ball_x,ball_y, 30,30) #ball
    
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
    #     if ball_x > 200 and ball_x < 300 and ball_y > 0 and ball_y < 35:
    #         showpowerup = True
    # if showpowerup ==True:
    #     ellipse(ball_b,ball_a,20,20)
    #     ball_a = ball_a + a_speed
    #     ball_b = ball_b + b_speed

        
    fill(87,16,16)
    strokeWeight(2)
    if showbrick4 == True:
        rect(300,0,100,20)
    if showbrick5 == True:
        rect(400,0,100,20)

#     #row 2
    
    if showbrick6 == True: #different color brick
        fill(b,r,g)
        rect(50,20,100,20)
        
    fill(87,16,16)   
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
        
        
    if showbrick12 == True: #different color brick 
        fill(b,g,r)
        rect(300,40,100,20)
        if ball_x > 300 and ball_x < 400 and ball_y > 55 and ball_y < 75:
            showpowerup = True
    if showpowerup ==True:
        ellipse(ball_b,ball_a,20,20)
        ball_a = ball_a + a_speed
        ball_b = ball_b + b_speed
    
#     #row 4
    fill(87,16,16)
    if showbrick13 == True:
        rect(150,60,100,20)
    if showbrick14 == True:
        rect(250,60,100,20)
    
#     #row 5
    if showbrick15 == True:
        rect(200,80,100,20)


def createGame2():
    background(0,0,0)
       
        
         
          
           
            
             
               
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
    global paddle_width
    global scoreboard
    
    
    background(255,255,255)

    fill(255,0,0)
    if mouseX > 60 and mouseX < 440:
        rect(mouseX-60,400,paddle_width,22) #paddle
    elif mouseX < 60:  #make paddle not go off of the left side
        rect(0,400,paddle_width,22)
    elif mouseX > 440:  #make paddle not go off of the right side
        rect(390,400,paddle_width,22)
  
    
    ball_y = ball_y + y_speed #speed of ball
    ball_x = ball_x + x_speed
    
    if ball_x > 490:
        x_speed = -1*x_speed
    elif ball_x < 10:
        x_speed = -1*x_speed
    elif ball_y < 10: #top of screen
        y_speed = -1*y_speed  
        
        
        
        #make ball bounce off of paddle
    if ball_y > 385 and ball_y < 400 and ball_x > mouseX-paddle_width/2 and ball_x < mouseX+paddle_width/2:
        y_speed = -1.5*y_speed
        r = random(0,255)
        g = random(0,255)
        b = random(0,255)
        
        #make powerup disappear when it hits paddle
    if ball_a > 385 and ball_a < 400 and ball_b > mouseX-paddle_width/2 and ball_b < mouseX+paddle_width/2 and showpowerup == True: #only happens once
        showpowerup = False
        paddle_width = paddle_width+25
        
        
    if y_speed < -6:
        y_speed = -6
        
        #top row
    if ball_x > 0 and ball_x < 100 and ball_y < 20 and showbrick1 == True:
        showbrick1 = False
        scoreboard = scoreboard + 50
        y_speed = -1*y_speed
    if ball_x > 100 and ball_x < 200 and ball_y < 20 and showbrick2 == True:
        showbrick2 = False
        scoreboard = scoreboard + 50
        y_speed = -1*y_speed
        
        #different color brick
    if ball_x > 200 and ball_x < 300 and ball_y < 20 and showbrick3 == True:
        showbrick3 = False
        scoreboard = scoreboard + 100
        y_speed = -1*y_speed
        
        
    if ball_x > 300 and ball_x < 400 and ball_y < 20 and showbrick4 == True:    
        showbrick4 = False
        scoreboard = scoreboard + 50
        y_speed = -1*y_speed
    if ball_x > 400 and ball_x < 500 and ball_y < 20 and showbrick5 == True:
        showbrick5 = False
        scoreboard = scoreboard + 50
        y_speed = -1*y_speed
        
        #second row from top
        
        #different color brick
    if ball_x > 50 and ball_x < 150 and ball_y > 20 and ball_y < 40 and showbrick6 == True:
        showbrick6 = False
        scoreboard = scoreboard + 60
        y_speed = -1*y_speed
        
        
    if ball_x > 150 and ball_x < 250 and ball_y > 20 and ball_y < 40 and showbrick7 == True:
        showbrick7 = False
        scoreboard = scoreboard + 40
        y_speed = -1*y_speed
    if ball_x > 250 and ball_x < 350 and ball_y > 20 and ball_y < 40 and showbrick8 == True:
        showbrick8= False
        scoreboard = scoreboard + 40
        y_speed = -1*y_speed
    if ball_x > 350 and ball_x < 450 and ball_y > 20 and ball_y < 40 and showbrick9 == True:
        showbrick9 = False
        scoreboard = scoreboard + 40
        y_speed = -1*y_speed
        
        #third row from top
    if ball_x > 100 and ball_x < 200 and ball_y > 40 and ball_y < 60 and showbrick10 == True:
        showbrick10 = False
        scoreboard = scoreboard + 30
        y_speed = -1*y_speed
    if ball_x > 200 and ball_x < 300 and ball_y > 40 and ball_y < 60 and showbrick11 == True:
        showbrick11= False
        scoreboard = scoreboard + 30
        y_speed = -1*y_speed
        
        
    if ball_x > 300 and ball_x < 400 and ball_y > 40 and ball_y < 60 and showbrick12 == True:
        showbrick12 = False
        scoreboard = scoreboard + 50
        y_speed = -1*y_speed
        
        
        #second row from bottom
    if ball_x > 150 and ball_x < 250 and ball_y > 60 and ball_y < 80 and showbrick13 == True:
        showbrick13 = False
        scoreboard = scoreboard + 20
        y_speed = -1*y_speed
    if ball_x > 250 and ball_x < 350 and ball_y > 60 and ball_y < 80 and showbrick14 == True:
        showbrick14 = False
        scoreboard = scoreboard + 20
        y_speed = -1*y_speed  
    
        #bottom row
    if ball_x > 200 and ball_x < 300 and ball_y > 80 and ball_y < 100 and showbrick15 == True:
        showbrick15 = False
        scoreboard = scoreboard + 10
        y_speed = -1*y_speed  
        
        
    if ball_y > 400:
        f= createFont("Notable-Regular.ttf",50)
        textFont(f)
        fill(0,0,0)
        text("GAME OVER..",50,250)
        
    f= createFont("Notable-Regular.ttf",20)
    textFont(f)
    fill(0,0,0)
    text("Score:"+str(scoreboard),360,490)
    
    if (showbrick1 == False and showbrick2 == False and showbrick3 == False and showbrick4 == False and showbrick5 == False and showbrick6 == False 
            and showbrick7 == False and showbrick8 == False and showbrick9 == False and showbrick10 == False and showbrick11 == False
                and showbrick12 == False and showbrick13 == False and showbrick14 == False and showbrick15 == False):
        f= createFont("Notable-Regular.ttf",50)
        textFont(f)
        fill(0,0,0)
        text("WINNER!!",100,250)
        y_speed = 0
        x_speed = 0

    createGame()

        
