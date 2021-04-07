# basic_game
Second Python capstone project - Using given code, expand upon a simple game to include more obstacles, maneuverability, a prize and win conditions

Task requirement:

A game based on the example provided, consisting of 1 player character, 
at least 3 enemy characters and at least 1 prize object.

Planning:

the PyGame library is required for this task and can be installed from windows command line using
	
	py -m pip install -U pygame --user

use
	py -m pygame.examples.aliens

from the command line to test if it is installed correctly.

Documentation for using the PyGame library can be found at
 
	https://www.pygame.org/docs/


from my understanding of the task, the game should be built by expanding on the functionality 
of the example game provided instead of built completely from the ground up.

Items missing from example code:
   From reading code base:
	2 "enemy" objects - 1 is provided
	a "prize" object
	ability for player to move left/right
	a winning condition for touching a 'prize' object

   From giving the game a test play
	no "win" screen - correction: displayed in terminal window
	no"lose" screen - correction: displayed in terminal window
	enemy only moves in a straight line and one direction, win condition met if player has dodged incoming enemy
	player and enemy size is too large for multiple instances to be present simultaneously
	
Changes made to original code:
	
	number of enemies increased from 1 to 4
		enemy movement set to be a pair of horizontaly and a pair of verticaly moving enemies
		restriction set in place to prevent spawning in same position
		enemy movement speed increased
		enemy movement speed varied
		
	prize object brought into game
		prize object made to spawn randomly on screen, X-Coordinate restricted to prevent
		spawning on top of player
	
	Images used for player and enemy changed
		images cropped to remove excess white spaces
		images scaled to better accomodate game screen
	
	Left and Right movement functionality of player character implemented
	
	Win condition for touching prize implemented
	


Explanation of code used in game file

Added code:
	
	pygame.transform.scale(image_var, (int(image_var.get_width()/2), int(image_var.get_height()/2)))
		I found that the provided images, even after cropping to get rid of excess white space,
		was too large for the game. As such I used this code to halve the size of the images used.

	enemy2XPosition =  random.randint(0, screen_width - enemy2_width)
	enemy2YPosition =  screen_height
		Similar to the enemy position given below, these 2 spawns an enemy character. Character Y position is specified and 
		off screen,	however their X position is randomised and set to span anywhere from the left of the screen to within the
		border of the rigt of the screen.
		I added this to introduce vertically moving enemies as only horizontal enemies was too easy to dodge
	
	while (enemy3YPosition == enemy1YPosition) :
		enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
	while (enemy4XPosition == enemy2XPosition) :
		enemy4XPosition =  random.randint(0, screen_width - enemy2_width)
		
		These 2 while loops prevent the enemies from spawning in the exact same position, they can still overlap however
	
	prizeXPosition =  random.randint(200, screen_width - prize_width)
	prizeYPosition =  random.randint(0, screen_height - prize_height)
		These 2 lines spawns the prize in random X and Y coordinates on the screen. X position has a lower limit of 200
		to prevent it from spawning on the player character
	
	if keyLeft == True:
        if playerXPosition > 0 :
			playerXPosition -= 1
	if keyRight == True:
        if playerXPosition < screen_width - player_width:
			playerXPosition += 1
		
		These 2 nested if statements insure that player character cannot move off the left or right side of the game window
			
	enemy2YPosition -= 0.70
		move enemy vertically

given code:

	pygame.display.set_mode((width,height))
		sets the size of the game window to specified parameters
	
	pygame.image.load("image.format")
		loads the designated image of file type format 
	
	variable.get_height()
	variable.get_width()
		these 2 in conjunction are used to get the size of the images used in order to calculate boundary detection
	
	playerXPosition = 100
	playerYPosition = 50
		these 2 in conjunction spawns the player character in the specific position of X-coordinate 100 and Y-coordinate 50
	
	enemyXPosition =  screen_width
	enemyYPosition =  random.randint(0, screen_height - enemy1_height)
		Similar to the above, these 2 spawns an enemy character. Character X position is specified and off screen,
		however their Y position is randomised and set to span anywhere from the top of the screen to within the border of
		the bottom of the screen.
	
	screen.fill(0)
		clears the screen
	
	screen.blit(reference, (referenceXPosition, referenceYPosition))
		spawns the referenced (player, enemy1, enemy3, prize, etc) piece on screen
	
	pygame.display.flip()
		updates the game screen
	
	for event in pygame.event.get():
		loops through game events, makes it run
		
	if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)
		
		checks if user has quit the game and exits the program if so
	
	if event.type == pygame.KEYDOWN:
		checks if a button on the keyboard is pressed
		
	if event.key == pygame.K_REF:
		keyRef = True
		related to button press event above, narrows selection down to the 4 required directional buttons
		and sets their bool check value to true while held. Each direction has their own ref code.
	
	if event.type == pygame.KEYUP:
		checks if a button on the keyboard is not pressed
	
	if event.key == pygame.K_REF:
		keyRef = False
		Related to buton press event above, insures that a key which is no longer pressed registers as such	
	
	if keyUp == True:
        if playerYPosition > 0 :
			playerYPosition -= 1
	if keyDown == True:
        if playerYPosition < screen_height - player_height:
			playerYPosition += 1
			
		These 2 nested if statements insures that character cannot move above or below game window
		
	referenceBox = pygame.Rect(reference.get_rect())
		Sets a boundary box around referenced object
	
	referenceBox.top = referenceYPosition
    referenceBox.left = referenceXPosition
		Maintains boundary box around referenced object as it moves
		
	playerBox.colliderect(other_referenceBox)
		detects if player collides with an enemy or the prize
	
	enemy1XPosition < 0 - enemy1_width
		references event to occur if enemies are off screen resulting in win condition
	
	enemy1XPosition -= 0.65
		move enemy horizontally, originally set speed to 0.15 which was too easy and thus amended
