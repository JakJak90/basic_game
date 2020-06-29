# Make a very simple game using the pygame library.

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 
#changed player icon to player.jpg, enemy became enemies 1-3 and image changed to monster.jpg, prize created and assigned icon of prize.jpg

player = pygame.image.load("player_cropped.jpg")
player = pygame.transform.scale(player, (int(player.get_width()/2), int(player.get_height()/2))) #image sizes too large, resized to half size

enemy1 = pygame.image.load("monster1_cropped.jpg")
enemy1 = pygame.transform.scale(enemy1, (int(enemy1.get_width()/2), int(enemy1.get_height()/2)))

enemy2 = pygame.image.load("monster2_cropped.jpg")
enemy2 = pygame.transform.scale(enemy2, (int(enemy2.get_width()/2), int(enemy2.get_height()/2)))

enemy3 = pygame.image.load("monster3_cropped.jpg")
enemy3 = pygame.transform.scale(enemy3, (int(enemy3.get_width()/2), int(enemy3.get_height()/2)))

enemy4 = pygame.image.load("monster4_cropped.jpg")
enemy4 = pygame.transform.scale(enemy4, (int(enemy4.get_width()/2), int(enemy4.get_height()/2)))

prize = pygame.image.load("prize_cropped.jpg")
prize = pygame.transform.scale(prize, (int(prize.get_width()/2), int(prize.get_height()/2)))



# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

enemy4_height = enemy4.get_height()
enemy4_width = enemy4.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemies start off screen and at a random y position.

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2XPosition =  random.randint(0, screen_width - enemy2_width)
enemy2YPosition =  screen_height 


enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height) #while loop prevents enemies spawning on same block
while (enemy3YPosition == enemy1YPosition) :
    enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

enemy4XPosition =  random.randint(0, screen_width - enemy2_width) #while loop prevents enemies spawning on same block
while (enemy4XPosition == enemy2XPosition) :
    enemy4XPosition =  random.randint(150, screen_width - enemy2_width)
enemy4YPosition =  screen_height

# Make the prize start off at a random x and y position.

prizeXPosition =  random.randint(200, screen_width - prize_width) #position of at least 150px prevents spawning on player
prizeYPosition =  random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other.

keyUp= False
keyDown = False
keyLeft= False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(enemy4, (enemy4XPosition, enemy4YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
            
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player left of the window.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:# This makes sure that the user does not move the player right of the window.
            playerXPosition += 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemies:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    enemy4Box = pygame.Rect(enemy4.get_rect())
    enemy4Box.top = enemy4YPosition
    enemy4Box.left = enemy4XPosition

    # Bounding box for the prize:
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box) or playerBox.colliderect(enemy4Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
 
        
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)


    # If the enemy is off the screen or the user touches the prize, user wins the game:
    
    if enemy1XPosition < 0 - enemy1_width or playerBox.colliderect(prizeBox):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemies approach the player.
    
    enemy1XPosition -= 0.65
    enemy2YPosition -= 0.70
    enemy3XPosition -= 0.75
    enemy4YPosition -= 0.80

    
    # ================The game loop logic ends here. =============
  
