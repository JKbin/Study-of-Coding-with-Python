info = [0,0,1,1,1,0,1,0,1,0,1,1]	
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	



def solution(info, edges):
    answer = 0
    
    def nextNodes(v):
        temp = list()
        for e in edges:
            i,j = e         # i : 부모, j : 자식
            
            if v == i:
                temp.append(j)
        return temp
            
    
    
    def dfs(sheep,wolf,current,path):
        
        if info[current] == 1:
            wolf += 1
        else:
            sheep += 1
            
        if wolf >= sheep:
            return 0
        
        maxSheep = sheep
        
        for p in path:
            for n in nextNodes(p):
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep,dfs(sheep,wolf,n,path))
                    path.pop()
        return maxSheep
    
                
                
        
    
    
    answer = dfs(0,0,0,[0])
    
    
    
    
    
    
    
    
    
    return answer


print(solution(info,edges))
