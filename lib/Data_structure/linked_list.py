# Node Class 정의
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # 추가 : O(n)
    def append(self, value):
        # 새 node 생성
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # 맨 뒤의 node가 new_node를 가르켜야 한다.
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node
    
    # 추가 : O(1)의 방법, tail version
    def append2(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    
    # get 메서드의 시간복잡도는 : O(n)
    def get(self, idx):
        current = self.head
        # idx만큼 이동
        for _ in range(idx):
            current = current.next
        return current.value

    def get_address(self, idx):
        current = self.head
        # idx만큼 이동
        for _ in range(idx):
            current = current.next
        return current.next
        

    def insert(self, idx, value):
        new_node = Node(value)
        current = self.head
        # 삽입 index - 1까지 반복
        for _ in range(idx-1):
            current = current.next
        # 새로운 노드의 next = index-1의 주소 값
        new_node.next = current.next
        # index-1의 next = 새로운 node의 주소 값
        current.next = new_node
        
    def remove(self, idx):
        current = self.head
        for _ in range(idx-1):
            current = current.next
        next_address = self.get_address(idx)
        current.next = next_address
        
            
    
    
lr = LinkedList()
lr.append(1)
lr.append(2)
lr.append(3)
lr.append(4)
lr.append(5)
print(lr.get(3))            # 4
# [1,2,3,4,5]
lr.remove(3)
# [1,2,3,5]
print(lr.get(3))            # 5





        