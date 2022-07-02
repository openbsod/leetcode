class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        btp = []

        def dfs(root, s):
            if not root.left and not root.right:
                return btp.append(s + str(root.val))
            if root.left:
                dfs(root.left, s + str(root.val) + '->')
            if root.right:
                dfs(root.right, s + str(root.val) + '->')

        dfs(root, "")
        return btp
