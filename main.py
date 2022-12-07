# write your code here
import sys


def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20
    else:
        sys.exit()




def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200
    else:
        sys.exit()


def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
    else:
        sys.exit()



def padel_game_cost():
    court_type = str(input("what type of court do you want? indoor or outdoor? \n"))
    racket_brand = str(input("choose racket type: Bullpadel , Nox , Siux \n"))
    ball_boxes = int(input("How many ball boxes do you want? 1 or 2 or 3? \n"))

    print(f"court_type: {court_type}")
    print(f"racket_brand: {racket_brand}")
    print(f"ball_boxes: {ball_boxes}")
    print(f"padel game cost: + {padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)}")


padel_game_cost()

