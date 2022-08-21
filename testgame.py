# import random
# import msvcrt
# from msvcrt import getch
import random
# import readchar
# c = {1:[4, 5], 2: [6, 7]}
# save = []
# for i in c:
#     if c[i][1] == 7:
#         save.append(i)
# x = random.choice(save)
# c[x] = [4, 1]
#
# print(c)

# location_dict[new_head][0] == (2 or 3)

# fruits = ["Apple", "Pear", "Peach", "Banana"]
#
# fruit_dictionary = dict.fromkeys(fruits, "")
# print(fruit_dictionary)

# def mmd():
#     x = 12
#
# b = mmd()
# print(b)

# first_location[(1, 1)], first_location[(1, 2)] = [3, 2], [2, 1]


# def mmd(x):
#     for i in range(10):
#         if i == x:
#             return {7: 8, 3: 5}, 'kir'
#     return {7: 5, 8: 6}, None
#
# n, m = mmd(12)
#
# print(n, m)

# nu = [1,2,3]
# for i in nu:
#     if i == 2:
#         i = "v"
# print(nu)

# print(dir(list))

#
# import emoji
#
# print('\U0001f3fb')
# input()
#
#
# print(emoji.emojize('Python is :thumbs_up:'))


# cd C:\Users\Ron\Desktop\MyPython
# pyinstaller --onefile pythonScriptName.py


# final_fig = []
# for i in range(1,11):
#     for b in range(1, 11):
#         final_fig.append([i, b])
# print(c)

# a = input('').split(" ")[0]
# print(a)
# import sys
# str = ""
# while True:
#     c = sys.stdin.read(1) # reads one byte at a time, similar to getchar()
#     if c == ' ':
#         break
# str += c
# print(str)
#
# z = msvcrt.getch(input())
#
# print('hhh')

#
# import readchar
# print("Reading a char:")
# print(repr(readchar.readchar()))
# print("Reading a key:")
# print(repr(readchar.readkey()))
#
# def getChar():
#     try:
#         # for Windows-based systems
#         import msvcrt # If successful, we are on Windows
#         return msvcrt.getch()
#
#     except ImportError:
#         # for POSIX-based systems (with termios & tty support)
#         import tty, sys, termios  # raises ImportError if unsupported
#
#         fd = sys.stdin.fileno()
#         oldSettings = termios.tcgetattr(fd)
#
#         try:
#             tty.setcbreak(fd)
#             answer = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)
#
#         return answer
# x = getChar()
# print(x)
# input()
# import readchar
# print("Reading a char:")
# x = repr(readchar.readchar()).lower()
# print(x)
# print(type(x))
# if x == 'b\'d\'':
#     print('dd')
#
# input()


# for i in screen:
#     if i%10 == 0:
#         print(i, end="\n")
#     else:
#         if i<10:
#             print(f" {i}", end=" ")
#         else:
#             print(i, end=" ")

#
# from threading import Timer
#
# timeout = 4
# t = Timer(timeout, print, [' '])
# t.start()
# prompt = "You have %d seconds to choose the correct answer...\n" % timeout
# answer = input(prompt)
# t.cancel()
# print('hhh')


# f = [1, 2,3,4]
# cv = f.copy()
# def d(dd):
#     x = dd.pop()
#     return x
#
# z = d(f)
# print(f)
# print(cv)
# f = cv.copy()
# z = d(f)
# print(f)
# print(cv)

# print(dir(dict))
# c = {1:2 , 2:5}
# x = c
# c[1] = 4
# print(c, x)
# move = repr(readchar.readchar())
# print(move)
# import time
# from threading import Thread
#
# answer = None
#
# def check():
#     time.sleep(4)
#     if answer != None:
#         return
#     answer = "w"
#
# Thread(target = check).start()
#
# answer = input("Input something: ")
#
#
# print('jjj')
# print('jjj')
#
# import threading
#
# some_rlock = threading.RLock(4)
#
# with some_rlock:
#     move = input()
#
# print('kkk')

#
# from threading import Timer
#
# out_of_time=False
#
# def time_ran_out():
#     print('You didn\'t answer in time')
#     out_of_time=True
#
# t=Timer(4,time_ran_out)
# t.start()
# user_input= input('Enter something: ')
#
# if user_input!=None and not out_of_time:
#     print('this should appear only if input was given in 4 seconds...')
#     t.cancel()
#
# print('hhh')
#
# import threading, msvcrt
# import sys
#
# def user_input(text, timeout = 5):
#     result=None
#     class KeyboardThread(threading.Thread):
#         def run(self):
#             self.timedout = False
#             self.input = ''
#             while True:
#                 if msvcrt.kbhit():
#                     chr = msvcrt.getche()
#                     if ord(chr) == 13:
#                         self.input+=' '
#                         break
#                     elif ord(chr) >= 32:
#                         self.input += chr
#                 if len(self.input) == 0 and self.timedout:
#                     break
#
#
#     sys.stdout.write('%s:'%(text));
#     it = KeyboardThread()
#     it.start()
#     it.join(timeout)
#     it.timedout = True
#     if len(it.input) > 0:
#         # wait for rest of input
#         it.join()
#         result = it.input
#     return result
#
# # and some examples of usage
# question= input('Enter something here, you have 5 seconds')
# if question!=None:
#     print('\nYou did it!')
# else:
#     print('\nYou failed')
# print('ddd')


#
# from os import system
# from random import choice
# # import time
# # import emoji
# from readchar import readchar
# from threading import Timer
# # ==============================================================================================
#
#
# def game_earth():
#     global game_size
#     game_size = int(input('pleas enter the size of earth game: '))
#     first_location = {}
#     system('cls')
#     for item in range(1, game_size):
#         for item2 in range(1, game_size):
#             first_location[(item, item2)] = [1, 0]
#     first_location[(1, 1)] = [3, 2]
#     first_location[(1, 2)] = [2, 1]
#     return first_location
# # ==============================================================================================
#
#
# def list_maker(list1):
#     global game_size
#     for i in range(1, game_size+1):
#         for b in range(1, game_size+1):
#             list1.append([i, b])
#     return list1
# # ==============================================================================================
#
#
# def apple_location(location_dict_ghably, new_locations):
#     save = []
#     free = []
#     for item in location_dict_ghably:
#         if location_dict_ghably[item][0] == 1:
#             save.append(item)
#     if save == free:
#         return 'won'
#     apple1 = choice(save)
#     new_locations[apple1] = [4, 0]
#     return new_locations
# # ==============================================================================================
#
#
# def head_location(location_dict_ghably, move_key, first_locations, dict_get_from_apple_location):
#     global snake_wide
#     for item in location_dict_ghably:
#         if (location_dict_ghably[item][0] == 3) and (location_dict_ghably[item][1] == 2):
#             snake_neck = list(item)
#         if location_dict_ghably[item][0] == 2:
#             new_head = list(item)
#             new_head_z = new_head.copy()
#     if move_key == 'b\'w\'':
#         new_head[0] -= 1
#     if move_key == 'b\'s\'':
#         new_head[0] += 1
#     if move_key == 'b\'a\'':
#         new_head[1] -= 1
#     if move_key == 'b\'d\'':
#         new_head[1] += 1
#
#     if location_dict_ghably[tuple(new_head)][0] == 2:
#         # cant back the head
#         # breakpoint()
#         e1 = new_head_z[0] - snake_neck[0]
#         e2 = new_head_z[1] - snake_neck[1]
#         if e1 == 1:
#             new_head[0] += 1
#         if e1 == -1:
#             new_head[0] -= 1
#         if e2 == 1:
#             new_head[1] += 1
#         if e2 == -1:
#             new_head[1] -= 1
#     if new_head == snake_neck:
#         new_head = new_head_z.copy()
#         e1 = new_head_z[0] - snake_neck[0]
#         e2 = new_head_z[1] - snake_neck[1]
#         if e1 == 1:
#             new_head[0] += 1
#         if e1 == -1:
#             new_head[0] -= 1
#         if e2 == 1:
#             new_head[1] += 1
#         if e2 == -1:
#             new_head[1] -= 1
#     if not(tuple(new_head) in first_locations):
#         return 'game over', None
#     if location_dict_ghably[tuple(new_head)][0] == 3:
#         if location_dict_ghably[tuple(new_head)][1] == snake_wide:
#             dict_get_from_apple_location[tuple(new_head)] = [2, 1]
#             return dict_get_from_apple_location, None
#         else:
#             return 'game over', None
#     # new_locations_dict = first_locations.copy()
#     if location_dict_ghably[tuple(new_head)][0] == 4:
#         dict_get_from_apple_location[tuple(new_head)] = [2, 1]
#         return dict_get_from_apple_location, 'true'
#     dict_get_from_apple_location[tuple(new_head)] = [2, 1]
#     return dict_get_from_apple_location, None
# # ==============================================================================================
#
#
# def snake_body(location_dict_ghably, arg, new_locations):
#     saver = location_dict_ghably.copy()
#     global snake_wide
#     for item in location_dict_ghably:
#         if location_dict_ghably[item][1] >= 2:
#             body_position = location_dict_ghably[item][1]
#             for item2 in saver:
#                 if saver[item2][1] == (body_position - 1):
#                     new_locations[item2] = [3, body_position]
#                 if (arg == 'true') and (body_position == snake_wide):
#                     snake_wide += 1
#                     new_locations[item2] = [3, snake_wide]
#     return new_locations
# # ==============================================================================================
#
#
# def final_list(new_locations, fig_list_1):
#     final_fig = []
#     for item in fig_list_1:
#         for item2 in new_locations:
#             if tuple(item) == item2:
#                 if new_locations[item2][0] == 1:
#                     final_fig.append('#')
#                     # print('\U0001f3fb')
#                 if new_locations[item2][0] == 2:
#                     final_fig.append('0')
#                 if new_locations[item2][0] == 3:
#                     final_fig.append('-')
#                 if new_locations[item2][0] == 4:
#                     final_fig.append('@')
#     return final_fig
# # ==============================================================================================
#
#
# def draw(final):
#     global game_size
#     counter = 0
#     for item in final:
#         counter += 1
#         if (counter % game_size) == 0:
#             print(item)
#         else:
#             print(item, end='')
# # ==============================================================================================
#
#
# while True:
#     snake_wide = 2
#     game_size = 10
#     fig_list = []
#     difficulty = int(input('enter the difficulty of game(from 1 to 5): '))
#     timing = 1.60 - (difficulty * 0.20)
#     locations = game_earth()
#     first_locations_copy = locations.copy()
#     counter2 = 1
#     fig_list = list_maker(fig_list)
#     fig_list_z = fig_list.copy()
#     fig_list = final_list(locations, fig_list_z)
#     draw(fig_list)
#     while True:
#         if counter2 == 1:
#             old_location_dict = locations.copy()
#             counter2 = 2
#             locations = apple_location(old_location_dict, locations)
#         # t = Timer(timing, print(' '))
#         # t.start()
#         move = repr(readchar()).lower()
#         # t.cancel()
#         # ==================================
#         # move = None
#
#         locations, apple = head_location(old_location_dict, move, first_locations_copy, locations)
#         if locations == 'game over':
#             print("GAME OVER \n play again ")
#             break
#         if apple == 'true':
#             status = apple_location(old_location_dict, status)
#             if status == "won":
#                 print("you Won!! \n  Hora")
#                 break
#         status = snake_body(old_location_dict, apple, status)
#         old_location_dict = status
#         fig_list = final_list(status, fig_list_z)
#         draw(fig_list)
#
#     print('for clean the page and start a new mach press p and for exit press any other key')
#     status2 = repr(readchar()).lower()
#     if status2 == 'b\'p\'':
#         system('cls')
#     else:
#         break


from threading import Timer

timing = 4


# def fuck():
#     print((0/0))
#     # import ursina
# try:
#     t = Timer(timing, fuck)
#     t.start()
#     move = repr(readchar.readchar()).lower()
#     t.cancel()
# except ZeroDivisionError:
#     print("ggg")
#     input("sabr")
#     print("ggg")
# finally:
#     print("hee")
#
# def fuck():
#     pass


# t = Timer(timing, fuck)
# t.start()
# move = repr(readchar.readchar()).lower()
# t.cancel()
# print("dddd")
# input()
# print("sss")


# deeee = {(1,1): 2, (1,0):1}
# s = list(deeee.keys())
# a = list(s.pop())
# print(deeee)
# print(s)

# x = []

# x.insert(s)
# print(x)
# input()

# j = [1,2,3,1,2,4]
# c = set(j)
# print(c)
# v = list(c)
# print(v)

# n = [(1,1), (2,2)]
# c = random.choice(n)
# print(c)

# d = {(1,2):2, (3,4): 5}
# print(len(d))
import tkinter as tk
from tkinter import ttk
import time


        
win =tk.Tk()
la = ttk.Label(win,text="kir")
la.grid(row=0,column=0, padx=25,pady=25)

def ck():
    global item, x
    li = ["Red", "Green", "Blue","Black", "White"]
    x = 0
    
    # win.update()
    # time.sleep(1)
    # for i in range(3):
    #     if x == 1:
    #         break
    #     win.update()
    #     time.sleep(3)
    #     la.configure(background=li[i])
    #     win.createtimerhandler("00","03")
    
    item = 0
    def ff():
        global x
        x = 1

    sal = ttk.Button(win, text="dik", command=ff)
    sal.grid(row=0,column=1)
    win.update()

    def hh():
        global item,x
        print(x,end=" , ")
        
        win.update()
        print(x)
        if x == 1:
            def lk():
                global x
                x =0
                # hh()
            sal.configure(text="un",command=lk)

        else:
            sal.configure(text="pa",command=ff)
            la.configure(background=li[item])
            item += 1

        win.after(5000,hh)        
        # win.update()
        
        
    hh()

s = ttk.Button(win,text="fuck", command=ck)
s.grid(row=1,column=1)
win.mainloop()
