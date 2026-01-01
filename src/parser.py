from KavaAst import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0]

    def advance(self):
        self.pos += 1
        if self.pos > len(self.tokens) - 1:
            self.current_token = None
        else:
            self.current_token = self.tokens[self.pos]

    def parse(self):
        statements = []
        while self.current_token and self.current_token.type != 'EOF':
            stmt = self.statement()
            statements.append(stmt)
            if isinstance(stmt, (Assign, Print, Return, Call, VarDecl)):
                if self.current_token.type != 'SEMI':
                    raise KavaError('Expected ;', self.current_token.line)
                self.advance()
        return statements

    def statement(self):
        if self.current_token.type == 'IDENT':
            name = self.current_token.value
            self.advance()
            if self.current_token.type == 'ASSIGN':
                self.advance()
                expr = self.expr()
                return Assign(name, expr)
            elif self.current_token.type == 'LPAREN':
                self.advance()
                args = []
                if self.current_token.type != 'RPAREN':
                    args.append(self.expr())
                    while self.current_token.type == 'COMMA':
                        self.advance()
                        args.append(self.expr())
                if self.current_token.type != 'RPAREN':
                    raise KavaError('Expected )', self.current_token.line)
                self.advance()
                return Call(name, args)
            else:
                raise KavaError('Expected = or (', self.current_token.line)
        elif self.current_token.type == 'PRINT':
            self.advance()
            expr = self.expr()
            return Print(expr)
        elif self.current_token.type == 'VAR':
            self.advance()

            name = self.current_token.value
            self.advance()

            var_type = None
            if self.current_token.type == 'LBRACKET':
                self.advance()
                var_type = self.current_token.value
                self.advance()
                if self.current_token.type != 'RBRACKET':
                    raise KavaError('Expected ]', self.current_token.line)
                self.advance()

            if self.current_token.type != 'ASSIGN':
                raise KavaError('Expected =', self.current_token.line)
            self.advance()

            value = self.expr()
            return VarDecl(name, var_type, value)

        elif self.current_token.type == 'IF':
            self.advance()
            condition = self.expr()
            if self.current_token.type != 'LBRACE':
                raise KavaError('Expected {', self.current_token.line)
            self.advance()
            then_block = self.parse_block()
            else_block = None
            if self.current_token and self.current_token.type == 'ELSE':
                self.advance()
                if self.current_token.type != 'LBRACE':
                    raise KavaError('Expected {', self.current_token.line)
                self.advance()
                else_block = self.parse_block()
            return If(condition, then_block, else_block)
        elif self.current_token.type == 'WHILE':
            self.advance()
            condition = self.expr()
            if self.current_token.type != 'LBRACE':
                raise KavaError('Expected {', self.current_token.line)
            self.advance()
            body = self.parse_block()
            return While(condition, body)
        elif self.current_token.type == 'FUNC':
            self.advance()
            name = self.current_token.value
            self.advance()
            if self.current_token.type != 'LPAREN':
                raise KavaError('Expected (', self.current_token.line)
            self.advance()
            params = []
            if self.current_token.type != 'RPAREN':
                param_name = self.current_token.value
                self.advance()
                if self.current_token.type != 'COLON':
                    raise KavaError('Expected :', self.current_token.line)
                self.advance()
                param_type = self.current_token.value
                self.advance()
                params.append((param_name, param_type))
                while self.current_token.type == 'COMMA':
                    self.advance()
                    param_name = self.current_token.value
                    self.advance()
                    if self.current_token.type != 'COLON':
                        raise KavaError('Expected :', self.current_token.line)
                    self.advance()
                    param_type = self.current_token.value
                    self.advance()
                    params.append((param_name, param_type))
            if self.current_token.type != 'RPAREN':
                raise KavaError('Expected )', self.current_token.line)
            self.advance()
            if self.current_token.type != 'LBRACE':
                raise KavaError('Expected {', self.current_token.line)
            self.advance()
            body = self.parse_block()
            return Func(name, params, body)
        elif self.current_token.type == 'RETURN':
            self.advance()
            expr = self.expr()
            return Return(expr)
        else:
            raise KavaError('Invalid statement', self.current_token.line)

    def parse_block(self):
        statements = []
        while self.current_token and self.current_token.type != 'RBRACE':
            stmt = self.statement()
            statements.append(stmt)
            if isinstance(stmt, (Assign, Print, Return, Call, VarDecl)):
                if self.current_token.type != 'SEMI':
                    raise KavaError('Expected ;', self.current_token.line)
                self.advance()
        self.advance()  
        return statements

    def expr(self):
        result = self.or_expr()
        return result

    def or_expr(self):
        result = self.and_expr()
        while self.current_token and self.current_token.type == 'OR':
            op = self.current_token
            self.advance()
            right = self.and_expr()
            result = BinOp(result, op, right)
        return result

    def and_expr(self):
        result = self.comp_expr()
        while self.current_token and self.current_token.type == 'AND':
            op = self.current_token
            self.advance()
            right = self.comp_expr()
            result = BinOp(result, op, right)
        return result

    def comp_expr(self):
        result = self.add_expr()
        while self.current_token and self.current_token.type in ('EQ', 'NE', 'LT', 'GT'):
            op = self.current_token
            self.advance()
            right = self.add_expr()
            result = BinOp(result, op, right)
        return result

    def add_expr(self):
        result = self.term()
        while self.current_token and self.current_token.type in ('PLUS', 'MINUS'):
            op = self.current_token
            self.advance()
            right = self.term()
            result = BinOp(result, op, right)
        return result

    def term(self):
        result = self.factor()
        while self.current_token and self.current_token.type in ('MUL', 'DIV'):
            op = self.current_token
            self.advance()
            right = self.factor()
            result = BinOp(result, op, right)
        return result

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.advance()
            return Num(token.value)
        elif token.type == 'STRING':
            self.advance()
            return Str(token.value)
        elif token.type == 'IDENT':
            name = token.value
            self.advance()
            if self.current_token and self.current_token.type == 'LPAREN':
                self.advance()
                args = []
                if self.current_token.type != 'RPAREN':
                    args.append(self.expr())
                    while self.current_token.type == 'COMMA':
                        self.advance()
                        args.append(self.expr())
                if self.current_token.type != 'RPAREN':
                    raise KavaError('Expected )', self.current_token.line)
                self.advance()
                return Call(name, args)
            else:
                return Var(name)
        elif token.type == 'LPAREN':
            self.advance()
            result = self.expr()
            if self.current_token.type != 'RPAREN':
                raise KavaError('Expected )', self.current_token.line)
            self.advance()
            return result
        else:
            raise KavaError('Invalid factor', self.current_token.line)