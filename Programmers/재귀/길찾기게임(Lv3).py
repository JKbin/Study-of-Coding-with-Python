import sys
sys.setrecursionlimit(10**6)

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	

class Node(object):
    def __init__(self, info):
        self.parent = None
        self.left = None
        self.right = None
        self.data = info[:2]
        self.value = info[2]
        
        
def set_node(parent, current):
    parent_x = parent.data[0]
    current_x = current[0]
    
    if current_x < parent_x:        # left
        if parent.left is None:
            parent.left = Node(current)
        else:
            set_node(parent.left, current)
    elif current_x > parent_x:
        if parent.right is None:
            parent.right = Node(current)
        else:
            set_node(parent.right, current)
    
# 후위순회
def preorder(root):
    result = [root.value]
    
    if root.left:
        result += preorder(root.left)
    if root.right:
        result += preorder(root.right)
    
    return result
    
    
def postorder(root):
    result = []
    
    if root.left:
        result += postorder(root.left)
    if root.right:
        result += postorder(root.right)
    result.append(root.value)
    return result
    
        
def solution(nodeinfo):
    answer = []
    
    n = len(nodeinfo)
    
    # value값 설정
    for i in range(n):
        nodeinfo[i].append(i+1)
        
    # y 값으로 내림차순, x값으로 오름차순 정렬
    nodeinfo.sort(key=lambda x:(-x[1],x[0]))        
    # 8, 6, 7
    
    root = Node(nodeinfo[0])
    
    for i in nodeinfo[1:]:
        set_node(root, i)
        
    preorder_list = preorder(root)
    postorder_list = postorder(root)
    
    return [preorder_list, postorder_list]
    
    
        
    
    
    
        
        
print(solution(nodeinfo))
