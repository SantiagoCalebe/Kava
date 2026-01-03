import sys
import os
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from KavaAst import KavaError
from version import KavaVersion

def enable_colors():
    if os.name != 'nt':
        return

    if os.getenv("ANSICON") or os.getenv("WT_SESSION") or os.getenv("TERM") == "xterm-256color":
        return

    try:
        import colorama
        colorama.init(autoreset=True)
    except ImportError:
        pass

enable_colors()

def main():
    if len(sys.argv) != 2:
        print(f"\n\033[91m[KAVA v. {KavaVersion}] - ERROR: Usage: python interp.py <file.kava>\033[0m")
        print("\n[KAVA] Operation ended with with exit code 1.")
        input("Press [ ENTER ] to close...")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith('.kava'):
        print(f"\n\033[91m[KAVA v. {KavaVersion}] - ERROR: File must have a .kava extension\033[0m")
        print("\n[KAVA] Operation ended with with exit code 1.")
        input("Press [ ENTER ] to close...")
        sys.exit(1)

    try:
        with open(filename, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"\n\033[91m[KAVA v. {KavaVersion}] - ERROR: File {filename} not found.\033[0m")
        print("\n[KAVA] Operation ended with with exit code 1.")
        input("Press [ ENTER ] to close...")
        sys.exit(1)

    try:
        lexer = Lexer(text)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        interpreter = Interpreter()
        interpreter.interpret(statements)

        if 'main' in interpreter.functions:
            from ast import Call
            main_call = Call('main', [])
            interpreter.visit(main_call)

        interpreter.interpret([])

        print("\033[92m\n[KAVA] Operation ended with exit code 0.\033[0m")

        if hasUpdate():
            print(f"\n\033[91m[KAVA v. {KavaVersion}] - Your Kava version is outdated! Update now!\033[0m")
            print(f"\033[91mhttps://github.com/santiagocalebe/Kava/releases/latest\033[0m")

        input("\033[92mPress [ ENTER ] to close...\033[0m")

    except KavaError as e:
        print(f"\n\033[91m[KAVA v. {KavaVersion}] - ERROR: ({filename}) [{e.line or 'N/A'}]: {e.message}\033[0m")
        print("\n[KAVA] Operation ended with with exit code 1.")
        input("Press [ ENTER ] to close...")
        sys.exit(1)

    except Exception as e:
        print(f"\n\033[91m[KAVA v. {KavaVersion}] - ERROR: ({filename}) [N/A]: Unexpected error: {e}\033[0m")
        print("\n[KAVA] Operation ended with with exit code 1.")
        input("Press [ ENTER ] to close...")
        sys.exit(1)

if __name__ == '__main__':
    main()
