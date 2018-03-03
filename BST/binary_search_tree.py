from tree_node import TreeNode


def build_bst(values):
  root = None

  for value in values:
    if root is None:
      root = TreeNode(value)
    else:
      root.insert_node(value)

  return root


def inorder_tree_walk(node, array):
  if node is None:
    return
  inorder_tree_walk(node.left(), array)
  array.append(node.value())
  inorder_tree_walk(node.right(), array)


def preorder_tree_walk(node, array):
  if node is None:
    return
  array.append(node.value())
  inorder_tree_walk(node.left(), array)
  inorder_tree_walk(node.right(), array)


def postorder_tree_walk(node, array):
  if node is None:
    return
  inorder_tree_walk(node.left(), array)
  inorder_tree_walk(node.right(), array)
  array.append(node.value())


def construct_from_inorder_preorder(inorder, preorder):
  if len(inorder) == 0 or len(preorder) == 0:
    return None
  node = TreeNode(preorder[0])
  pos = inorder.index(preorder[0])
  right_tree_index = pos + 1

  node.set_left(construct_from_inorder_preorder(inorder[:pos], preorder[1:(pos + 1)]))
  node.set_right(construct_from_inorder_preorder(inorder[right_tree_index:], preorder[right_tree_index:]))
  return node


values = [6, 5, 3, 2, 4, 8, 7, 9]
inorder = []
preorder = []
bst = build_bst(values)
inorder_tree_walk(bst, inorder)
preorder_tree_walk(bst, preorder)

print(inorder)
print(preorder)

reconstructed_tree = construct_from_inorder_preorder(inorder, preorder)
new_inorder = []
new_preorder = []
inorder_tree_walk(reconstructed_tree, new_inorder)
preorder_tree_walk(reconstructed_tree, new_preorder)

print(new_inorder)
print(new_preorder)

