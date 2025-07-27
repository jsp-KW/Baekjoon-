import sys

class TrieNode :
    
    def __init__ (self) :
        self.children = dict()
        self.is_terminal = False


class Trie :

    def __init__ (self) :
        self.root = TrieNode()
        self.leaf_count = 0

    
    def insert(self, word) :
        node = self.root
        for ch in word :
            if ch not in node.children :
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
            node.is_terminal = True

    
    def count_prefix(self) :

        def dfs (node) :
            if node.is_terminal and not node.children :
                return 1
            count = 0

            for child  in node.children.values() :
                count+= dfs(child)
            return count
        
        return dfs (self.root)

N = int(sys.stdin.readline())
t = Trie()

for _ in range(N) :
    words = sys.stdin.readline().strip()
    t.insert(words)

print (t.count_prefix())

