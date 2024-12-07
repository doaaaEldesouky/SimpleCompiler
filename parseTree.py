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
from anytree import Node, RenderTree

# تعريف الجذر والشجرة باستخدام Nodes
S = Node("S")
statement = Node("Statement", parent=S)
assignment = Node("Assignment", parent=statement)
conditional = Node("Conditional", parent=statement)
print_statement = Node("PrintStatement", parent=statement)
loop_statement = Node("LoopStatement", parent=statement)

# بناء الشجرة مع العلاقات بين العقد
assignment_type = Node("Assignment Type", parent=assignment)
loop_for = Node("For Loop", parent=loop_statement)
loop_while = Node("While Loop", parent=loop_statement)
conditional_if = Node("If Statement", parent=conditional)

# إضافة القواعد الأخرى (مثل Type, Expression, وغيرها)
type_int = Node("'int'", parent=assignment_type)
type_float = Node("'float'", parent=assignment_type)
type_string = Node("'string'", parent=assignment_type)

identifier = Node("IDENTIFIER", parent=assignment_type)
expression = Node("Expression", parent=assignment_type)

# إضافة القواعد الخاصة بـ Expression
identifier_expression = Node("IDENTIFIER", parent=expression)
number_expression = Node("NUMBER", parent=expression)

# بناء الشجرة لقاعدة Conditional
condition = Node("Condition", parent=conditional_if)
identifier_condition = Node("IDENTIFIER", parent=condition)
operator = Node("'>'", parent=condition)
number = Node("NUMBER", parent=condition)

# إضافة القواعد الأخرى لـ Loop
loop_condition = Node("Condition", parent=loop_for)
loop_expression = Node("Expression", parent=loop_for)

# طباعة الشجرة بشكل هرمي مع إبراز العقد والأفرع لتوضيح شجرة التحليل
print("Parse Tree:")
for pre, fill, node in RenderTree(S):
    print(f"{pre}{node.name}")
