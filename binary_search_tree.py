class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # Constructor just assigns an empty root.
    def __init__(self):
        self.root = None

    # Search for a node containing a matching key. Returns the
    # Node object that has the matching key if found, None if
    # not found.
    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node
                
            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left
                
            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_node = current_node.right
      
        # The key was not found in the tree.
        return None

    # Inserts the new node into the tree.
    def insert(self, node):

        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None: 
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right       
   
    # Removes the node with the matching key from the tree.
    def remove(self, key):
        # Public remove method. Avg runtime O(h)
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, current_node, key):
        # Recursive helper to remove a node
        # Avg runtime O(h)
        if current_node is None:
            return None

        if key < current_node.key:
            # Key is in the left subtree.
            current_node.left = self._remove_recursive(current_node.left, key)
        elif key > current_node.key:
            # Key is in the right subtree.
            current_node.right = self._remove_recursive(current_node.right, key)
        else:
            # Found the node to remove.

            # Case 1: no children.
            if current_node.left is None and current_node.right is None:
                return None

            # Case 2: one child (right only).
            if current_node.left is None:
                return current_node.right

            # Case 3: one child (left only).
            if current_node.right is None:
                return current_node.left

            # Case 4: two children.
            # Find inorder successor (smallest in right subtree).
            successor = self._find_min(current_node.right)
            # Copy successor's key and value into current node.
            current_node.key = successor.key
            current_node.value = successor.value
            # Remove the successor from the right subtree.
            current_node.right = self._remove_recursive(current_node.right, successor.key)

        return current_node

    def _find_min(self, node):
        # Find smallest key in a subtree
        # Worst runtime O(h)
        while node.left is not None:
            node = node.left
        return node
    
    def inorder_traversal(self, node, visit):
    # Inorder is left -> node -> right 
    # Runtime O(n) because each node is visited once
        if node is not None:
            self.inorder_traversal(node.left, visit)   # visit left subtree
            visit(node)                                # process current node
            self.inorder_traversal(node.right, visit)  # visit right subtree

    def preorder_traversal(self, node, visit):
        # Preorder is node -> left -> right 
        # Runtime O(n) for a full tree traversal
        if node is not None:
            visit(node)                                # process current node first
            self.preorder_traversal(node.left, visit)  # visit left subtree
            self.preorder_traversal(node.right, visit) # visit right subtree

    def postorder_traversal(self, node, visit):
        # Postorder is left -> right -> node 
        # Runtime O(n) because each node is visited once.
        if node is not None:
            self.postorder_traversal(node.left, visit)  # visit left subtree
            self.postorder_traversal(node.right, visit) # visit right subtree
            visit(node)                                 # process node after children
