'''
John Groos and Nicole Binder
CS 111 Final Project
An "undefeatable" game of tic-tac-toe
'''
from graphics import *
import time

def gametime(window, color_1, color_2, color_3):
    #draws board
    window = GraphWin("Tic-Tac-Toe", 600, 600)
    window.setBackground(color_1)
    window.setCoords(0, 0, 600, 600)

    #draws Board Lines
    board_line_1  = Rectangle(Point(195, 25), Point(205, 575))
    board_line_2 = Rectangle(Point(395, 25), Point(405, 575))
    board_line_3 = Rectangle(Point(25, 195), Point(575, 205))
    board_line_4 = Rectangle(Point(25, 395), Point(575, 405))
    board_line_1.setFill(color_3)
    board_line_2.setFill(color_3)
    board_line_3.setFill(color_3)
    board_line_4.setFill(color_3)
    board_line_1.setOutline(color_3)
    board_line_2.setOutline(color_3)
    board_line_3.setOutline(color_3)
    board_line_4.setOutline(color_3)
    board_line_1.draw(window)
    board_line_2.draw(window)
    board_line_3.draw(window)
    board_line_4.draw(window)

    # sets starting moves, row1-3 list keep track of actual position, score lists keep tracks of # in rows
    movelist = []
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    count = 1
    row_x_scores = [0, 0 , 0]
    column_x_scores = [0, 0 , 0]
    diagonal_x_scores = [0, 0]
    row_o_scores = [0, 0 , 0]
    column_o_scores = [0, 0 , 0]
    diagonal_o_scores = [0, 0]

    game_play = True

    while game_play == True:
        x = 1 #changed to zero is user clicks in a filled position
        if count % 2 == 1:
            move_point = window.getMouse()
            x_value = move_point.getX()
            y_value = move_point.getY()
            if x_value <= 200 and y_value <= 200:
                move = 7
            elif x_value <= 400 and y_value <= 200:
                move = 8
            elif x_value <= 600 and y_value <= 200:
                move = 9
            elif x_value <= 200 and y_value <= 400:
                move = 4
            elif x_value <= 400 and y_value <= 400:
                move = 5
            elif x_value <= 600 and y_value <= 400:
                move = 6
            elif x_value <= 200 and y_value <= 600:
                move = 1
            elif x_value <= 400 and y_value <= 600:
                move = 2
            elif x_value <= 600 and y_value <= 600:
                move = 3
            if move in movelist:
                x = 0
            if x == 1:
                if move == 1:
                    row1[0] = "X"
                    draw_player1(move, window)
                    row_x_scores[0] += 1
                    column_x_scores[0] += 1
                    diagonal_x_scores[0] += 1
                if move == 2:
                    row1[1] = "X"
                    draw_player1(move, window)
                    row_x_scores[0] += 1
                    column_x_scores[1] += 1
                if move == 3:
                    row1[2] = "X"
                    draw_player1(move, window)
                    row_x_scores[0] += 1
                    column_x_scores[2] += 1
                    diagonal_x_scores[1] += 1
                if move == 4:
                    row2[0] = "X"
                    draw_player1(move, window)
                    row_x_scores[1] += 1
                    column_x_scores[0] += 1
                if move == 5:
                    row2[1] = "X"
                    draw_player1(move, window)
                    row_x_scores[1] += 1
                    column_x_scores[1] += 1
                    diagonal_x_scores[0] += 1
                    diagonal_x_scores[1] += 1
                if move == 6:
                    row2[2] = "X"
                    draw_player1(move, window)
                    row_x_scores[1] += 1
                    column_x_scores[2] += 1
                if move == 7:
                    row3[0] = "X"
                    draw_player1(move, window)
                    row_x_scores[2] += 1
                    column_x_scores[0] += 1
                    diagonal_x_scores[1] += 1
                if move == 8:
                    row3[1] = "X"
                    draw_player1(move, window)
                    row_x_scores[2] += 1
                    column_x_scores[1] += 1
                if move == 9:
                    row3[2] = "X"
                    draw_player1(move, window)
                    row_x_scores[2] += 1
                    column_x_scores[2] += 1
                    diagonal_x_scores[0] += 1
                movelist.append(move)
                count += 1
            for column in range(3):
                if row_x_scores[column] == 3:
                    player1_wins(window)
                elif column_x_scores[column] == 3:
                    player1_wins(window)
            for column in range(2):
                if diagonal_x_scores[column] == 3:
                    player1_wins(window)
            if len(movelist) == 9:
                tie_game(window)
        if count % 2 == 0:
            if 5 not in movelist:
                move = 5
            if 5 in movelist:
                if row_x_scores[0] == 2:
                    for i in range(3):
                        if row1[i] == " ":
                            move = i + 1
                if row_x_scores[1] == 2:
                    for i in range(3):
                        if row2[i] == " ":
                            move = i + 4
                if row_x_scores[2] == 2:
                    for i in range(3):
                        if row3[i] == " ":
                            move = i + 7
                if column_x_scores[0] == 2:
                    if row1[0] == " ":
                        move = 1
                    if row2[0] == " ":
                        move = 4
                    if row3[0] == " ":
                        move = 7
                if column_x_scores[1] == 2:
                    if row1[1] == " ":
                        move = 2
                    if row2[1] == " ":
                        move = 5
                    if row3[1] == " ":
                        move = 8
                if column_x_scores[2] == 2:
                    if row1[2] == " ":
                        move = 3
                    if row2[2] == " ":
                        move = 6
                    if row3[2] == " ":
                        move = 9
                if diagonal_x_scores[0] == 2:
                    if row1[0] == " ":
                        move = 1
                    if row2[1] == " ":
                        move = 5
                    if row3[2] == " ":
                        move = 9
                if diagonal_x_scores[1] == 2:
                    if row1[2] == " ":
                        move = 3
                    if row2[1] == " ":
                        move = 5
                    if row3[0] == " ":
                        move = 7
                if row_o_scores[0] == 2:
                  for i in range(3):
                      if row1[i] == " ":
                          move = i + 1
                if row_o_scores[1] == 2:
                  for i in range(3):
                      if row2[i] == " ":
                          move = i + 4
                if row_o_scores[2] == 2:
                  for i in range(3):
                      if row3[i] == " ":
                          move = i + 7
                if column_o_scores[0] == 2:
                  if row1[0] == " ":
                      move = 1
                  if row2[0] == " ":
                      move = 4
                  if row3[0] == " ":
                      move = 7
                if column_o_scores[1] == 2:
                  if row1[1] == " ":
                      move = 2
                  if row2[1] == " ":
                      move = 5
                  if row3[1] == " ":
                      move = 8
                if column_o_scores[2] == 2:
                  if row1[2] == " ":
                      move = 3
                  if row2[2] == " ":
                      move = 6
                  if row3[2] == " ":
                      move = 9
                if diagonal_o_scores[0] == 2:
                  if row1[0] == " ":
                      move = 1
                  if row2[1] == " ":
                      move = 5
                  if row3[2] == " ":
                      move = 9
                if diagonal_o_scores[1] == 2:
                  if row1[2] == " ":
                      move = 3
                  if row2[1] == " ":
                      move = 5
                  if row3[0] == " ":
                      move = 7
                if move in movelist:
                    if x == 1:
                        if row2[1] == "X":
                            if row3[2] == "X":
                                if 7 not in movelist:
                                    move = 7
                                    x = 0
                        if row3[1] == "X":
                            if row2[2] == "X":
                                if 7 not in movelist:
                                    move = 7
                                    x = 0
                        if row1[2] == "X":
                            if row3[0] == "X":
                                if 4 not in movelist:
                                    move = 4
                                    x = 0
                    if x == 1:
                        if row1[0] == " ":
                            move = 1
                            x = 0
                    if x == 1:
                        if row1[1] == " ":
                            move = 2
                            x = 0
                    if x == 1:
                        for i in range(3):
                            if row2[i] == " ":
                                move = i + 4
                                x = 0
                    if x == 1:
                        for i in range(3):
                            if row3[i] == " ":
                                move = i + 7
                                x = 0
            if move == 1:
                row1[0] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[0] += 1
                column_o_scores[0] += 1
                diagonal_o_scores[0]+= 1
            elif move == 2:
                row1[1] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[0] += 1
                column_o_scores[1] += 1
            elif move == 3:
                row1[2] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[0] += 1
                column_o_scores[2] += 1
                diagonal_o_scores[1] += 1
            elif move == 4:
                row2[0] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[1] += 1
                column_o_scores[0] += 1
            elif move == 5:
                row2[1] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[1] += 1
                column_o_scores[1] += 1
                diagonal_o_scores[0] += 1
                diagonal_o_scores[1] += 1
            elif move == 6:
                row2[2] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[1] += 1
                column_o_scores[2] += 1
            elif move == 7:
                row3[0] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[2] += 1
                column_o_scores[0] += 1
                diagonal_o_scores[1] += 1
            elif move == 8:
                row3[1] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[2] += 1
                column_o_scores[1] += 1
            elif move == 9:
                row3[2] = "O"
                draw_player2(move, window, color_1, color_2)
                row_o_scores[2] += 1
                column_o_scores[2] += 1
                diagonal_o_scores[0] += 1
            movelist.append(move)
            count += 1
            for column in range(3):
                if row_o_scores[column] == 3:
                    player2_wins(window)
                elif column_o_scores[column] == 3:
                    player2_wins(window)
            for column in range(2):
                if diagonal_o_scores[column] == 3:
                    player2_wins(window)

def replay(window):
    mouse = window.getMouse()
    x = mouse.getX()
    if x >= 0 and x <= 600:
        window.close()
        main()

def draw_player1(move, window):
    #Call function to draw moves in gametime()
    x1 = Point(0, 0)
    y1 = Point(0, 0)
    x1 = Point(0, 0)
    y1 = Point(0, 0)
    if move == 1:
        x1 = Point(25, 425)
        x2 = Point(175, 425)
        y1 = Point(175, 575)
        y2 = Point(25, 575)
    if move == 2:
        x1 = Point(225, 425)
        x2 = Point(375, 425)
        y1 = Point(375, 575)
        y2 = Point(225, 575)
    if move == 3:
        x1 = Point(425, 425)
        x2 = Point(575, 425)
        y1 = Point(575, 575)
        y2 = Point(425, 575)
    if move == 4:
        x1 = Point(25, 225)
        x2 = Point(175, 225)
        y1 = Point(175, 375)
        y2 = Point(25, 375)
    if move == 5:
        x1 = Point(225, 225)
        x2 = Point(375, 225)
        y1 = Point(375, 375)
        y2 = Point(225, 375)
    if move == 6:
        x1 = Point(425, 225)
        x2 = Point(575, 225)
        y1 = Point(575, 375)
        y2 = Point(425, 375)
    if move == 7:
        x1 = Point(25, 25)
        x2 = Point(175, 25)
        y1 = Point(175, 175)
        y2 = Point(25, 175)
    if move == 8:
        x1 = Point(225, 25)
        x2 = Point(375, 25)
        y1 = Point(375, 175)
        y2 = Point(225, 175)
    if move == 9:
        x1 = Point(425, 25)
        x2 = Point(575, 25)
        y1 = Point(575, 175)
        y2 = Point(425, 175)
    draw_half1 = Line(x1, y1)
    draw_half2 = Line(x2, y2)
    line_color = "black"
    draw_half1.setFill(line_color)
    draw_half2.setFill(line_color)
    draw_half1.draw(window)
    draw_half2.draw(window)

def player1_wins(window):
    message = Text(Point(300, 300), "Congratulations, you win!")
    message.setFace("courier")
    message.setSize(24)
    message.setStyle("bold")
    message.setFill("black")
    message.draw(window)
    replay(window)

def draw_player2(move, window, color_1, color_2):
    time.sleep(.2)
    center = Point(0, 0)
    if move == 1:
        center = Point(100, 500)
    if move == 2:
        center = Point(300, 500)
    if move == 3:
        center = Point(500, 500)
    if move == 4:
        center = Point(100, 300)
    if move == 5:
        center = Point(300, 300)
    if move == 6:
        center = Point(500, 300)
    if move == 7:
        center = Point(100, 100)
    if move == 8:
        center = Point(300, 100)
    if move == 9:
        center = Point(500, 100)
    circle = Circle(center, 75)
    middle_circle = Circle(center, 60)
    circle.setFill(color_2)
    circle.setOutline(color_2)
    middle_circle.setFill(color_1)
    middle_circle.setOutline(color_1)
    circle.draw(window)
    middle_circle.draw(window)

def player2_wins(window):
    message = Text(Point(300, 300), "Sorry, the computer wins!")
    message.setFace("courier")
    message.setSize(24)
    message.setStyle("bold")
    message.setFill("black")
    message.draw(window)
    replay(window)

def tie_game(window):
    message = Text(Point(300, 300), "So close, Tie Game!")
    message.setFace("courier")
    message.setSize(24)
    message.setStyle("bold")
    message.setFill("black")
    message.draw(window)
    replay(window)

#Theme Options Window
def set_settings_text(window, name, color_3):
    name.setFace("courier")
    name.setSize(22)
    name.setStyle("bold")
    name.setFill(color_3)
    name.draw(window)

def draw_settings_window(color_1, color_2, color_3):
    settings_window = GraphWin("Settings", 400, 450)
    settings_window.setCoords(0, 0, 400, 450)
    settings_window.setBackground(color_1)
    title = Text(Point(200, 400), " BOARD THEME")
    title.setFace("courier")
    title.setSize(32)
    title.setFill(color_2)
    title.draw(settings_window)
    choice_1 = Text(Point(200, 350), "Default")
    set_settings_text(settings_window, choice_1, color_3)
    choice_2 = Text(Point(200, 300), "Facebook")
    set_settings_text(settings_window, choice_2, color_3)
    choice_3 = Text(Point(200, 250), "Google")
    set_settings_text(settings_window, choice_3, color_3)
    choice_4 = Text(Point(200, 200), "Youtube")
    set_settings_text(settings_window, choice_4, color_3)
    choice_5 = Text(Point(200, 150), "Twitter")
    set_settings_text(settings_window, choice_5, color_3)
    choice_6 = Text(Point(200, 100), "iPhone")
    set_settings_text(settings_window, choice_6, color_3)
    choosing = True
    while choosing is True:
        choice = settings_window.getMouse()
        x = choice.getX()
        y = choice.getY()
        if x <= 350 and x >= 50 and y <= 375 and y > 325:
            color_1 = color_rgb(220, 205, 188)
            color_2 = color_rgb(124, 57, 72)
            color_3 = color_rgb(42, 95, 109)
            choosing = False
        elif x <= 350 and x >= 50 and y <= 325 and y > 275:
            color_1 = color_rgb(247, 247, 247)
            color_2 = color_rgb(59, 89, 152)
            color_3 = color_rgb(139,157,195)
            choosing = False
        elif x <= 350 and x >= 50 and y <= 275 and y > 225:
            color_1 = color_rgb(255, 255, 255)
            color_2 = color_rgb(214, 45, 32)
            color_3 = color_rgb(0, 87, 231)
            choosing = False
        elif x <= 350 and x >= 50 and y <= 225 and y > 175:
            color_1 = color_rgb(241, 241, 241)
            color_2 = color_rgb(204, 24, 30)
            color_3 = color_rgb(102, 102, 102)
            choosing = False
        elif x <= 350 and x >= 50 and y <= 175 and y > 125:
            color_1 = color_rgb(212, 216, 212)
            color_2 = color_rgb(50, 106, 218)
            color_3 = color_rgb(67, 62, 144)
            choosing = False
        elif x <= 350 and x >= 50 and y <= 125 and y > 75:
            color_1 = color_rgb(227, 228, 230)
            color_2 = color_rgb(201, 150, 158)
            color_3 = color_rgb(49, 49, 49)
            choosing = False
    settings_window.close()
    return color_1, color_2, color_3

def main():
    window = GraphWin('TicTacToe', 600, 600)
    window.setCoords(0, 0, 600, 600)
    color_1 = color_rgb(220, 205, 188)
    color_2 = color_rgb(124, 57, 72)
    color_3 = color_rgb(42, 95, 109)
    #draws board lines
    window.setBackground(color_1)
    name = Text(Point(300, 475), "TIC-TAC-TOE")
    name.setFace("courier")
    name.setSize(36)
    name.setFill(color_2)
    name.draw(window)
    welcome = Text(Point(300, 400), "Can You Beat the Computer?")
    welcome.setFace("courier")
    welcome.setSize(22)
    welcome.setStyle("bold")
    welcome.setFill(color_3)
    welcome.draw(window)

    #draws begin playing
    behind_message = Rectangle(Point(50, 200), Point(550, 300))
    behind_message.setFill(color_2)
    message = Text(Point(300, 250), "Click Here to Play!")
    message.setFace("courier")
    message.setSize(22)
    message.setFill(color_1)
    behind_message.draw(window)
    message.draw(window)

    settings = Text(Point(300, 75), "themes")
    settings.setSize(18)
    settings.setFace("courier")
    settings.setStyle("bold")
    settings.setFill(color_3)
    settings.draw(window)

    waiting = True
    while waiting is True:
        window.setBackground(color_1)
        name.setFill(color_2)
        welcome.setFill(color_3)
        behind_message.setFill(color_2)
        message.setFill(color_1)
        mouse_click = window.getMouse()
        x = mouse_click.getX()
        y = mouse_click.getY()
        if x <= 550 and x >= 50 and y <= 315 and y >= 175:
            waiting = False
            window.close()
            gametime(window, color_1, color_2, color_3)
        elif x <= 400 and x >= 300 and y <= 100 and y >= 25:
            color_1, color_2, color_3 = draw_settings_window(color_1, color_2, color_3)
main()
