"""
Time Complexity:
| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Inorder   | O(1)      | O(N)         | O(N)       |
| Preorder  | O(1)      | O(N)         | O(N)       |
| Postorder | O(1)      | O(N)         | O(N)       |

Space Complexity:
| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Inorder   | O(1)      | O(log N)     | O(N)       |
| Preorder  | O(1)      | O(log N)     | O(N)       |
| Postorder | O(1)      | O(log N)     | O(N)       |
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def postorder(root: TreeNode):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)


def preorder(root: TreeNode):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

     
