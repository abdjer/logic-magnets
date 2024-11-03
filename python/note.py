# import random  

# def create_zero_matrix(n):  
#     return [[0 for i in range(n)] for j in range(n)]  

# def generate_black(game_board_matrix, count):  
#     n = len(game_board_matrix)  
#     for _ in range(count):  
#         while True:  # حلقة للتحقق من عدم التداخل  
#             x = random.randint(0, n - 1)  
#             y = random.randint(0, n - 1)  
#             if game_board_matrix[x][y] == 0:  
#                 game_board_matrix[x][y] = "B"   
#                 break   

# def generate_magnets(game_board_matrix):  
#     n = len(game_board_matrix)  
#     while True:  
#         pinkX = random.randint(0, n - 1)  
#         pinkY = random.randint(0, n - 1)  
#         if game_board_matrix[pinkX][pinkY] == 0:  
#             game_board_matrix[pinkX][pinkY] = "P"   
#             break  
        
#     while True:  
#         redX = random.randint(0, n - 1)  
#         redY = random.randint(0, n - 1)  
#         if game_board_matrix[redX][redY] == 0:  
#             game_board_matrix[redX][redY] = "R"  
#             break  

# def generate_goal(game_board_matrix, count):  
#     n = len(game_board_matrix)  
#     for _ in range(count):  
#         while True:  
#             x = random.randint(0, n - 1)  
#             y = random.randint(0, n - 1)  
#             if game_board_matrix[x][y] == 0:  
#                 game_board_matrix[x][y] = "G"  
#                 break   

# # قراءة طول المصفوفة  
# n = int(input('Enter length of matrix: '))   
# game_board_matrix = create_zero_matrix(n)   
# count = random.randint(1, n)  
# generate_black(game_board_matrix, count)  
# generate_goal(game_board_matrix, count + 2)  
# generate_magnets(game_board_matrix)  

# # طباعة المصفوفة  
# for row in game_board_matrix:  
#     print(row)  

# # عد الأهداف و البلاك  
# goalcnt = sum(row.count("G") for row in game_board_matrix)  
# blackcnt = sum(row.count("B") for row in game_board_matrix) + 2  # لأننا أضفنا 2  

# print("Goal count: " + str(goalcnt))  
# print("Black count: " + str(blackcnt))  
# print("Count: " + str(count))  

# # قراءة إحداثيات الحركة  
# piece = input('Enter the piece that you want to move: ').upper()   

# for row_index, row in enumerate(game_board_matrix):  
#     for col_index, item in enumerate(row):   
#         if str(item) == str(piece):  
#             print(f"Coordinates of {piece}: ({row_index}, {col_index})")

# # تعريف رموز الألوان  
# RED = "\033[91m"  
# GREEN = "\033[92m"  
# YELLOW = "\033[93m"  
# BLUE = "\033[94m"  
# RESET = "\033[0m"  # إعادة تعيين اللون إلى الوضع الافتراضي  

# # طباعة نص ملون  
# print(RED + "هذا نص باللون الأحمر" + RESET)  
# print(GREEN + "هذا نص باللون الأخضر" + RESET)  
# print(YELLOW + "هذا نص باللون الأصفر" + RESET)  
# print(BLUE + "هذا نص باللون الأزرق" + RESET)
#####################################################كود شد
# def shift_column(matrix, x, y):  
#     # تحقق من أن الإحداثيات صحيحة  
#     if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):  
#         print("Invalid coordinates.")  
#         return matrix  
    
#     # حفظ قيمة العنصر الحالي في (x, y)  
#     selected_value = matrix[x][y]  

#     # إزاحة العناصر الموجودة فوق النقطة (x, y) إلى الأعلى  
#     for i in range(x - 1, -1, -1):  # ابدأ من الصف الذي فوق x وانزل إلى الصف الأول  
#         matrix[i + 1][y] = matrix[i][y]  

#     # إزاحة العناصر الموجودة تحت النقطة (x, y) إلى الأسفل  
#     for i in range(x + 1, len(matrix)):  # ابدأ من الصف الذي تحت x إلى الصف الأخير  
#         matrix[i - 1][y] = matrix[i][y]  

#     # تعيين القيمة المدخلة في (x, y) إلى المكان الصحيح  
#     matrix[0][y] = selected_value  # تعيين القيمة المحفوظة في الصف الأول  
#     matrix[len(matrix) - 1][y] = selected_value  # تعيين القيمة المحفوظة في الصف الأخير  

#     return matrix  

# # اختبار تابع الإزاحة  
# matrix = [  
#     [0, 'G', 0, 0, 0],  
#     [0, 0, 0, 'G', 0],  
#     [0, 'P', 0, 0, 0],  
#     ['B', 0, 0, 0, 0],  
#     [0, 0, 'G', 'R', 0]  
# ]  

# x = int(input("Enter row index (x): "))  
# y = int(input("Enter column index (y): "))  

# print("Original value at (x, y):", matrix[x][y])  
# updated_matrix = shift_column(matrix, x, y)  

# # طباعة المصفوفة بعد التحديث  
# for row in updated_matrix:  
#     print(row)
# def apply_attraction(matrix,r_i, r_j ):  
#     rows = len(matrix)  
#     cols = len(matrix[0])  

    

     
#     for i in range(rows):  
#         for j in range(cols):  
#             if matrix[i][j] in ['G', 'B', 'P']:  
#                 if i < r_i:   
#                     matrix[i][j] = '0'  
#                     matrix[r_i - 1][r_j] = matrix[r_i - 1][r_j] if matrix[r_i - 1][r_j] != '0' else matrix[i][j]  
#                 elif i > r_i: 
#                     matrix[i][j] = '0'  
#                     matrix[r_i + 1][r_j] = matrix[r_i + 1][r_j] if matrix[r_i + 1][r_j] != '0' else matrix[i][j]  
#                 elif j < r_j:  # إذا كانت الكتلة إلى اليسار  
#                     matrix[i][j] = '0'  
#                     matrix[r_i][r_j - 1] = matrix[r_i][r_j - 1] if matrix[r_i][r_j - 1] != '0' else matrix[i][j]  
#                 elif j > r_j:  # إذا كانت الكتلة إلى اليمين  
#                     matrix[i][j] = '0'  
#                     matrix[r_i][r_j + 1] = matrix[r_i][r_j + 1] if matrix[r_i][r_j + 1] != '0' else matrix[i][j]  


# matrix = [  
#     [0, 'G', 0, 0, 0],  
#     [0, 0, 0, 'G', 0],  
#     [0, 'P', 0, 0, 0],  
#     ['B', 0, 0, 'R', 0],  
#     [0, 0, 'G', 'R', 0],  
#     [0, 0, 'G', 0, 0]   
# ]  

# print("Matrix before applying attraction:")  
# for row in matrix:  
#     print(row)  

# apply_attraction(matrix,3,3)  

# print("\nMatrix after applying attraction:")  
# for row in matrix:  
#     print(row)