import nltk
nltk.download('punkt')

# Define the TreeNode class to represent the parse tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        if level == 0:
            print(self.value)
        else:
            print("│    " * (level - 1) + "└───" + self.value)
        
        for child in self.children:
            child.print_tree(level + 1)


# Download the punkt tokenizer if not already present
nltk.download('punkt')

# Define the grammar rules
variable_declaration_cfg = nltk.CFG.fromstring("""
    S -> Statement
    Statement -> Assignment | Conditional | PrintStatement
    Assignment -> 'int' identifier '=' NUMBER ';'
    Assignment -> 'float' identifier '=' NUMBER ';'
    identifier -> 'a' | 'b' | 'c' | 'x' | 'y' | 'z' | 'r'
    NUMBER -> DIGIT | DIGIT DIGITS
    DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    DIGITS -> DIGIT | DIGIT DIGITS
    Conditional -> 'if' '(' identifier '>' NUMBER ')' '{' Statement '}'
    PrintStatement -> 'print' '(' identifier ')' ';'
""")

# Create the parser based on the grammar rules
parser = nltk.ChartParser(variable_declaration_cfg)

# Define the file path
file_path = r'C:\Users\Computec\Desktop\compiler pro\tx.txt'

try:
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line in the file
    for line in lines:
        # Check if the line does not contain the word "float"
        if "float" not in line:
            tokens = nltk.word_tokenize(line.strip())  # Tokenize the line into words

            program_tree = TreeNode("Parse Tree:")  # Create the root node of the parse tree

            for tree in parser.parse(tokens):
                # Convert the NLTK tree into a TreeNode tree structure
                def convert_nltk_tree_to_tree_node(nltk_tree, parent_node):
                    if isinstance(nltk_tree, nltk.Tree):
                        node = TreeNode(nltk_tree.label())
                        parent_node.add_child(node)
                        for child in nltk_tree:
                            convert_nltk_tree_to_tree_node(child, node)
                    else:
                        parent_node.add_child(TreeNode(str(nltk_tree)))

                convert_nltk_tree_to_tree_node(tree, program_tree)
                program_tree.print_tree()  # Print the parse tree in TreeNode format
                
                # Display the tree using NLTK's pretty_print
                tree.pretty_print()
                print("------------------------------------------------------------------------")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


