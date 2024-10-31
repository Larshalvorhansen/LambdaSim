import os
from anytree import Node, RenderTree

def build_tree(path, parent_node):
    # Loop through each item in the current directory
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        
        # Create a new node for this item
        item_node = Node(item, parent=parent_node)
        
        # If the item is a directory, recursively build the tree
        if os.path.isdir(item_path):
            build_tree(item_path, item_node)

def visualize_folder_structure(folder_path):
    # Create the root node
    root = Node(os.path.basename(folder_path))
    
    # Build the tree starting from the root node
    build_tree(folder_path, root)
    
    # Render the tree
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")

# Set the folder path to the current working directory
folder_path = os.getcwd()
visualize_folder_structure(folder_path)
