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


def inorder_iterative(root: TreeNode):
    stack, current = [], root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.val)
            current = current.right


def preorder_iterative(root: TreeNode):
    stack = [root]

    while stack:
        current = stack.pop()
        if current:
            print(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


def postorder_iterative(root: TreeNode):
    stack = [root]
    output = []

    while stack:
        current = stack.pop()
        if current:
            output.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

    print(" ".join(map(str, output[::-1])))
