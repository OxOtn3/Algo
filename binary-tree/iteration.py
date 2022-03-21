from ast import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# 前序遍历，基于栈
def preorderTraversal(self, root: TreeNode) -> List:
    res = []
    if not root:
        return res
    
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res


# 中序遍历，基于栈
def inorderTraversal(self, root: TreeNode) -> List:
    res = []
    stack = []
    while stack or root:
        # 不断往左子树方向走，每走一次就将当前节点保存到栈中
        # 这是模拟递归的调用
        if root:
            stack.append(root)
            root = root.left
        # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
        # 然后转向右边节点，继续上面整个过程
        else:
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
    return res


# 后序遍历，基于栈
def postorderTraversal(self, root: TreeNode) -> List:
    if not root:
        return []
    
    res = []
    stack = []
    prev = None

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            res.append(root.val)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right
    
    return res