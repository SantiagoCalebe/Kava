import re

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

    def __repr__(self):
        return f'Token({self.type}, {self.value}, {self.line})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.current_char = self.text[0] if self.text else None

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def read_number(self):
        result = ''
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        if '.' in result:
            return float(result)
        else:
            return int(result)

    def read_string(self):
        self.advance()  # skip opening quote
        result = ''
        while self.current_char and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # skip closing quote
        return result

    def read_identifier(self):
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char == '#':
                while self.current_char and self.current_char != '\n':
                    self.advance()
                continue
            if self.current_char.isdigit():
                tokens.append(Token('NUMBER', self.read_number(), self.line))
                continue
            if self.current_char == '"':
                tokens.append(Token('STRING', self.read_string(), self.line))
                continue
            if self.current_char.isalnum() or self.current_char == '_':
                ident = self.read_identifier()
                if ident in ['print', 'if', 'else', 'while', 'func', 'return', 'var', 'int', 'float', 'string', 'array']:
                    tokens.append(Token(ident.upper(), ident, self.line))
                else:
                    tokens.append(Token('IDENT', ident, self.line))
                continue
            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    tokens.append(Token('EQ', '==', self.line))
                else:
                    tokens.append(Token('ASSIGN', '=', self.line))
                continue
            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    tokens.append(Token('NE', '!=', self.line))
                else:
                    raise ValueError('Invalid character: !')
                continue
            if self.current_char == '<':
                self.advance()
                tokens.append(Token('LT', '<', self.line))
                continue
            if self.current_char == '>':
                self.advance()
                tokens.append(Token('GT', '>', self.line))
                continue
            if self.current_char == '+':
                self.advance()
                tokens.append(Token('PLUS', '+', self.line))
                continue
            if self.current_char == '-':
                self.advance()
                tokens.append(Token('MINUS', '-', self.line))
                continue
            if self.current_char == '*':
                self.advance()
                tokens.append(Token('MUL', '*', self.line))
                continue
            if self.current_char == '/':
                self.advance()
                tokens.append(Token('DIV', '/', self.line))
                continue
            if self.current_char == '(':
                self.advance()
                tokens.append(Token('LPAREN', '(', self.line))
                continue
            if self.current_char == ')':
                self.advance()
                tokens.append(Token('RPAREN', ')', self.line))
                continue
            if self.current_char == '{':
                self.advance()
                tokens.append(Token('LBRACE', '{', self.line))
                continue
            if self.current_char == '}':
                self.advance()
                tokens.append(Token('RBRACE', '}', self.line))
                continue
            if self.current_char == ';':
                self.advance()
                tokens.append(Token('SEMI', ';', self.line))
                continue
            if self.current_char == ',':
                self.advance()
                tokens.append(Token('COMMA', ',', self.line))
                continue
            if self.current_char == ':':
                self.advance()
                tokens.append(Token('COLON', ':', self.line))
                continue
            if self.current_char == '[':
                self.advance()
                tokens.append(Token('LBRACKET', '[', self.line))
                continue
            if self.current_char == ']':
                self.advance()
                tokens.append(Token('RBRACKET', ']', self.line))
                continue
            if self.current_char == '|':
                self.advance()
                if self.current_char == '|':
                    self.advance()
                    tokens.append(Token('OR', '||', self.line))
                else:
                    raise ValueError('Invalid character: |')
                continue
            if self.current_char == '&':
                self.advance()
                if self.current_char == '&':
                    self.advance()
                    tokens.append(Token('AND', '&&', self.line))
                else:
                    raise ValueError('Invalid character: &')
                continue
            raise ValueError(f'Invalid character: {self.current_char}')
        tokens.append(Token('EOF', None, self.line))
        return tokens