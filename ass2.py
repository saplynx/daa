import heapq

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq

        self.symbol = symbol

        self.left = left

        self.right = right

        self.code = ''

    def __lt__(self, next):
        return self.freq < next.freq
    

def huffmanCoding(chars, freq):
    nodes = []

    for c in range(len(chars)):
        heapq.heappush(nodes, node(freq[c], chars[c]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.code = 0
        right.code = 1

        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

        heapq.heappush(nodes, newNode)

    return nodes


def printNodes(node, val = ''):
    newVal = val + str(node.code)

    if(node.left):
        printNodes(node.left, newVal)

    if(node.right):
        printNodes(node.right, newVal)

    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


def main():
    chars = ['a', 'b', 'c', 'd', 'e', 'f',]

    freq = [5, 9, 12, 13, 16, 45]
    
    nodes = huffmanCoding(chars, freq)

    printNodes(nodes[0])

main()
