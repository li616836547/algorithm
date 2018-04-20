class TreeNode(object):
    """
    二叉树
    data:节点的值
    left:左子树
    right: 右子树
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __len__(self):
        t = self
        return TreeNode._length(t)

    @ staticmethod
    def _length(t):
        if t is None:
            return 0
        else:
            return 1 + TreeNode._length(t.left) + TreeNode._length(t.right)

    @staticmethod
    def print_value(t):
        print(t.data)


class BSTNode(object):
    """二叉排序树（binary search tree）"""
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, data):
        bt = self._root
        if not bt:
            self._root = TreeNode(data)
        while bt:
            entry = bt.data
            if data < entry:
                bt = bt.left
            elif data > entry:
                bt = bt.right
            else:
                return entry
        return None

    def insert(self, data):
        bt = self._root
        if not bt:
            self._root = TreeNode(data)
            return
        while True:
            entry = bt.data
            if data < entry:
                if bt.left is None:
                    bt.left = TreeNode(data)
                    return
            elif data > entry:
                if bt.right is None:
                    bt.right = TreeNode(data)
                    return
            else:
                return



# 前序遍历
def preorder(t, fun=TreeNode.print_value):
    if t is None:
        return
    fun(t)
    preorder(t.left)
    preorder(t.right)
# 中序遍历
def midorder(t, fun=TreeNode.print_value):
    if not t:
        return
    midorder(t.left)
    fun(t)
    midorder(t.right)
# 后序遍历
def postorder(t, fun=TreeNode.print_value):
    if not t:
        return
    postorder(t.left)
    postorder(t.right)
    fun(t)
# 层序遍历(宽度优先搜索)
def levelorder(t, fun=TreeNode.print_value):
    if not t:
        return
    queue = [t]
    while queue:
        now = queue.pop()
        fun(now)
        if now.left:
            queue.append(now.left)
        if now.right:
            queue.append(now.right)



if __name__ == '__main__':
    t = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), None))