from collections import deque

def bfs(root):
    queue = deque()
    level = 0

    if root:
        queue.append(root)
    
    while len(queue) > 0:
        print("level", level)


        for i in range(len(queue)):
            curr = quque.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


