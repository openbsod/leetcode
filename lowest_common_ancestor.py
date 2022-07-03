class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printTree(self):
        print(self.data)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        stack = [root]
        parent = {root: None}
        p_not_found = True
        q_not_found = True

        while p_not_found or q_not_found:
            node = stack.pop()
            if node == p: p_not_found = False
            if node == q: q_not_found = False
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
        return q


root = n1 = TreeNode(1)
root.left = n2 = TreeNode(2)
root.right = n3 = TreeNode(3)
root.left.left = n4 = TreeNode(4)
root.left.right = n5 = TreeNode(5)
root.right.left = n6 = TreeNode(6)
root.right.right = n7 = TreeNode(7)
n5.left = n8 = TreeNode(8)
n5.right = n9 = TreeNode(9)

root.printTree
sol = Solution()
"""
print("ans ", sol.lowestCommonAncestor(root, n8, n6).val)
print("ans ", sol.lowestCommonAncestor(root, n4, n5).val)
print("ans ", sol.lowestCommonAncestor(root, n6, n7).val)
"""
