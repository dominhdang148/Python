from os import system
system('cls')
print("Chờ chút nhé...")
from menu import MenuClass
from os import system
choose = 'abc'
menu = MenuClass()
while choose != 0:
    choose=menu.ChonMenu()
    menu.XuLyMenu(choose)
system('cls')
