# Morris遍历

from ast import List


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

        
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    if not root:
        return res
    
    p1 = root
    while p1:
        p2 = p1.left
        if p2:
            while p2.right and p2.right != p1:
                p2 = p2.right
            if not p2.right:
                res.append(p1.val)
                p2.right = p1
                p1 = p1.left
                continue
            else:
                p2.right = None
        else:
            res.append(p1.val)
        p1 = p1.right
    
    return res