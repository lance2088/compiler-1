from Compiler.X86 import boolean_exprs as compile_x86
from Compiler.VM import boolean_exprs as compile_vm
from Interpreter import boolean_exprs as interpreter


class RelopBexp:
    """
    Relation operation boolean expression class for AST.
    eval - runtime function for Evaluator (return result of applying the boolean operation to left and right values).
    Example: x > 56
    """
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def eval(self, env):
        return interpreter.relop_bexp(env, self.op, self.left, self.right)

    def compile_vm(self, commands, data):
        return compile_vm.relop_bexp(commands, data, self.op, self.left, self.right)

    def compile_x86(self, compiler):
        return compile_x86.relop_bexp(compiler, self.op, self.left, self.right)


class AndBexp:
    """
    'And' operation boolean expression class for AST.
    eval - runtime function for Evaluator (return result of applying the 'and' operation to left and right values).
    Example: x > 56 and x < 61
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        return interpreter.and_bexp(env, self.left, self.right)

    def compile_vm(self, commands, data):
        return compile_vm.and_bexp(commands, data, self.left, self.right)

    def compile_x86(self, compiler):
        return compile_x86.and_bexp(compiler, self.left, self.right)


class OrBexp:
    """
    'Or' operation boolean expression class for AST.
    eval - runtime function for Evaluator (return result of applying the 'or' operation to left and right values).
    Example: x < 11 or x > 100
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, env):
        return interpreter.or_bexp(env, self.left, self.right)

    def compile_vm(self, commands, data):
        return compile_vm.or_bexp(commands, data, self.left, self.right)


class NotBexp:
    """
    'Not' operation boolean expression class for AST.
    eval - runtime function for Evaluator (return result of applying the 'not' operation to value).
    Example: x not 11
    """
    def __init__(self, exp):
        self.exp = exp

    def eval(self, env):
        return interpreter.not_bexp(env, self.exp)

    def compile_vm(self, commands, data):
        return compile_vm.not_bexp(commands, data, self.exp)
