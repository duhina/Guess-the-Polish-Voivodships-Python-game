This is a python quizz which presuming that there are 16 Voivodships of Poland and every single time you type in the name of a voivodship, then that voivodship gets labelled and you score one point.

In this game I  used turtle and some CSV data. 

There are 4 files: 
1) csv file - contains all 16 Voivodships of Poland by name and then X and Y value. You can change the data and use your own X and Y value using this code for getting mouse tclick coordinates in Python turtle:
 import turtle
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
 
2) gif file - should only be the file in gif format, as turtle only works with this one image format.
3) final_board file - contains a class and a function with a block of code which runs in case if the user guesses all Voivodships correctly.
4) main file.

If user doesn't guess all Voivodships and click "Exit", the code will generate the CSV file which is going to contain just the names of Voivodships which have not been guessed by the user when they exit the game.
