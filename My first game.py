#Import pygame
import pygame
#Initaite the game
pygame.mixer.init()
pygame.init()

#Set the screen width and height and store in variable
width, height = 850, 450
screen=pygame.display.set_mode((width, height))
#Top left of the window it will display "My First Game
pygame.display.set_caption("My First Game!!")

#Declared variables
WHITE =(255, 255, 255)
BLUE =(0, 0, 200)
player_width, player_height= (50, 50)
enemy_width, enemy_height= (75,75)
FPS= 60
speed= 2
reward_width, reward_height= (200, 100)
you_lose_width, you_lose_height= (200, 100)
star_width, star_height= (20, 20)



#Load all character images and screens for the game
player= pygame.image.load("player.jpg")
player = pygame.transform.scale(player,(50,50))
enemy1=pygame.image.load("monster.jpg")
enemy1=pygame.transform.scale(enemy1, (75,75))
enemy2=pygame.image.load("monster.jpg")
enemy2=pygame.transform.scale(enemy2, (75,75))                              
enemy3=pygame.image.load("monster.jpg")
enemy3=pygame.transform.scale(enemy3, (75,75))
reward= pygame.image.load("reward.png")
reward= pygame.transform.scale(reward, (500, 200))
you_lose= pygame.image.load("you_lose.png")
you_lose= pygame.transform.scale(you_lose, (500, 200))
star=pygame.image.load("prize.jpg")
star=pygame.transform.scale(star, (20, 20))
                               
                               

#Define players movement in fuction
def player_movement(keys_pressed, good_guy):
     #Moves Character left
     if keys_pressed[pygame.K_LEFT] and good_guy.x - speed > 0: 
                good_guy.x -= speed
     #Moves character right           
     if keys_pressed[pygame.K_RIGHT] and good_guy.x + speed < width - 50:
                good_guy.x += speed
     #Moves character up           
     if keys_pressed[pygame.K_UP] and good_guy.y - speed > 0:
                good_guy.y -= speed
     #moves character down           
     if keys_pressed[pygame.K_DOWN] and good_guy.y + speed < height - 50:
                good_guy.y += speed
    

    
    
    
#define draw_window into a fuction
def draw_window(good_guy, bad_guy1, bad_guy2, bad_guy3):
    #Makes game backround screen blue
    screen.fill(BLUE)
    #Shows player on screen at a spesific start spot
    screen.blit(player,(good_guy.x, good_guy.y))
    #Shows "enemies" on screen at a spesific start spot
    screen.blit(enemy1,(bad_guy1.x, bad_guy1.y))
    screen.blit(enemy2,(bad_guy2.x, bad_guy2.y))
    screen.blit(enemy3,(bad_guy3.x, bad_guy3.y))
    screen.blit(star, (prize.x, prize.y))
    #Updates the game screen
    pygame.display.update()
    

#Set the starting coordinates of all images
good_guy= pygame.Rect(0, 225, player_width, player_height)
bad_guy1= pygame.Rect(850, 225, enemy_width, enemy_height)
bad_guy2= pygame.Rect(400, 70, enemy_width, enemy_height)
bad_guy3= pygame.Rect(225, 350, enemy_width, enemy_height)
win= pygame.Rect(150,200, reward_width, reward_height)
lose= pygame.Rect(150,200, you_lose_width, you_lose_height)
prize= pygame.Rect(830,20, star_width, star_height) 

#variable for the frame rate
clock = pygame.time.Clock()
run=True
while run:
     #sets Frame per second 
     clock.tick(FPS)
     #If user quits game will end
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run=False
                   

     #applied above made fuction
     keys_pressed= pygame.key.get_pressed()
     player_movement(keys_pressed, good_guy)

    
     
     #makes images move from left to right or top to bottom or bottom to top
     bad_guy1.x -= 1
     bad_guy2.y += 1
     bad_guy3.y -= 1

     #makes a rectangle to store image in               
     playerbox= pygame.Rect(player.get_rect())
     playerbox.top = good_guy.y
     playerbox.left = good_guy.x

     enemybox1= pygame.Rect(enemy1.get_rect())
     enemybox1.top = bad_guy1.y
     enemybox1.left = bad_guy1.x

     enemybox2= pygame.Rect(enemy2.get_rect())
     enemybox2.top = bad_guy2.y
     enemybox2.left = bad_guy2.x

     enemybox3= pygame.Rect(enemy3.get_rect())
     enemybox3.top = bad_guy3.y
     enemybox3.left = bad_guy3.x

     starbox= pygame.Rect(star.get_rect())
     starbox.top = prize.y
     starbox.left = prize.x

     
     
#if player colides into any of the three moving images then player losses and you lose screen will appear
#if player colides with the prize the player wins the game and winning screen appears     
     Collide=False
     if playerbox.colliderect(enemybox1):
          Collide= True
          print("You lose!!")
          screen.blit(you_lose, (lose.x, lose.y))
          pygame.display.update()
          #Delays the time before quiting the game
          pygame.time.delay(5000)            
          pygame.quit()
          break
     elif playerbox.colliderect(enemybox2):
          Collide= True
          print("You lose!!")
          screen.blit(you_lose, (lose.x, lose.y))
          pygame.display.update()
          pygame.time.delay(5000)            
          pygame.quit()
          break
     elif playerbox.colliderect(enemybox3):
          Collide= True
          print("You lose!!")
          screen.blit(you_lose, (lose.x, lose.y))
          pygame.display.update()
          pygame.time.delay(5000)            
          pygame.quit()
          break
     elif playerbox.colliderect(starbox):
          print("You win")
          screen.blit(reward, (win.x, win.y))
          pygame.display.update()
          pygame.time.delay(5000)
          pygame.quit()
          break

     draw_window(good_guy, bad_guy1, bad_guy2, bad_guy3)


          
               
               
               
            

              
          
          
        

          
