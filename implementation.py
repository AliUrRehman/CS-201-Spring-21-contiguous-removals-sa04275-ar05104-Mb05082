# BufferTree node
class BufferTreeNode: #this tree will perform all operations in a Top Down approach
    def __init__(self, leaf=False):
        self.leaf = leaf #This flag will tell that it is leaf node or not
        self.keys = []
        self.child = []
        self.buffer = [] #buffer used to store the data


class BufferTree:
    def __init__(self, t):
        self.root = BufferTreeNode(True)
        self.t = t
        self.nodeswithbuffer = dict()

    # Insert a key
    def insert(self, k):
        root = self.root #saving root for replacement with new node
        if len(root.keys) == (4 * self.t) - 1: #if buffer is full
            temp = BufferTreeNode() # make new node
            self.root = temp #make new node as root of tree
            temp.child.insert(0, root) #insert old root to the child of new root
            self.split_child(temp, 0) #split new node which is current root
            self.insert_non_full(temp, k) # call insert on non full node again
        else:
            self.insert_non_full(root, k)
