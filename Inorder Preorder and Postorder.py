"""
Standardized Tree Traversal Algorithms

| Algorithm                     | Best Case | Average Case | Worst Case |
|-------------------------------|-----------|--------------|------------|
| Inorder (Recursive & Iterative)   | O(1)      | O(N)         | O(N)       |
| Preorder (Recursive & Iterative)  | O(1)      | O(N)         | O(N)       |
| Postorder (Recursive & Iterative) | O(1)      | O(N)         | O(N)       |
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_recursive(root: TreeNode):
    if root is None:
        return
    inorder_recursive(root.left)
    print(root.val)
    inorder_recursive(root.right)


def postorder_recursive(root: TreeNode):
    if root is None:
        return
    postorder_recursive(root.left)
    postorder_recursive(root.right)
    print(root.val)


def preorder_recursive(root: TreeNode):
    if root is None:
        return
    print(root.val)
    preorder_recursive(root.left)
    preorder_recursive(root.right)

            stack.append(current.right)

    print(" ".join(map(str, output[::-1])))
