import operator


# Define a Node class to represent each element in the AST
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Could be an operator, attribute, or value
        self.left = left  # Left child node
        self.right = right  # Right child node


# Define supported operations
operations = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "=": operator.eq,
    "!=": operator.ne,
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
}


def create_rule(rule_string):
    """
    Parses a rule string and converts it into an AST.
    """
    tokens = rule_string.replace("(", " ( ").replace(")", " ) ").split()
    stack = []
    current_node = None

    for token in tokens:
        if token == '(':
            # Start a new subexpression
            stack.append(current_node)
            current_node = None
        elif token == ')':
            # Close the current expression and go back to the previous node
            if stack:
                parent = stack.pop()
                if parent:
                    if not parent.left:
                        parent.left = current_node
                    else:
                        parent.right = current_node
                    current_node = parent
        elif token in operations:
            # Handle operators
            new_node = Node(token)
            if current_node:
                new_node.left = current_node
            current_node = new_node
        else:
            # Handle values and attributes
            token = token.strip("'")  # Strip any surrounding single quotes from strings
            if current_node and not current_node.left:
                current_node.left = Node(token)
            elif current_node and current_node.right is None:
                current_node.right = Node(token)
            else:
                current_node = Node(token)

    return current_node


def combine_rules(rules):
    """
    Combines multiple rules (ASTs) into a single AST using AND operator by default.
    """
    if not rules:
        return None

    combined_node = rules[0]
    for rule in rules[1:]:
        combined_node = Node("AND", combined_node, rule)

    return combined_node


def evaluate_node(node, data):
    """
    Recursively evaluates a node against the data dictionary.
    """
    if node.value in operations:
        # Evaluate logical or comparison operator
        left_val = evaluate_node(node.left, data)
        right_val = evaluate_node(node.right, data)
        return operations[node.value](left_val, right_val)
    elif node.left is None and node.right is None:
        # It's a leaf node - return the value
        # If it's a numeric value, cast it
        if node.value.isdigit():
            return int(node.value)
        # Otherwise, assume it's an attribute in data
        return data.get(node.value, node.value)
    else:
        raise ValueError("Unexpected node structure")


def evaluate_rule(ast, data):
    """
    Evaluates the entire AST against the provided data.
    """
    return evaluate_node(ast, data)


# Example usage
rule1 = create_rule("department = 'Marketing'")
rule2 = create_rule("salary > 20000")
rule3 = create_rule("experience > 5")

# Combine rules
combined_rule = combine_rules([rule1, rule2, rule3])

# Sample data
data1 = {"department": "Marketing", "salary": 25000, "experience": 6}
data2 = {"department": "Sales", "salary": 80000, "experience": 3}

# Evaluate
print(evaluate_rule(combined_rule, data1))  # Expected output: True
print(evaluate_rule(combined_rule, data2))  # Expected output: False
