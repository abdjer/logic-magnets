from collections import deque  

def bfs(tree, start):  
    vis = []       
    q = deque([start])  
    bfs_tareq = []         
    while q:           
        ver = q.popleft()  
        if ver not in vis:  
            vis.append(ver)    
            bfs_tareq.append(ver)

            for son in tree[ver]:  
                if son not in vis :  
                    q.append(son)  
                # if son >= len(tree):
                #     print("index error:"+str(son))
        print("visited:"+ str(vis))
    return bfs_tareq  

  
tree = [[1], [ 2, 3 ,4], [5], [6, 7], [8, 9], [6], [],[], [9], []]  

start_node = 0
print("BFS starting from node:", start_node)  
print(bfs(tree, start_node))