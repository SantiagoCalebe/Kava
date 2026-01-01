class ASTNode:
    pass

class KavaError(Exception):
    def __init__(self, message, line=None):
        self.message = message
        self.line = line
        super().__init__(f"{message}" + (f" at line {line}" if line else ""))

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Str(ASTNode):
    def __init__(self, value):
        self.value = value

class Var(ASTNode):
    def __init__(self, name):
        self.name = name

class Assign(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class If(ASTNode):
    def __init__(self, condition, then_block, else_block):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

class While(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class Func(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class VarDecl:
    def __init__(self, name, var_type, value):
        self.name = name
        self.var_type = var_type
        self.value = value

class Return(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class Call(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args