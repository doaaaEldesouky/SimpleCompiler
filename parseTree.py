import nltk
nltk.download('punkt')

# تعريف الفئة TreeNode لتمثيل شجرة التحليل
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


# تنزيل مكتبة punkt إذا لم تكن موجودة
nltk.download('punkt')

# تعريف القواعد النحوية (الجرامر)
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

# إنشاء المحلل بناءً على القواعد النحوية
parser = nltk.ChartParser(variable_declaration_cfg)

# تحديد مسار ملف النصوص
file_path = r'C:\Users\Computec\Desktop\compiler pro\tx.txt'

try:
    # قراءة محتويات الملف
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # معالجة كل سطر في الملف
    for line in lines:
        # التحقق من السطر إذا كان يحتوي على كلمة "float"
        if "float" not in line:
            tokens = nltk.word_tokenize(line.strip())  # تقسيم السطر إلى كلمات

            program_tree = TreeNode("Parse Tree:")  # إنشاء الجذر لشجرة التحليل

            for tree in parser.parse(tokens):
                # تحويل شجرة NLTK إلى شجرة TreeNode
                def convert_nltk_tree_to_tree_node(nltk_tree, parent_node):
                    if isinstance(nltk_tree, nltk.Tree):
                        node = TreeNode(nltk_tree.label())
                        parent_node.add_child(node)
                        for child in nltk_tree:
                            convert_nltk_tree_to_tree_node(child, node)
                    else:
                        parent_node.add_child(TreeNode(str(nltk_tree)))

                convert_nltk_tree_to_tree_node(tree, program_tree)
                program_tree.print_tree()  # طباعة شجرة التحليل بتنسيق TreeNode
                
                # عرض الشجرة باستخدام NLTK
                tree.pretty_print()
                print("------------------------------------------------------------------------")

except FileNotFoundError:
    print(f"خطأ: الملف '{file_path}' غير موجود. الرجاء التحقق من المسار.")
except Exception as e:
    print(f"حدث خطأ غير متوقع: {e}")

# from graphviz import Digraph

# # إنشاء كائن للرسم البياني
# dot = Digraph(comment='Parse Tree')

# # تعريف الجذر والقواعد الرئيسية
# dot.node('S', 'S')
# dot.node('Statement', 'Statement')
# dot.node('Assignment', 'Assignment')
# dot.node('Conditional', 'Conditional')
# dot.node('PrintStatement', 'PrintStatement')
# dot.node('LoopStatement', 'LoopStatement')

# # بناء العلاقات بين الجذر والقواعد الرئيسية
# dot.edge('S', 'Statement')
# dot.edge('Statement', 'Assignment')
# dot.edge('Statement', 'Conditional')
# dot.edge('Statement', 'PrintStatement')
# dot.edge('Statement', 'LoopStatement')

# # إضافة العقد الفرعية Assignment
# dot.node('AssignmentType', 'Type')
# dot.node('Identifier', 'IDENTIFIER')
# dot.node('Expression', 'Expression')
# dot.node('AssignmentSymbol', "'='")
# dot.node('Semicolon', "';'")

# # بناء العلاقات داخل Assignment
# dot.edge('Assignment', 'AssignmentType')
# dot.edge('Assignment', 'Identifier')
# dot.edge('Assignment', 'AssignmentSymbol')
# dot.edge('Assignment', 'Expression')
# dot.edge('Assignment', 'Semicolon')

# # إضافة العقد الفرعية LoopStatement
# dot.node('LoopFor', "'for'")
# dot.node('LoopWhile', "'while'")
# dot.node('ForBody', 'Block')
# dot.node('WhileBody', 'Block')

# # بناء العلاقات داخل LoopStatement
# dot.edge('LoopStatement', 'LoopFor')
# dot.edge('LoopStatement', 'ForBody')
# dot.edge('LoopStatement', 'LoopWhile')
# dot.edge('LoopStatement', 'WhileBody')

# # إضافة العقد الفرعية Conditional
# dot.node('If', "'if'")
# dot.node('Condition', 'Condition')
# dot.node('ConditionBody', 'Block')

# # بناء العلاقات داخل Conditional
# dot.edge('Conditional', 'If')
# dot.edge('Conditional', 'Condition')
# dot.edge('Conditional', 'ConditionBody')

# # بناء القواعد داخل Condition
# dot.node('ConditionIdentifier', 'IDENTIFIER')
# dot.node('ConditionOperator', "'>' | '<' | '=='")
# dot.node('ConditionNumber', 'NUMBER')
# dot.edge('Condition', 'ConditionIdentifier')
# dot.edge('Condition', 'ConditionOperator')
# dot.edge('Condition', 'ConditionNumber')

# # إضافة العقد الفرعية PrintStatement
# dot.node('Print', "'print'")
# dot.node('PrintArgs', 'IDENTIFIER')
# dot.node('PrintSemicolon', "';'")

# # بناء العلاقات داخل PrintStatement
# dot.edge('PrintStatement', 'Print')
# dot.edge('PrintStatement', 'PrintArgs')
# dot.edge('PrintStatement', 'PrintSemicolon')

# # إضافة العقد الفرعية Type
# dot.node('TypeInt', "'int'")
# dot.node('TypeFloat', "'float'")
# dot.node('TypeString', "'string'")

# # بناء العلاقات داخل Type
# dot.edge('AssignmentType', 'TypeInt')
# dot.edge('AssignmentType', 'TypeFloat')
# dot.edge('AssignmentType', 'TypeString')

# # عرض الرسم البياني
# dot.render('parse_tree', format='png', view=True)