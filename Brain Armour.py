import pygame
import numpy as np
from tkinter import *
from tkinter.ttk import *
import pygame_menu
from pygame.locals import *
from time import sleep
import sys
import random


master = Tk()

master.geometry("800x800")
bg = PhotoImage(file = "/Users/ajayjayakumar/Desktop/Ajay/setb.png")
label1 = Label( master, image = bg)
label1.place(x = 0, y = 0)

def open2NewWindow():
    pygame.init()

    surface = pygame.display.set_mode((800, 800))


    def start_the_game2 ():

        pygame.init()
        scr = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("challenging ball")
        pygame.display.set_icon(scr)
        bg = pygame.image.load(r"/Users/ajayjayakumar/Desktop/Ajay/cb.png")
        scr.blit(bg, (0, 0))

        f40 = pygame.font.SysFont('stkaiti', 40)
        f30 = pygame.font.SysFont('stkaiti', 30)

        def printtext(font, text, x, y, color):
            img = font.render(text, True, color)
            scr.blit(img, (x, y))

        def draw_p(p1_y, p2_y):
            speed = 12
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                p1_y -= speed
                p1_y = max(0, p1_y)
            elif keys[K_s]:
                p1_y += speed
                p1_y = min(750, p1_y)
            if keys[K_UP]:
                p2_y -= speed
                p2_y = max(0, p2_y)
            elif keys[K_DOWN]:
                p2_y += speed
                p2_y = min(750, p2_y)
            pygame.draw.rect(scr, (143, 188, 143), (100, p1_y, 10, 50), 0)
            pygame.draw.rect(scr, (255, 0, 0), (690, p2_y, 10, 50), 0)
            return (p1_y, p2_y)

        # for initialize the ball
        def init_ball(ball_speed):
            pygame.draw.circle(scr, (0, 0, 0), (400, 400), 7)

            px = random.randint(-ball_speed, ball_speed)
            py = random.randint(-ball_speed, ball_speed)
            while px == 0:
                px = random.randint(-ball_speed, ball_speed)
            while py == 0:
                py = random.randint(-ball_speed, ball_speed)
            return 400, 400, px, py

        # for panel detection
        def in_p(x, y, p1_y, p2_y):
            if x in range(100, 110):
                return y in range(p1_y, p1_y + 50)
            elif x in range(690, 800):
                return y in range(p2_y, p2_y + 50)

        # for update and display the ball
        def update_ball(x, y, px, py, p1_y, p2_y):
            x += px
            y += py

            if x < 0 or x > (800 - 7) or in_p(x, y, p1_y, p2_y):
                px = -px
            if y < 0 or y > (800 - 7):
                py = -py
            pygame.draw.circle(scr, (0, 0, 0), (x, y), 7)
            return x, y, px, py

        def main_loop():
            p1_y, p2_y = 400, 400
            p1 = 0
            p2 = 0
            b_x, b_y = -1, -1
            while True:
                if p1 >= 2 or p2 >= 2:
                    break
                scr.blit(bg, (0, 0))

                for eve in pygame.event.get():
                    if eve.type == QUIT:
                        sys.exit()
                keys = pygame.key.get_pressed()

                p1_y, p2_y = draw_p(p1_y, p2_y)
                printtext(f30, "Player 1: " + str(p1), 10, 10, (143, 188, 143))
                printtext(f30, "Player 2: " + str(p2), 690, 10, (255, 0, 0))
                printtext(f40, "press SPACE Reserve ", 250, 700, (255, 255, 255))
                if (b_x == -1 and b_y) == -1 or keys[K_SPACE]:
                    b_x, b_y, px, py = init_ball(2)
                else:
                    b_x, b_y, px, py = update_ball(b_x, b_y, px, py, p1_y, p2_y)
                if b_x in range(0, 80) and b_y in range(75, 725):
                    p2 += 1
                    pygame.display.update()
                    sleep(1.5)
                    b_x, b_y, px, py = init_ball(2)
                elif b_x in range(720, 800) and b_y in range(75, 725):
                    p1 += 1
                    pygame.display.update()
                    sleep(1.5)
                    b_x, b_y, px, py = init_ball(2)
                pygame.display.update()
                sleep(0.005)
            scr.blit(bg, (0, 0))
            printtext(f40, "Player %d got 1 point!" % (1 if p1 > p2 else 2), 220, 200, (255, 255, 255))
            printtext(f30, "press SPACE to restart", 200, 30, (255, 255, 255))
            pygame.display.update()
            keys = pygame.key.get_pressed()
            scr.blit(bg, (0, 0))
            while not keys[K_SPACE]:
                for eve in pygame.event.get():
                    if eve.type == QUIT:
                        sys.exit()
                keys = pygame.key.get_pressed()
                printtext(f40, "Player %d WIN" % (1 if p1 > p2 else 2), 250, 200, (255, 255, 255))
                printtext(f30, "press Key space to restart", 250, 30, (255, 255, 255))
                pygame.display.update()

        while True:
            main_loop()



    def   about_game ():
        pygame.init()

        scr = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("challenging ball")
        pygame.display.set_icon(scr)
        bg = pygame.image.load(r"/Users/ajayjayakumar/Desktop/Ajay/challenging Ball.png")
        scr.blit(bg, (0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # deactivates the pygame library
                    pygame.quit()
                    # quit the program.
                    quit()

                pygame.display.update()



    menu = pygame_menu.Menu('Welcome', 800, 800, theme=pygame_menu.themes.THEME_DARK)
    pygame.display.set_caption('CHALLENGING BALL')
    menu.add.button('Play', start_the_game2)
    menu.add.button('Hint', about_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)



def openNewWindow():

    pygame.init()

    surface = pygame.display.set_mode((800, 800))
    def start_the_game():
        pygame.init()
        WIDTH = 800
        HEIGHT = 800
        LINE_WIDTH = 15
        WIN_LINE_WIDTH = 15
        BOARD_ROWS = 3
        BOARD_COLS = 3
        SQUARE_SIZE = 270
        CIRCLE_RADIUS = 20
        CIRCLE_WIDTH = 20
        line_width = 10
        line_color = (128,0,0)
        CIRCLE_COLOR = (47,79,79)
        circle_color = (75,0,130)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('SET')
        board = np.zeros((BOARD_ROWS, BOARD_COLS))
        bg = pygame.image.load(r"/Users/ajayjayakumar/Desktop/Ajay/setb.png")
        screen.blit(bg, (0, 0))

        def draw_lines():
            pygame.draw.line(screen, line_color, (120, 130), (688, 681), line_width)  # first diagonal
            pygame.draw.line(screen, line_color, (120, 681), (688, 681), line_width)  # horizontal bottom
            pygame.draw.line(screen, line_color, (120, 130), (688, 130), line_width)  # horizontal top
            pygame.draw.line(screen, line_color, (120, 405), (688, 405), line_width)  # horizontal mid
            pygame.draw.line(screen, line_color, (405, 128), (405, 681), line_width)  # vertical mid
            pygame.draw.line(screen, line_color, (120, 130), (120, 681), line_width)  # vertical first
            pygame.draw.line(screen, line_color, (120, 681), (688, 130), line_width)  # diagonal second
            pygame.draw.line(screen, line_color, (688, 130), (688, 681), line_width)  # vertical last

        def yellow():
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    if board[row][col] == 1:
                        pygame.draw.circle(screen, CIRCLE_COLOR, (
                            int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                           CIRCLE_RADIUS,
                                           CIRCLE_WIDTH)

        def red():
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    if board[row][col] == 2:
                        pygame.draw.circle(screen, circle_color, (
                            int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                           CIRCLE_RADIUS,
                                           CIRCLE_WIDTH)

        def mark_square(row, col, player):
            board[row][col] = player

        def available_square(row, col):
            return board[row][col] == 0

        def is_board_full():
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    if board[row][col] == 0:
                        return False
            return True

        def check_win(player):
            for col in range(BOARD_COLS):
                if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                    draw_vertical_winning_line(col, player)
                    return True
            for row in range(BOARD_ROWS):
                if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                    draw_horizontal_winning_line(row, player)
                    return True
            if board[2][0] == player and board[1][1] == player and board[0][2] == player:
                draw_asc_diagonal(player)
                return True
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                draw_desc_diagonal(player)
                return True
            return False

        def draw_vertical_winning_line(col, player):
            posX = col * SQUARE_SIZE + SQUARE_SIZE // 2
            if player == 1:
                color = CIRCLE_COLOR
            elif player == 2:
                color = circle_color
            pygame.draw.line(screen, color, (posX, 150), (posX, HEIGHT - 115), LINE_WIDTH)

        def draw_horizontal_winning_line(row, player):
            posY = row * SQUARE_SIZE + SQUARE_SIZE // 2
            if player == 1:
                color = CIRCLE_COLOR
            elif player == 2:
                color = circle_color
            pygame.draw.line(screen, color, (150, posY), (WIDTH - 115, posY), WIN_LINE_WIDTH)

        def draw_asc_diagonal(player):
            if player == 1:
                color = CIRCLE_COLOR
            elif player == 2:
                color = circle_color
            pygame.draw.line(screen, color, (120, 681), (688, 130), WIN_LINE_WIDTH)

        def draw_desc_diagonal(player):
            if player == 1:
                color = CIRCLE_COLOR
                pygame.draw.line(screen, color, (120, 130), (688, 681), WIN_LINE_WIDTH)
            elif player == 2:
                color = circle_color
                pygame.draw.line(screen, color, (120, 130), (688, 681), WIN_LINE_WIDTH)

        def restart():
            draw_lines()
            for row in range(BOARD_ROWS):
                for col in range(BOARD_COLS):
                    board[row][col] = 0

        draw_lines()
        player = 1
        game_over = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)
                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)
                        if check_win(player):
                            game_over = True
                        player = player % 2 + 1
                        red(), yellow()

            pygame.display.update()

    def about_game():

        pygame.init()

        scr = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("SET")
        pygame.display.set_icon(scr)
        bg = pygame.image.load(r"/Users/ajayjayakumar/Desktop/Ajay/setde.png")
        scr.blit(bg, (0, 0))
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # deactivates the pygame library
                    pygame.quit()
                    # quit the program.
                    quit()

                pygame.display.update()
                # hint last
    menu = pygame_menu.Menu('Welcome', 800, 800, theme=pygame_menu.themes.THEME_DARK)
    pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE
    pygame.display.set_caption('SET')
    menu.add.button('Play', start_the_game)
    menu.add.button('Hint', about_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)


photo = PhotoImage(file=r"/Users/ajayjayakumar/Desktop/Ajay/output-onlinepngtools (3).png")
photo2 = PhotoImage(file=r"/Users/ajayjayakumar/Desktop/Ajay/challenging Ball.png")

label = Label(master)

    # a button widget which will open a
    # new window on button click00
button = Button(master,
                image=photo,
                command=openNewWindow)
button.pack(pady=12)
button.place(x=400, y=350)
button2 = Button(master,
                     image=photo2,
                     command=open2NewWindow)
button2.pack(pady=12)
button2.place(x=250, y=350)

mainloop()