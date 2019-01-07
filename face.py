'''
   Face.py
   Nicole Binder 13 October 2018

'''

from graphics import *

def main():
    window = GraphWin('Draw A Face', 500, 500)
    
    

    head = Circle(Point(250,250), 100)
    head_color = color_rgb(0, 0, 0)
    head.setOutline(head_color)
    head_fill_color = color_rgb(215,135,175)
    head.setFill(head_fill_color)
    
    eye1 = Circle(Point(220,220), 20)
    eye2 = Circle(Point(280,220), 20)
    eye_color = color_rgb(0, 0, 0)
    eye1.setOutline(eye_color)
    eye2.setOutline(eye_color)
    eye_fill_color = 'white'
    eye1.setFill(eye_fill_color)
    eye2.setFill(eye_fill_color)
    
    iris1 = Oval(Point(205,235), Point(235,210))
    iris2 = Oval(Point(265,235), Point(295,210))
    iris_color = color_rgb(135,175,95)
    iris1.setOutline(iris_color)
    iris2.setOutline(iris_color)
    iris_fill_color = color_rgb(135,175,95)
    iris1.setFill(iris_fill_color)
    iris2.setFill(iris_fill_color)
    
    pupil1 = Circle(Point(220,225), 8)
    pupil2 = Circle(Point(280,225), 8)
    pupil_color = 'black'
    pupil1.setOutline(pupil_color)
    pupil2.setOutline(pupil_color)
    pupil1.setFill(pupil_color)
    pupil2.setFill(pupil_color)
    
    mouth = Polygon(Point(220, 280), Point(280,280), Point(270, 295), Point(230, 295))
    mouth.setFill(pupil_color)
    teeth = Polygon(Point(240, 280), Point(260,280), Point(260, 290), Point(240, 290))
    teeth.setFill(eye_fill_color)
    
    eyebrow1 = Polygon(Point(220,185), Point(240,180), Point(200,190))
    eyebrow2 = Polygon(Point(280,185), Point(300,190), Point(260,180))
    eyebrow_color = color_rgb(8,8,8)
    eyebrow1.setOutline(eyebrow_color)
    eyebrow1.setFill(eyebrow_color)
    eyebrow2.setOutline(eyebrow_color)
    eyebrow2.setFill(eyebrow_color)
    
    head.draw(window)
    eye1.draw(window)  
    eye2.draw(window)
    iris1.draw(window)
    iris2.draw(window)
    pupil1.draw(window)
    pupil2.draw(window)
    mouth.draw(window)
    eyebrow1.draw(window)
    eyebrow2.draw(window)
    teeth.draw(window)
    
    
    print('Hit any key to quit')
    keyResponse = window.getKey()
    print('You hit', keyResponse)

main()
