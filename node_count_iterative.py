class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def getNodeCount(root : Node) -> int:
    if root is None:
        return 0

    queue = []

    queue.append(root)

    count = 0
    while(len(queue) > 0):
        node = queue.pop(0)

        count += 1

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

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
