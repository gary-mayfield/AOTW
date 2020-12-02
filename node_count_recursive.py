class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def getNodeCount(root : Node) -> int:
    if root is None:
        return 0

    count = 0
    count += 1

    count += (getNodeCount(root.left) + getNodeCount(root.right))

    return count

if __name__ == '__main__':
    root = Node(2) 
    root.left = Node(7) 
    root.right = Node(5) 
    root.left.right = Node(6) 
    root.left.right.left = Node(1) 
    root.left.right.right = Node(11) 
    root.right.right = Node(9) 
    root.right.right.left = Node(4) 
    print(f"node count: {getNodeCount(root)}")
