
import pygame 
import time
import random

pygame.init()
pygame.mixer.init()
  
icon_image = pygame.image.load("icon.png")
pygame.display.set_icon(icon_image) 

is_muted = False

clock = pygame.time.Clock()

open_image = pygame.image.load('open.png')
open_image = pygame.transform.scale(open_image, (1000, 800))

load_image = pygame.image.load('loading.png')
load_image = pygame.transform.scale(load_image, (1000, 800))

start_image = pygame.image.load('Menu_Page.png')
start_image = pygame.transform.scale(start_image, (1000, 800))
fin_image = pygame.image.load('fin_image.png')
fin_image = pygame.transform.scale(fin_image, (1000, 800))


game_image = pygame.image.load('game.png')
game_image = pygame.transform.scale(game_image, (1000, 800))

horse1_img = pygame.image.load('horse1_img.png')
horse1_img = pygame.transform.scale(horse1_img, (70, 70))
horse1_img_btn = pygame.transform.scale(horse1_img, (100, 100))

horse2_img = pygame.image.load('horse2_img.png')
horse2_img = pygame.transform.scale(horse2_img, (70, 70))
horse2_img_btn = pygame.transform.scale(horse2_img, (100, 100))

horse3_img = pygame.image.load('horse3_img.png')
horse3_img = pygame.transform.scale(horse3_img, (70, 70))
horse3_img_btn = pygame.transform.scale(horse3_img, (100, 100))

horse4_img = pygame.image.load('horse4_img.png')
horse4_img = pygame.transform.scale(horse4_img, (70, 70))
horse4_img_btn = pygame.transform.scale(horse4_img, (100, 100))

horse5_img = pygame.image.load('horse5_img.png')
horse5_img = pygame.transform.scale(horse5_img, (70, 70))
horse5_img_btn = pygame.transform.scale(horse5_img, (100, 100))

screen = pygame.display.set_mode((1000, 800)) 

pygame.display.set_caption("Gambaling") 

screen.fill("white") 

pygame.display.flip() 

running = True


color = "deep sky blue"

bet = None

points = 20

betpoint = 1

hx1 = 100
hx2 = 100
hx3 = 100
hx4 = 100
hx5 = 100

leadX = None
winner = None

font = pygame.font.SysFont(None, 74) 
font2 = pygame.font.SysFont(None, 40) 
font3 = pygame.font.SysFont(None, 30) 

disq = random.randint(1,100)
disq2 = random.randint(1,100)
disq3 = random.randint(1,100)
disq4 = random.randint(1,100)
disq5 = random.randint(1,100)

def horse1(x):
    global hx1
    global h1speed
    global h1speed2

    hx1 += x

    if disq <= 10:
        h1speed = 0
        h1speed2 = 0
        pygame.draw.rect(screen, color, pygame.Rect(hx1, 95, 70, 70))

    else:
        pygame.draw.rect(screen, color, pygame.Rect(hx1, 95, 70, 70))
        screen.blit(horse1_img, (hx1, 95))
    
def horse2(x):
    global hx2
    global h2speed
    global h2speed2

    hx2 += x

    if disq2 <= 10:
        h2speed = 0
        h2speed2 = 0
        pygame.draw.rect(screen, color, pygame.Rect(hx2, 215, 70, 70))

    else:
        pygame.draw.rect(screen, color, pygame.Rect(hx2, 215, 70, 70))
        screen.blit(horse2_img, (hx2, 215))

def horse3(x):
    global hx3
    global h3speed
    global h3speed2

    hx3 += x

    if disq3 <= 10:
        h3speed = 0
        h3speed2 = 0
        pygame.draw.rect(screen, color, pygame.Rect(hx3, 335, 70, 70))
    
    else:
        pygame.draw.rect(screen, color, pygame.Rect(hx3, 335, 70, 70))
        screen.blit(horse3_img, (hx3, 335))

def horse4(x):
    global hx4
    global h4speed
    global h4speed2

    hx4 += x
    
    if disq4 <= 5:        
        h4speed = 0
        h4speed2 = 0
        pygame.draw.rect(screen, color, pygame.Rect(hx4, 455, 70, 70))
    
    else:
        pygame.draw.rect(screen, color, pygame.Rect(hx4, 455, 70, 70))
        screen.blit(horse4_img, (hx4, 455))

def horse5(x):
    global hx5
    global h5speed
    global h5speed2

    hx5 += x

    if disq5 == 1:
        h4speed = 0
        h4speed2 = 0
        pygame.draw.rect(screen, color, pygame.Rect(hx5, 575, 70, 70))

    else:
        pygame.draw.rect(screen, color, pygame.Rect(hx5, 575, 70, 70))
        screen.blit(horse5_img, (hx5, 575))

def play_button_clicked(mouse_pos):
    return play_button.collidepoint(mouse_pos)

def button_clicked(mouse_pos):
    return button_rect.collidepoint(mouse_pos)

def button_clicked2(mouse_pos):
    return button2_rect.collidepoint(mouse_pos)

def button_clickedH1(mouse_pos):
    return button_h1.collidepoint(mouse_pos)

def button_clickedH2(mouse_pos):
    return button_h2.collidepoint(mouse_pos)

def button_clickedH3(mouse_pos):
    return button_h3.collidepoint(mouse_pos)

def button_clickedH4(mouse_pos):
    return button_h4.collidepoint(mouse_pos)

def button_clickedH5(mouse_pos):
    return button_h5.collidepoint(mouse_pos)

def button_hovered(mouse_pos):
    return button_Plus.collidepoint(mouse_pos)

def button_hovered2(mouse_pos):
    return button_Min.collidepoint(mouse_pos)

def button_M_Clicked(mouse_pos):
    return button_M.collidepoint(mouse_pos)


def display_winner(winner):
    global click_check
    global start_clicked
    global bet 
    global points
    global h1color
    global h2color
    global h3color
    global h4color
    global h5color
    global hx1
    global hx2
    global hx3
    global hx4
    global hx5
    global payout
    global h4speed2
    global h5speed
    global h5speed2
    global race_start
    global restart
    global disq

    screen.blit(fin_image, (0, 0))

    disq = random.randint(1,100)

    race_start = False
    winner_screen = True

    hx1 = 100
    hx2 = 100
    hx3 = 100
    hx4 = 100
    hx5 = 100

    h1color = "deep sky blue"
    h2color = "deep sky blue"
    h3color = "deep sky blue"
    h4color = "deep sky blue"
    h5color = "deep sky blue"

    start_clicked = False
    click_check = False

    win_bg = pygame.Rect(293, 85, 422, 267)

    win_bg_colour = "White" 

    win_sound()
    winner2 = ""

    if winner == "Horse 1":
        winner2 = "Batterink"
    elif winner == "Horse 2":
        winner2 = "Savoy"
    elif winner == "Horse 3":
        winner2 = "Fusilli"  
    elif winner == "Horse 4":
        winner2 = "Demu"     
    elif winner == "Horse 5":
        winner2 = "Hammood"  

    if bet == "Horse 1":
        bet2 = "Batterink"
    elif bet == "Horse 2":
        bet2 = "Savoy"
    elif bet == "Horse 3":
        bet2 = "Fusilli"  
    elif bet == "Horse 4":
        bet2 = "Demu"     
    elif bet == "Horse 5":
        bet2 = "Hammood"     

    for i in range(0,4):

        if bet == winner:
            win_bg_colour = "Green"
            pygame.draw.rect(screen, win_bg_colour, win_bg)
            payout_text = font3.render("You Won "+str(payout * betpoint)+" Points!", True, "black")
            screen.blit(payout_text, (400, 200))
            payout_text_bet = font3.render("Your Bet: "+bet2, True, "black")
            screen.blit(payout_text_bet, (300, 320))

            text = font2.render(winner2+" Has won the race!", True, "black")
            screen.blit(text, (325, 100))

            payout_text_pointbet = font3.render("Your Bet Amount: "+str(betpoint), True, "black")
            screen.blit(payout_text_pointbet, (500, 320))
            time.sleep(0.5)
            pygame.display.update()



            win_bg_colour = "White"
            pygame.draw.rect(screen, win_bg_colour, win_bg)
            payout_text = font3.render("You Won "+str(payout * betpoint)+" Points!", True, "black")
            screen.blit(payout_text, (400, 200))
            payout_text_bet = font3.render("Your Bet: "+bet2, True, "black")
            screen.blit(payout_text_bet, (300, 320))

            text = font2.render(winner2+" Has won the race!", True, "black")
            screen.blit(text, (325, 100))

            payout_text_pointbet = font3.render("Your Bet Amount: "+str(betpoint), True, "black")
            screen.blit(payout_text_pointbet, (500, 320))
            time.sleep(0.5)
            pygame.display.update()



        else:
            win_bg_colour = "Red"
            pygame.draw.rect(screen, win_bg_colour, win_bg)
            payout_text = font3.render("You Lost "+str(betpoint)+" Points", True, "black")
            screen.blit(payout_text, (400, 200))
            payout_text_bet = font3.render("Your Bet: "+bet2, True, "black")
            screen.blit(payout_text_bet, (300, 320))

            text = font2.render(winner2+" Has won the race!", True, "black")
            screen.blit(text, (325, 100))

            payout_text_pointbet = font3.render("Your Bet Amount: "+str(betpoint), True, "black")
            screen.blit(payout_text_pointbet, (500, 320))
            time.sleep(0.5)
            pygame.display.update()



            win_bg_colour = "White"
            pygame.draw.rect(screen, win_bg_colour, win_bg)
            payout_text = font3.render("You Lost "+str(betpoint)+" Points", True, "black")
            screen.blit(payout_text, (400, 200))
            payout_text_bet = font3.render("Your Bet: "+bet2, True, "black")
            screen.blit(payout_text_bet, (300, 320))

            text = font2.render(winner2+" Has won the race!", True, "black")
            screen.blit(text, (325, 100))

            payout_text_pointbet = font3.render("Your Bet Amount: "+str(betpoint), True, "black")
            screen.blit(payout_text_pointbet, (500, 320))
            time.sleep(0.5)
            pygame.display.update()
            
    if bet == winner:
        points += betpoint * payout 

    else:
        points -= betpoint

    payout = 1
    bet = None

    h4speed2 = 8.3
    h5speed = 2
    h5speed2 = 3.2

    h4AB = random.randint(1, 100)

    h5AB = random.randint(1,100)

    if h4AB <= 10:
        h4speed = 9.5
    
    if h5AB <= 15:
        h5speed = 4
        h5speed2 = 5.5


    #menu_music()   

    restart = False
 

def win_sound():

    pygame.mixer.music.stop()
    pygame.mixer.music.load("win.mp3")
    pygame.mixer.music.play()
    pygame.display.update()

def start_sound():
    global race_start
    if race_start == False:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Race.mp3")
        pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(4)

def menu_music():
    global restart
    if restart != True:
        pygame.mixer.music.load("Menu.mp3")
        pygame.mixer.music.play(-1)
        restart = True

def toggle_mute():
    global is_muted
    global button_M_Colour
    if is_muted:
        pygame.mixer.music.set_volume(1) 
        is_muted = False
        button_M_Colour= "deep sky blue"
    else:
        pygame.mixer.music.set_volume(0) 
        is_muted = True

def stat_screen():

    global h1speed
    global h2speed2
    global h2speed
    global h2speed2
    global h3speed
    global h3speed2
    global h4speed
    global h4speed2
    global h5speed
    global h5speed2

    font3 = pygame.font.Font(None, 30)
    

    running = True
    while running:
        screen.fill("white")
        screen.blit(start_image, (0, 0))
        pygame.draw.rect(screen, "deep sky blue", play_button)
        play_text = font2.render("Exit", True, "white")
        screen.blit(play_text, (play_button.x + 25, play_button.y + 26))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_button_clicked(mouse_pos):
                    print("Button clicked!")
                    running = False


        bg_h1 = pygame.Rect(50, 30, 100, 100)
        bg_h2 = pygame.Rect(50, 190, 100, 100)
        bg_h3 = pygame.Rect(50, 350, 100, 100)
        bg_h4 = pygame.Rect(50, 510, 100, 100)
        bg_h5 = pygame.Rect(50, 670, 100, 100)

        bg1_h1 = pygame.Rect(160, 20, 215, 120)
        bg2_h2 = pygame.Rect(160, 180, 215, 120)
        bg3_h3 = pygame.Rect(160, 340, 215, 120)
        bg4_h4 = pygame.Rect(160, 500, 215, 120)
        bg5_h5 = pygame.Rect(160, 660, 215, 120)

        h4_upgrade = pygame.Rect(400, 500, 100, 50)
        h5_upgrade = pygame.Rect(400, 660, 100, 50)

        pygame.draw.rect(screen, "deep sky blue", bg_h1)
        pygame.draw.rect(screen, "deep sky blue", bg1_h1)
        screen.blit(horse1_img_btn, (50, 30))
        h1_stat_txt = font3.render("Speed:0.65+ to 9.2",True, "white")
        screen.blit(h1_stat_txt, (165, 30))
        h1_stat_txt = font3.render("Payout: 1.5X", True, "White")
        screen.blit(h1_stat_txt, (165, 70))
        h1_stat_txt = font3.render("Disq Chance: 10%", True, "White")
        screen.blit(h1_stat_txt, (165, 110))

        pygame.draw.rect(screen, "deep sky blue", bg2_h2)
        pygame.draw.rect(screen, "deep sky blue", bg_h2)
        screen.blit(horse2_img_btn, (50, 190))
        h2_stat_txt = font3.render("Speed: 3.12 to 6.5",True, "white")
        screen.blit(h2_stat_txt, (165, 190))
        h2_stat_txt = font3.render("Payout: 1.5X", True, "White")
        screen.blit(h2_stat_txt, (165, 230))
        h2_stat_txt = font3.render("Disq Chance: 10%", True, "White")
        screen.blit(h2_stat_txt, (165, 270))
   
        pygame.draw.rect(screen, "deep sky blue", bg3_h3)
        pygame.draw.rect(screen, "deep sky blue", bg_h3)
        screen.blit(horse3_img_btn, (50, 350))
        h3_stat_txt = font3.render("Speed: 0.0005 to 9.25",True, "white")
        screen.blit(h3_stat_txt, (165, 350))
        h3_stat_txt = font3.render("Payout: 1.5X", True, "White")
        screen.blit(h3_stat_txt, (165, 390))
        h3_stat_txt = font3.render("Disq Chance: 10%", True, "White")
        screen.blit(h3_stat_txt, (165, 430))       
        
        pygame.draw.rect(screen, "deep sky blue", bg4_h4)
        pygame.draw.rect(screen, "deep sky blue", bg_h4)
        pygame.draw.rect(screen, "deep sky blue", h4_upgrade)
        screen.blit(horse4_img_btn, (50, 510))
        h4_stat_txt = font3.render("Speed: 0.0001 to 8.5",True, "white")
        screen.blit(h4_stat_txt, (165, 510))
        h4_stat_txt = font3.render("Payout: 4X", True, "White")
        screen.blit(h4_stat_txt, (165, 550))
        h4_stat_txt = font3.render("Disq Chance: 4%", True, "White")
        screen.blit(h4_stat_txt, (165, 590))
        h4_stat_txt = font3.render("SPEAB", True, "White")
        screen.blit(h4_stat_txt, (h4_upgrade.x +10, h4_upgrade.y + 15))

        pygame.draw.rect(screen, "deep sky blue", bg5_h5)
        pygame.draw.rect(screen, "deep sky blue", bg_h5)
        pygame.draw.rect(screen, "deep sky blue", h5_upgrade)
        screen.blit(horse5_img_btn, (50, 670))
        h5_stat_txt = font3.render("Speed: 2.5 to 5.5",True, "white")
        screen.blit(h5_stat_txt, (165, 670))
        h5_stat_txt = font3.render("Payout: 10x", True, "White")
        screen.blit(h5_stat_txt, (165, 710))
        h5_stat_txt = font3.render("Disq Chance: 1%", True, "White")
        screen.blit(h5_stat_txt, (165, 750))
        h5_stat_txt = font3.render("SPEAB", True, "White")
        screen.blit(h5_stat_txt, (h5_upgrade.x +10, h5_upgrade.y + 15))
      
        pygame.display.flip()


h1speed = 0.65
h1speed2 = 9.2

h2speed = 3.12
h2speed2 = 6.5

h3speed = 0.0005
h3speed2 = 9.25

h4speed = 0.0001
h4speed2 = 8.3


start_clicked = False

h1_clicked = False
h2_clicked = False
h3_clicked = False
h4_clicked = False
h5_clicked = False

play_button = pygame.Rect(890, 10, 100, 80)

bg_box1 = pygame.Rect(20, 20, 150, 30) 
bg_box2 = pygame.Rect(775, 20, 210, 30) 

button2_rect = pygame.Rect(400, 540, 200, 30) 
button2_text = font3.render("Stats", True, "white")

button_rect = pygame.Rect(350, 575, 300, 70) 
button_text = font2.render("Start!", True, "white")

button_h1 = pygame.Rect(150, 675, 100, 100) 
button_h2 = pygame.Rect(300, 675, 100, 100) 
button_h3 = pygame.Rect(450, 675, 100, 100) 
button_h4 = pygame.Rect(600, 675, 100, 100) 
button_h5 = pygame.Rect(750, 675, 100, 100) 

button_Plus = pygame.Rect(925, 100, 50, 50) 
button_Min = pygame.Rect(925, 175, 50, 50) 

button_M = pygame.Rect(850, 100, 50, 50) 


h1color = "deep sky blue"
h2color = "deep sky blue"
h3color = "deep sky blue"
h4color = "deep sky blue"
h5color = "deep sky blue"

click_check = False

payout = 1

mouse_held = True

race_start = False

restart = False

plus_c ="deep sky blue"
Min_c = "deep sky blue"
button_M_Colour = "deep sky blue"


h5speed = 2.5
h5speed2 = 5.5


h4AB = random.randint(1, 100)
h5AB = random.randint(1,100)

if h4AB <= 10:
    h4speed2 = 9.5

if h5AB <= 15:
    h5speed = 4
    h5speed2 = 6.5


first = True
load = True
first_Open = True
bar_progress = 0
img_launch = open_image
sleeptime = 3

fade_speed = 5 
max_alpha = 255

while running:
    while load:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if first_Open:
            for alpha in range(0, max_alpha, fade_speed):
                open_image.set_alpha(alpha)
                screen.blit(open_image, (0, 0))
                pygame.display.update()
                time.sleep(0.03)
                first_Open = False
            time.sleep(4)

        screen.blit(load_image, (0,0))
        bar_progress += 10
        load_bar = pygame.Rect(163, 270, bar_progress, 70) 
        pygame.draw.rect(screen, "white", load_bar)
        time.sleep(0.01)
        pygame.display.update()

        if bar_progress >= 645:
            time.sleep(0.5)
            load = False


    #elif load == False:
    menu_music()

    restart = True

    mouse_pos = pygame.mouse.get_pos()
    
    screen.blit(start_image, (0, 0))

    pygame.draw.rect(screen, "deep sky blue", button_rect)
    screen.blit(button_text, (button_rect.x + 110, button_rect.y + 20))

    pygame.draw.rect(screen, "deep sky blue", button2_rect)
    screen.blit(button2_text, (button2_rect.x + 73, button2_rect.y + 5))


    points_text = font2.render("Points: "+str(points), True, "black")
    screen.blit(points_text, (10, 20))

    points_text = font2.render("Bet Amount: "+str(betpoint), True, "black")
    screen.blit(points_text, (755, 20))
    
    pygame.draw.rect(screen, plus_c, button_Plus)
    plus_text= font.render(("+"), True, "black")
    screen.blit(plus_text, (button_Plus.x +10, button_Plus.y))

    pygame.draw.rect(screen, Min_c, button_Min)
    plus_text= font.render(("-"), True, "black")
    screen.blit(plus_text, (button_Min.x +18, button_Min.y))

    pygame.draw.rect(screen, button_M_Colour, button_M)
    Mute_text= font.render(("M"), True, "black")
    screen.blit(Mute_text, (button_M.x +4, button_M.y + 2))

    pygame.draw.rect(screen, h1color, button_h1)
    screen.blit(horse1_img_btn, (150, 675))
    pygame.draw.rect(screen, h2color, button_h2)
    screen.blit(horse2_img_btn, (300, 675))
    pygame.draw.rect(screen, h3color, button_h3)
    screen.blit(horse3_img_btn, (450, 675))
    pygame.draw.rect(screen, h4color, button_h4)
    screen.blit(horse4_img_btn, (600, 675))
    pygame.draw.rect(screen, h5color, button_h5)
    screen.blit(horse5_img_btn, (750, 675))

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if button_clicked(mouse_pos):  
                if betpoint <= points and betpoint > 0:
                    if bet != None:
                        start_clicked = True

                    else:
                        Error_text_bet = font2.render("Invaild Bet Selection", True, "black")
                        screen.blit(Error_text_bet, (70, 595))

                else:
                    Error_text_points = font2.render("Invaild Points", True, "black")
                    screen.blit(Error_text_points, (150, 595))

            if button_clicked2(mouse_pos):
                stat_screen()


            if button_clickedH1(mouse_pos):
                if click_check != True:
                    bet = "Horse 1"
                    h1color = "green"
                    click_check = True
                    payout = 1.5

            if button_clickedH2(mouse_pos):
                if click_check != True:
                    bet = "Horse 2"
                    h2color = "green"
                    click_check = True
                    payout = 1.5

            if button_clickedH3(mouse_pos):
                if click_check != True:
                    bet = "Horse 3"
                    h3color = "green"
                    click_check = True
                    payout = 2

            if button_clickedH4(mouse_pos):
                if click_check != True:
                    bet = "Horse 4"
                    h4color = "green"
                    click_check = True
                    payout = 4

            if button_clickedH5(mouse_pos):

                if click_check != True:
                    bet = "Horse 5"
                    h5color = "green"
                    click_check = True
                    payout = 10

            if button_M_Clicked(mouse_pos):
                button_M_Colour= "green"
                toggle_mute()

            if button_hovered(mouse_pos):
                plus_c = "green"
                if betpoint < points:
                    betpoint += 1
                    if betpoint > points:
                        betpoint-= 1

            if button_hovered2(mouse_pos):
                Min_c = "green"
                if betpoint != 0:
                    betpoint -= 1
                    
            

        elif event.type == pygame.MOUSEBUTTONUP: 
            mouse_held = False

            plus_c ="deep sky blue"
            Min_c = "deep sky blue"

    if start_clicked:

        screen.blit(game_image, (0, 0))

        pygame.draw.rect(screen, "green", pygame.Rect(0, 700, 1000, 300))

    #=========================Horses============================
        horse1(random.uniform(h1speed,h1speed2))
        horse2(random.uniform(h2speed,h2speed2)) 
        horse3(random.uniform(h3speed,h3speed2)) 
        horse4(random.uniform(h4speed,h4speed2))
        horse5(random.uniform(h5speed,h5speed2))

        leadX = max(hx1, hx2, hx3, hx4, hx5)

        if hx1 >= leadX:
            lead = "Batterink"

        elif hx2 >= leadX:
            lead = "Savoy"

        elif hx3 >= leadX:
            lead = "Fusilli"

        elif hx4 >= leadX:
            lead = "Demu"

        elif hx5 >= leadX:
            lead = "Hamood"


        if hx1 >= 880:
            winner = "Horse 1"

        elif hx2 >= 880:
            winner = "Horse 2"

        elif hx3 >= 880:
            winner = "Horse 3"

        elif hx4 >= 880:
            winner = "Horse 4"

        elif hx5 >= 880:
            winner = "Horse 5"

        if bet == "Horse 1":
            bet2 = "Batterink"

        elif bet == "Horse 2":
            bet2 = "Savoy"

        elif bet == "Horse 3":
            bet2 = "Fusilli"

        elif bet == "Horse 4":
            bet2 = "Demu"

        elif bet == "Horse 5":
            bet2 = "Hamood"

        textLead = font2.render("Leader: "+lead, True, "black")
        screen.blit(textLead, (25, 710))

        text_bethorse = font2.render("Your Bet: "+str(bet2), True, "black")
        screen.blit(text_bethorse, (25, 760))

        text_betamt = font2.render("Your Bet Amount: "+str(betpoint), True, "black")
        screen.blit(text_betamt, (675, 760))

        text_payout = font2.render("Your Payout: "+str(payout)+"X", True, "black")
        screen.blit(text_payout, (700, 710))

        start_sound()
        race_start = True

        if winner:
            display_winner(winner)
            winner = None
                
    pygame.display.update()

    clock.tick(10)
    #time.sleep(0.001)
