from KavaAst import *
from version import KavaVersion

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.warnings = []
        self.used_vars = set()

    def is_truthy(self, value):
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return value != 0
        if isinstance(value, str):
            return len(value) > 0
        return False

    def visit(self, node):
        if isinstance(node, Num):
            return node.value
        elif isinstance(node, Str):
            return node.value
        elif isinstance(node, Var):
            if node.name in self.variables:
                self.used_vars.add(node.name)
                return self.variables[node.name]
            else:
                raise KavaError(f'Undefined variable: {node.name}')
        elif isinstance(node, BinOp):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op.type == 'PLUS':
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                else:
                    return left + right
            elif node.op.type == 'MINUS':
                return left - right
            elif node.op.type == 'MUL':
                return left * right
            elif node.op.type == 'DIV':
                return left / right
            elif node.op.type == 'EQ':
                return left == right
            elif node.op.type == 'NE':
                return left != right
            elif node.op.type == 'LT':
                return left < right
            elif node.op.type == 'GT':
                return left > right
            elif node.op.type == 'OR':
                return self.is_truthy(left) or self.is_truthy(right)
            elif node.op.type == 'AND':
                return self.is_truthy(left) and self.is_truthy(right)
        elif isinstance(node, Assign):
            value = self.visit(node.expr)
            self.variables[node.name] = value
        elif isinstance(node, Print):
            value = self.visit(node.expr)
            print(value)
        elif isinstance(node, If):
            if self.is_truthy(self.visit(node.condition)):
                self.interpret(node.then_block)
            elif node.else_block:
                self.interpret(node.else_block)
        elif isinstance(node, While):
            while self.is_truthy(self.visit(node.condition)):
                self.interpret(node.body)
        elif isinstance(node, Func):
            self.functions[node.name] = node
        elif isinstance(node, VarDecl):
            value = self.visit(node.value)
            self.variables[node.name] = value
        elif isinstance(node, Return):
            raise ReturnException(self.visit(node.expr))
        elif isinstance(node, Call):
            func = self.functions.get(node.name)
            if not func:
                raise KavaError(f'Undefined function: {node.name}')
            if len(node.args) != len(func.params):
                raise KavaError(f'Wrong number of arguments for {node.name}')
            old_vars = {}
            for (param_name, param_type), arg in zip(func.params, node.args):
                if param_name in self.variables:
                    old_vars[param_name] = self.variables[param_name]
                self.variables[param_name] = self.visit(arg)
            result = None
            try:
                self.interpret(func.body)
            except ReturnException as e:
                result = e.value
            for param_name, _ in func.params:
                if param_name in old_vars:
                    self.variables[param_name] = old_vars[param_name]
                else:
                    del self.variables[param_name]
            return result

    def interpret(self, statements):
        for stmt in statements:
            self.visit(stmt)
        if not hasattr(self, 'top_level_done'):
            self.top_level_done = True

            for var in self.variables:
                if var not in self.used_vars:
                    self.warnings.append(f"Variable '{var}' is declared but not used")
            if self.warnings:
                YELLOW = "\033[33m"
                RESET = "\033[0m"
                print()
                for warning in self.warnings:
                    print(f"{YELLOW}[KAVA v. {KavaVersion}] - WARNING: {warning}{RESET}")