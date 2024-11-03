#moving.py


# تعريف رموز الألوان  
RED = "\033[91m"  
GREEN = "\033[92m"  
YELLOW = "\033[93m"  
BLUE = "\033[94m"
PURPLE = "\033[95m"
LIGHT_GRAY = "\033[37m" 
BLACK = "\033[90m"   
RESET = "\033[0m"   


def apply_repulsion(matrix, i,j):  
                rows = len(matrix)  
                cols = len(matrix[0])  
                print(str(cols))
  
                # التحقق من الاتجاهات الأربعة  
                # لأعلى  
                if i > 1 and ( matrix[i-1][j] == 'B' or matrix[i-1][j] == 'R'):  
                    matrix[i-2][j]= matrix[i-1][j]
                    matrix[i-1][j] = '0'  # تغيير القيمة حسب التنافر  
            
                # لأسفل  
                if i < rows - 1 and ( matrix[i+1][j] == 'B' or matrix[i+1][j] == 'R'):  
                    matrix[i+2][j] = matrix[i+1][j] 
                    matrix[i+1][j] = '0'  # تغيير القيمة حسب التنافر  
            
                # لليمين  
                if j < cols - 1 and ( matrix[i][j+1] == 'B' or matrix[i][j+1] == 'R'): 
                    matrix[i][j+2] = matrix[i][j+1] 
                    matrix[i][j+1] = '0'  # تغيير القيمة حسب التنافر  
            
                # لليسار  
                if j > 1 and (  matrix[i][j-1] == 'B' or matrix[i][j-1] == 'R'):  
                    matrix[i][j-2]=matrix[i][j-1]
                    matrix[i][j-1] = '0'  # تغيير القيمة حسب التنافر  
                return matrix
 


def apply_attraction(matrix, i,j):  
            rows = len(matrix)  
            cols = len(matrix[0])  
            print(str(cols))
  
            for k in range(i,rows): 
                if k>i+1 and ( matrix[k][j] == 'B' or matrix[k][j] == 'P'):  
                    matrix[k-1][j]= matrix[k][j]
                    matrix[k][j] = '0'  # تغيير القيمة حسب التنافر  
                    break 
            for k in range(i,0,-1):  
                # لأسفل  
                if k<i-1 and ( matrix[k][j] == 'B' or matrix[k][j] == 'P'):  
                    matrix[k+1][j] = matrix[k][j] 
                    matrix[k][j] = '0'  # تغيير القيمة حسب التنافر  
                    break 
            for k in range(j,0,-1):    
                # لليمين  
                if k<j-1 and ( matrix[i][k] == 'B' or matrix[i][k] == 'P'): 
                    matrix[i][k+1] = matrix[i][k] 
                    matrix[i][k] = '0'  # تغيير القيمة حسب التنافر  
            for k in range(j,cols): 
                # لليسار  
                if k>j+1 and (  matrix[i][k] == 'B' or matrix[i][k] == 'P'):  
                    matrix[i][k-1]=matrix[i][k]
                    matrix[i][k] = '0'  # تغيير القيمة حسب التنافر  
            return matrix

def printing(game_board_matrix,goal_matrix):
      for row_index, row in enumerate(game_board_matrix):  
        colored_row = ""  
        for col_index, item in enumerate(row):     
            if  goal_matrix[row_index][col_index] =="G":
                colored_row += GREEN + str(item) + " " + RESET 
            else:  
                if item == "B":  
                    colored_row += BLACK + str(item)+ " " + RESET  
                elif item == "G":  
                    colored_row += str(item) + " "   
                elif item == "P":  
                    colored_row += PURPLE + str(item) + " " + RESET  
                elif item == "R":  
                    colored_row += RED + str(item) + " " + RESET  
                else:  
                    colored_row += str(item) + " "  
    
        print(colored_row)



      
# matrix = [  
#     [ 0  , 'G' , 0  , 0 , 0],  
#     [ 0  ,  0  , 0  ,'G', 0],  
#     [ 0  , 'P' , 0  , 0 , 0],  
#     ['B' ,  0  , 0  ,'P' , 0],  
#     [ 0  ,  0  ,'G' ,'R', 0] ,
#     [ 0  ,  0  ,'G' , 0 , 0] 
# ]  

# print("Matrix before applying repulsion:")  
# for row in matrix:  
#     print(row)  

# apply_repulsion(matrix, 2, 0)   

# print("\nMatrix after applying repulsion:")  
# for row in matrix:  
#     print(row)
