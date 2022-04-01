import sys
# 백준 1991

input = sys.stdin.readline


n = int(input().rstrip())

tree = {}

for i in range(n):
    root,left,right = map(str,input().rstrip().split())
    tree[root] = [left,right]

# 전위순회
def preorder(root):
    if root != '.':
        print(root,end='')          # root
        preorder(tree[root][0])     # left
        preorder(tree[root][1])     # left
        
# 중위순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])      # left
        print(root,end='')          # root
        inorder(tree[root][1])      # right
    
# 후위순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])      # left
        postorder(tree[root][1])      # right
        print(root,end='')              # root
        
print(tree)

# preorder('A')
# print()
#inorder('A')
#print()
#postorder('A')

        
        