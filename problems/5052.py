import sys

class Trie:    
    class Node:
        def __init__(self):
            self.isEnd = False
            self.children = {}

    def __init__(self):
        self.head = self.Node()
    
    def push(self, data):
        return self._push_recursion(data, self.head);

    def _push_recursion(self, data, node):
        # print(node.data, list(node.children))
        if len(data) == 0:
            node.isEnd = True
            return len(node.children) == 0

        if node.isEnd:
            return False

        key = data[0]

        if not (key in node.children):
            node.children[key] =  self.Node()

        return self._push_recursion(data[1:], node.children[key])

def readInt():
    return int(sys.stdin.readline().strip())

trie = Trie()

t = readInt()

for _ in range(t):
    n = readInt()
    trie = Trie()
    flag = True
    for __ in range(n):
        num = sys.stdin.readline().strip()
        if not trie.push(num):
            flag = False
    print("YES" if flag else "NO")
