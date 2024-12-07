from prettytable import PrettyTable

# دالة لحساب First
def calculate_first(grammar, symbol, memo):
    if symbol in memo:
        return memo[symbol]

    first_set = set()
    for lhs, rhs in grammar:
        if lhs == symbol:
            if rhs == 'epsilon':
                first_set.add('epsilon')
            elif not rhs[0].isupper():
                first_set.add(rhs[0])
            else:
                for s in rhs:
                    sub_first = calculate_first(grammar, s, memo)
                    first_set |= sub_first - {'epsilon'}
                    if 'epsilon' not in sub_first:
                        break
                else:
                    first_set.add('epsilon')
    memo[symbol] = first_set
    return first_set

# دالة لحساب Follow
def calculate_follow(grammar, start_symbol, symbol, first_sets, memo):
    if symbol in memo:
        return memo[symbol]

    follow_set = set()
    if symbol == start_symbol:
        follow_set.add('$')

    for lhs, rhs in grammar:
        for i, sym in enumerate(rhs):
            if sym == symbol:
                # إذا كان في النهاية، أضف Follow اليسار
                if i + 1 == len(rhs):
                    if lhs != symbol:  # تجنب التكرار الذاتي
                        follow_set |= calculate_follow(grammar, start_symbol, lhs, first_sets, memo)
                else:
                    next_symbol = rhs[i + 1]
                    if next_symbol in first_sets:  # تحقق أن next_symbol ليس رمزا طرفيا
                        next_first = first_sets[next_symbol]
                        follow_set |= next_first - {'epsilon'}
                        if 'epsilon' in next_first:
                            follow_set |= calculate_follow(grammar, start_symbol, lhs, first_sets, memo)
                    else:  # إذا كان next_symbol طرفيا، أضفه مباشرة إلى Follow
                        follow_set.add(next_symbol)
    memo[symbol] = follow_set
    return follow_set

# القواعد النحوية
grammar = [
    ('E', 'TA'),
    ('A', '+TA'),
    ('A', 'epsilon'),
    ('T', 'FB'),
    ('B', '*FB'),
    ('B', 'epsilon'),
    ('F', '(E)'),
    ('F', 'd'),
]

# تحديد Non-terminals و Terminals
non_terminals = {lhs for lhs, _ in grammar}
terminals = set(c for _, rhs in grammar for c in rhs if not c.isupper() and c != 'epsilon') | {'$', 'epsilon'}

# حساب First و Follow
first_sets = {}
follow_sets = {}
for nt in non_terminals:
    first_sets[nt] = calculate_first(grammar, nt, first_sets)

for nt in non_terminals:
    follow_sets[nt] = calculate_follow(grammar, 'E', nt, first_sets, follow_sets)

# إنشاء الجدول لعرض النتائج باستخدام PrettyTable
def print_table(title, headers, data):
    table = PrettyTable()
    table.field_names = headers
    for row in data:
        table.add_row(row)
    print(f"{title}:\n{table}\n")

# جدول القواعد النحوية
print_table("Grammar Rules", ["Non-terminal", "Production"], grammar)

# جدول First Sets
print_table("First Sets", ["Non-terminal", "First Set"], [(nt, first_sets[nt]) for nt in non_terminals])

# جدول Follow Sets
print_table("Follow Sets", ["Non-terminal", "Follow Set"], [(nt, follow_sets[nt]) for nt in non_terminals])

# إنشاء جدول التحليل (Parse Table)
parse_table = PrettyTable()
parse_table.field_names = ["NT / T", "$", "(", ")", "*", "+"]
parse_table.add_row(["A", "A => epsilon", "", "A => epsilon", "", "A => ['+TA']"])
parse_table.add_row(["B", "B => epsilon", "", "B => epsilon", "B => ['*FB']", "B => epsilon"])
parse_table.add_row(["E", "", "E => ['TA']", "", "", ""])
parse_table.add_row(["F", "", "F => ['(E)', 'd']", "", "", ""])
parse_table.add_row(["T", "", "T => ['FB']", "", "", ""])

# عرض جدول التحليل (Parse Table)
print(f"Parse Table:\n{parse_table.get_string()}")
