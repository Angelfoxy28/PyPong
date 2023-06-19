# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# posicion y velocidad del jugador y la pelota
jugadorX = 50
jugadorY = 10
jugadorVel = 8

jugador2X = 1280-(30+50)
jugador2Y = 10
jugador2Vel = 8

circleX = screen.get_width()/2
circleY = screen.get_height()/2
circleRad = random.randrange(15,20)
circleVel = 5

# variables importantes para el circulo
circleLeft = random.choice([True, False])
circleUp = random.choice([True, False])

# imagenes
dottedLine = pygame.image.load("line.png")
dottedLineBG = pygame.image.load("line.png")
dottedLineBG.set_alpha(80)

# textos y fuente
FONT = pygame.font.Font("font.ttf", 80)

JScore = 0
J2Score = 0

JScoreText = FONT.render("0", False, "white")
JScoreTextBG = FONT.render("0", False, (50,50,50))
J2ScoreText = FONT.render("0", False, "white")
J2ScoreTextBG = FONT.render("0", False, (50,50,50))

# importante
jugando = True



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, (50,50,50), (jugadorX+5,jugadorY+5,30,200))
    pygame.draw.rect(screen, (255,255,255), (jugadorX,jugadorY,30,200))
    pygame.draw.rect(screen, (50,50,50), (jugador2X+5,jugador2Y+5,30,200))
    pygame.draw.rect(screen, (255,255,255), (jugador2X,jugador2Y,30,200))

    screen.blit(dottedLineBG, (5, 5))
    screen.blit(dottedLine, (0, 0))

    JScoreText = FONT.render(str(JScore), False, "white")
    J2ScoreText = FONT.render(str(J2Score), False, "white")
    JScoreTextBG = FONT.render(str(JScore), False, (50,50,50))
    J2ScoreTextBG = FONT.render(str(J2Score), False, (50,50,50))

    screen.blit(JScoreTextBG, (565, 25))
    screen.blit(JScoreText, (560, 20))
    screen.blit(J2ScoreTextBG, (685, 25))
    screen.blit(J2ScoreText, (680, 20))

    pygame.draw.circle(screen, (255,255,255), (circleX, circleY), circleRad)

    # RENDER YOUR GAME HERE

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    if keys[pygame.K_s] and jugadorVel < 8:
        #jugadorY += jugadorVel
        jugadorVel += 15
    elif keys[pygame.K_w] and jugadorVel > -8:
        #jugadorY -= jugadorVel
        jugadorVel -= 15
    else:
        jugadorVel = 0

    jugadorY += jugadorVel

    if keys[pygame.K_DOWN] and jugador2Vel < 8:
        jugador2Vel += 15
    elif keys[pygame.K_UP] and jugador2Vel > -8:
        jugador2Vel -= 15
    else:
        jugador2Vel = 0

    jugador2Y += jugador2Vel

    if jugadorY < 0:
        jugadorY = 0
    if jugadorY > 520:
        jugadorY = 520
    if jugador2Y < 0:
        jugador2Y = 0
    if jugador2Y > 520:
        jugador2Y = 520

    if circleLeft == False:
        circleX -= circleVel
    else:
        circleX += circleVel

    if circleUp == False:
        circleY -= circleVel
    else:
        circleY += circleVel

    if circleY > screen.get_height()-circleRad:
        circleUp = False
        circleVel += 0.05
    elif circleY < circleRad:
        circleUp = True
        circleVel += 0.05

    if circleX > jugadorX and circleX < jugadorX+30 and circleY > jugadorY and circleY < jugadorY + 200:
        circleLeft = True
        circleVel += 0.3

    if circleX > jugador2X and circleX < jugador2X+30 and circleY > jugador2Y and circleY < jugador2Y + 200:
        circleLeft = False
        circleVel += 0.3

    if circleX < -circleRad:
        circleX = screen.get_width()/2+200
        circleY = screen.get_height()/2
        circleLeft = False
        circleUp = random.choice([True, False])
        circleRad = random.randrange(15,20)
        circleVel = 5
        J2Score += 1
    elif circleX > screen.get_width()+circleRad:
        circleX = screen.get_width()/2-200
        circleY = screen.get_height()/2
        circleLeft = True
        circleUp = random.choice([True, False])
        circleRad = random.randrange(15,20)
        circleVel = 5
        JScore += 1

    if JScore > 9 or J2Score > 9:
        pygame.quit()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()