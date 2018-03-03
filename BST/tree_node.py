class TreeNode:
  _value = 0
  _left_child = None
  _right_child = None

  def __init__(self, value):
    self._value = value

  def set_left(self, left_child):
    self._left_child = left_child
  def set_right(self, right_child):
    self._right_child = right_child

  def left(self):
    return self._left_child
  def right(self):
    return self._right_child
  def value(self):
    return self._value

  def insert_node(self, value):
    if value < self._value:
      if self.left() is None:
        self.set_left(TreeNode(value))
      else:
        self.left().insert_node(value)
    else:
      if self.right() is None:
        self.set_right(TreeNode(value))
      else:
        self.right().insert_node(value)
