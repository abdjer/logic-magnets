# def shift_column(matrix, x, y):  
#     # تحقق من أن الإحداثيات صحيحة  
#     if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):  
#         print("Invalid coordinates.")  
#         return matrix  

#     # حفظ القيمة الأصلية  
#     selected_value = matrix[x][y]  

#     # إزاحة العناصر الموجودة فوق (x, y) نحو الأسفل  
#     for i in range(0, x):  
      
#         matrix[i][y]=matrix[i+1][y]
        
#     # إزاحة العناصر الموجودة تحت (x, y) نحو الأعلى  
#     for i in range(x + 1, len(matrix)):
#         print("i:"+str(i))  
#         matrix[i ][y] = matrix[i-1][y]  


#     return matrix  

# # مصفوفة الاختبار  
# matrix = [  
#     [ 0  , 'G' , 0  , 0 , 0],  
#     [ 0  ,  0  , 0  ,'G', 0],  
#     [ 0  , 'P' , 0  , 0 , 0],  
#     ['B' ,  0  , 0  , 0 , 0],  
#     [ 0  ,  0  ,'G' ,'R', 0] ,
#     [ 0  ,  0  ,'G' , 0 , 0] 
# ]  

# x = int(input("Enter row index (x): "))  
# y = int(input("Enter column index (y): "))   

# print("Original value at (x, y):", matrix[x][y])  
# updated_matrix = shift_column(matrix, x, y)  

# # طباعة المصفوفة بعد التحديث  
# for row in updated_matrix:  
#     print(row)
    


# def apply_attraction(matrix, i,j):  
#             rows = len(matrix)  
#             cols = len(matrix[0])  
#             print(str(cols))
  
#             for k in range(i,rows): 
#                 if k>i+1 and ( matrix[k][j] == 'B' or matrix[k][j] == 'P'):  
#                     matrix[k-1][j]= matrix[k][j]
#                     matrix[k][j] = '0'  # تغيير القيمة حسب التنافر  
#                     break 
#             for k in range(i,0,-1):  
#                 # لأسفل  
#                 if k<i-1 and ( matrix[k][j] == 'B' or matrix[k][j] == 'P'):  
#                     matrix[k+1][j] = matrix[k][j] 
#                     matrix[k][j] = '0'  # تغيير القيمة حسب التنافر  
#                     break 
#             for k in range(j,0,-1):    
#                 # لليمين  
#                 if k<j-1 and ( matrix[i][k] == 'B' or matrix[i][k] == 'P'): 
#                     matrix[i][k+1] = matrix[i][k] 
#                     matrix[i][k] = '0'  # تغيير القيمة حسب التنافر  
#             for k in range(j,cols): 
#                 # لليسار  
#                 if k>j+1 and (  matrix[i][k] == 'B' or matrix[i][k] == 'P'):  
#                     matrix[i][k-1]=matrix[i][k]
#                     matrix[i][k] = '0'  # تغيير القيمة حسب التنافر  
#             return matrix



      
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

# apply_attraction(matrix, 3, 1)   

# print("\nMatrix after applying repulsion:")  
# for row in matrix:  
#     print(row)
