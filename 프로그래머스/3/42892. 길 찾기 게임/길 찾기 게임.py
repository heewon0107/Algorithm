from sys import setrecursionlimit
setrecursionlimit(10000)

class Node(object):
    def __init__(self,info):
        self.num = info[2]
        self.pos = info[:2]
        self.left = None
        self.right = None
        
def insert_node(parent, info):
    if parent.pos[0] > info[0]:
        if parent.left:
            insert_node(parent.left, info)
        else:
            parent.left = Node(info)
    elif parent.pos[0] < info[0]:
        if parent.right:
            insert_node(parent.right, info)
        else:
            parent.right = Node(info)
            
def pre_order(tree):
    result = [tree.num]
    
    if tree.left:
        result += pre_order(tree.left)
    
    if tree.right:
        result += pre_order(tree.right)
    
    return result

def post_order(tree):
    result = []
    
    if tree.left:
        result += post_order(tree.left)
    if tree.right:
        result += post_order(tree.right)
        
    result.append(tree.num)
    return result

def solution(nodeinfo):
    nodeinfo = sorted([(x, y, idx+1) for idx, (x, y) in enumerate(nodeinfo)], key=lambda x: (-x[1], x[0]))
    tree = Node(nodeinfo[0])    
    
    for info in nodeinfo[1:]:
        insert_node(tree, info)
    
    
    answer = []
    answer.append(pre_order(tree))
    answer.append(post_order(tree))
    
    return answer