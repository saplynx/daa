class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

    def __lt__(self, next):
        return self.freq < next.freq
    

def huffmanCoding(freq, chars):
    nodes  = []

    

    while(True):
        freq.sort()

