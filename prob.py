import math
import matplotlib.pyplot as plt
import numpy as np


def welcome():
    print("Choose an option")
    print("[1] Manual Tool")
    print("[2] Skadi")
    print("[3] Graph Rolls Over Time")
    print("[4] Exit")
    choice = int(input())
    if choice == 1:
        manual_checker()
    elif choice == 2:
        skadi()
    elif choice == 3:
        automatic_graph()
    elif choice == 4:
        exit()
    else:
        print('Invalid input, please choose the number associated with the tool you wish to use')
        welcome()
    
def design_graph():
    print('X-Axis Label: ')
    xaxis = input()

    print('Y-Axis Label: ')
    yaxis = input()

    print('Title: ')
    title = input()

    plt.style.use('seaborn-whitegrid')

    fig = plt.figure()
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)

    


def traverse():
    print("Back to menu? (y/n)")
    menu = input()
    if menu == 'y' or menu == 'Y':
        welcome()
    else:
        exit()


def manual_checker():
    print("What is the drop rate? (in decimal form): ")
    drop_rate = float(input())

    print("How many times have you attempted it?: ")
    n = int(input())

    #Weird negative rounding error if both steps are done at once
    probability = 1-(math.pow(1-drop_rate, n))
    f_probability = round(probability * 100,1)

    print("You have had a {} percent chance of achieving your drop in {} runs.".format(f_probability, n))

    traverse()

    


def skadi():

    print('Current run count: ')
    runs = int(input())

    print('Current number of characters running Skadi per day: ')
    characters = int(input())

    plt.style.use('seaborn-whitegrid')

    fig = plt.figure()
    plt.xlabel('Rolls')
    plt.ylabel('Percent Chance')


    drop_rate = 0.01  



    

    for i in range(1,runs):
        prob = 1-(math.pow(1-drop_rate, i))
        plt.plot(i,prob*100,'ro')   





    current = round((1-(math.pow(1-drop_rate, runs)))*100,3)
    tomorrow = round((1-(math.pow(1-drop_rate, runs + characters)))*100, 3)

    print('Current odds: {} percent'.format(current))
    print('Tomorrows odds: {} percent'.format(tomorrow))

    plt.show()

    traverse()


def automatic_graph():
    print("What is the drop rate? (in decimal form): ")
    drop_rate = float(input())

    print("How many times have you attempted it?: ")
    n = int(input())

    print('----------------Graph Design--------------')
    print('[1] Accept default graph')
    print('[2] Design your own graph')
    g_choice = int(input())
    if g_choice == 1:
        plt.style.use('seaborn-whitegrid')

        fig = plt.figure()
        plt.xlabel('Rolls')
        plt.ylabel('Percent Chance')
        plt.title('Percent Chance of Obtaining Drop by Each Roll')
    elif g_choice == 2:
        design_graph()
    else:
        print('Invalid input. Accepting defaults...')
        plt.style.use('seaborn-whitegrid')

        fig = plt.figure()
        plt.xlabel('Rolls')
        plt.ylabel('Percent Chance')
        plt.title('Percent Chance of Obtaining Drop by Each Roll')
 

    for i in range(1,n):
        prob = 1-(math.pow(1-drop_rate, i))
        plt.plot(i,prob*100,'ro')

    plt.show()

    traverse()


welcome()








    











