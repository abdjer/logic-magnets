
import random  
from moving import *


def create_zero_matrix(n):  
    return [[0 for _ in range(n)] for _ in range(n)]  

def generate_black(game_board_matrix, count):  
    n = len(game_board_matrix)  
    for _ in range(count):  
        while True:  # حلقة للتحقق من عدم التداخل  
            x = random.randint(0, n - 1)  
            y = random.randint(0, n - 1)  
            if game_board_matrix[x][y] == 0:  
                game_board_matrix[x][y] = "B"   
                break   

def generate_magnets(game_board_matrix):  
    n = len(game_board_matrix)  
    while True:  
        pinkX = random.randint(0, n - 1)  
        pinkY = random.randint(0, n - 1)  
        if game_board_matrix[pinkX][pinkY] == 0:  
            game_board_matrix[pinkX][pinkY] = "P"   
            break  
        
    while True:  
        redX = random.randint(0, n - 1)  
        redY = random.randint(0, n - 1)  
        if game_board_matrix[redX][redY] == 0:  
            game_board_matrix[redX][redY] = "R"  
            break  

def generate_goal(game_board_matrix, count):  
    n = len(game_board_matrix)  
    for _ in range(count):  
        while True:  
            x = random.randint(0, n - 1)  
            y = random.randint(0, n - 1)  
            if game_board_matrix[x][y] == 0:  
                game_board_matrix[x][y] = "G" 
                goal_matrix[x][y] = "G" 
                break   

def check(game_board_matrix):  
    for row in game_board_matrix:  
        for item in row:  
            if item == 'G':  
                return False  
    return True        


# قراءة طول المصفوفة  
n = int(input('Enter length of matrix: '))  
#n=4
game_board_matrix = create_zero_matrix(n) 
goal_matrix = create_zero_matrix(n)   
count = random.randint(1, n)  

generate_black(game_board_matrix, count)  
generate_goal(game_board_matrix, count + 2)  
generate_magnets(game_board_matrix)  

printing(game_board_matrix,goal_matrix)  

# for row in goal_matrix:      
#      print(row)  
# عد الأهداف و البلاك  
goalcnt = sum(row.count("G") for row in game_board_matrix)  
blackcnt = sum(row.count("B") for row in game_board_matrix) + 2   

print("Goal count: " + str(goalcnt))  
print("Black count: " + str(blackcnt))  
print("Count: " + str(count))  



while not check(game_board_matrix):  
# قراءة إحداثيات الحركة  
   
    piece = input('Enter the piece that you want to move: ').upper()   

    for row_index, row in enumerate(game_board_matrix):  
        for col_index, item in enumerate(row):   
            if str(item) == str(piece):  
                print(f"Coordinates of {piece}: ({row_index}, {col_index})")  
                game_board_matrix[row_index][col_index] = 0  
                if goal_matrix[row_index][col_index]=="G":
                    game_board_matrix[row_index][col_index] ="G"
#عنا كورنيل كيس ازا الحركة مرفوضة
    coordinates = input("Enter the coordinates of the location you want to move to.(like x,y): ")   
    x, y = map(int, coordinates.split(','))  
    if 0 <= x < n and 0 <= y < n:  
        if game_board_matrix[x][y] == 0 or game_board_matrix[x][y] == 'G' or game_board_matrix[x][y] == '0' :  
               game_board_matrix[x][y] = piece  # نقل القطعة إلى الموقع الجديد  
       
        else:  
             print("Invalid move: The destination cell is not empty.")
             continue
    else:  
        print("Invalid move: Coordinates out of bounds.")
        continue  

    if piece=="P":
        game_board_matrix =apply_repulsion(game_board_matrix, x,y)
    if piece=="R":
        game_board_matrix =apply_attraction(game_board_matrix, x,y)
        
    # طباعة المصفوفة بعد الحركة  
    printing(game_board_matrix,goal_matrix)
print("All goals have been reached!")