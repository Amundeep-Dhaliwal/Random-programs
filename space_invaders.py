import pygame, random, math, time
from pygame import mixer

pygame.init() # Initialize the pygame

screen = pygame.display.set_mode((800, 600)) # 800 pixels wide 600 pixels height

background = pygame.image.load(r"C:\Users\Amundeep\Pictures\PyAutoGUI\stardust800_600.png")

mixer.music.load(r"C:\Users\Amundeep\Documents\Amundeep Singh Dhaliwal\Coding\Useful programs\Incomplete\space invaders\Space-Invaders-Pygame-master\back.wav")
mixer.music.play(-1)

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load(r"C:\Users\Amundeep\Pictures\Camera Roll\space.png")
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load(r"C:\Users\Amundeep\Pictures\Camera Roll\space64.png")
playerx = 368
playery = 500
playerx_change = 0
playery_change = 0

# Score

player_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10 

def show_score(x, y):
    score = font.render('Score: ' + str(player_score), True, (255, 247, 0))
    screen.blit(score, (x,y))

# Game over message
game_over = pygame.font.Font('freesansbold.ttf',50 )
def game_over_text():
    game_screen = game_over.render('GAME OVER!', True, (255,0,0))
    screen.blit(game_screen,(245, 250))


def player(x,y):
    screen.blit(playerImg, (x, y))

#enemy
enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_change =[]
enemyy_change=[]
num_of_enemies = 6 # number of enemies

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r"C:\Users\Amundeep\Pictures\Camera Roll\spaceship64.png"))
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(4)
    enemyy_change.append(20) # change how far down the the screen the ships move

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))


#bullet
bulletImg = pygame.image.load(r"C:\Users\Amundeep\Pictures\Camera Roll\bullet32.png")
bulletx = 0
bullety = 500
bullety_change = 8
bulletx_change = 0
bullet_fire = 'ready'

def fire_bullet(x, y):
    global bullet_fire
    bullet_fire = 'fired'
    screen.blit(bulletImg, (x+22, y+10))


def collision(enemyx, enemyy, bulletx, bullety):
    collide = math.sqrt(math.pow(enemyx - bulletx,2) + math.pow(enemyy - bullety,2))
    if collide < 27:
        return True
    else:
        return False


running = True
while running:
    r = random.randint(25,55)
    g = random.randint(0,55)
    b = random.randint(0,55)
    screen.fill((0,0,51))
    screen.blit(background, (0,0))
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change -= 5
            if event.key == pygame.K_RIGHT:
                playerx_change += 5
            if event.key == pygame.K_SPACE:
                if bullet_fire=='ready':
                    bulletx = playerx
                    laser_sound = mixer.Sound(r"C:\Users\Amundeep\Documents\Amundeep Singh Dhaliwal\Coding\Useful programs\Incomplete\space invaders\Space-Invaders-Pygame-master\laser.wav")
                    #bullety =playery
                    laser_sound.play()
                    fire_bullet(bulletx, bullety)

            #elif event.key == pygame.K_UP:
             #   playery_change -= 5
            #elif event.key == pygame.K_DOWN:
             #   playery_change += 5
        if event.type == pygame.KEYUP:
            #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerx_change = 0
            playery_change = 0

    # checking boundaries for player
    playerx += playerx_change
    playery += playery_change

    if playerx <= 0:
        playerx = 0
    if playerx >= 736:
        playerx = 736
    if playery >= 525: # limit how far down the player can go
        playery = 525
    if playery <= 200: # limit how far up the player can go
        playery = 200

    # enemy movement
    for i in range(num_of_enemies):
        # game over condition
        if enemyy[i] > 480:
            for j in range(num_of_enemies):
                enemyy[j] = 1000
            game_over_text()
            break


        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 4
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -4
            enemyy[i] += enemyy_change[i]

        despawn = collision(enemyx[i], enemyy[i], bulletx, bullety)
        if despawn:
            explosion_sound = mixer.Sound(r"C:\Users\Amundeep\Documents\Amundeep Singh Dhaliwal\Coding\Useful programs\Incomplete\space invaders\Space-Invaders-Pygame-master\explosion.wav")
            explosion_sound.play()
            
            bullety = -10
            player_score += 1
            enemyx[i] = random.randint(0,736)
            enemyy[i] = random.randint(50,150)
            bullet_state = 'ready'

        enemy(enemyx[i],enemyy[i],i)
    # bullet 
    if bullety <=-5:
        bullety=playery
        bullet_fire = 'ready'

    if bullet_fire=='fired':
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change 

    

    player(playerx, playery)
    show_score(textx,texty)
    pygame.display.update()
