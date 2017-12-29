from Compiler.X86 import arithmetic_exprs as compile_x86
from Compiler.VM import arithmetic_exprs as compile_vm
from Interpreter import arithmetic_exprs as interpreter


class IntAexp:
    """
    Integer arithmetic expression class for AST.
    eval - runtime function for Evaluator (just return i).
    Example: 54
    """
    def __init__(self, i):
        self.i = i

    def eval(self, env):
        return interpreter.int_aexp(env, self.i)

    def compile_vm(self, commands, data):
        return compile_vm.int_aexp(commands, data, self.i)

    def compile_x86(self, compiler):
        return compile_x86.int_aexp(compiler, self.i)


class VarAexp:
    """
    Variable arithmetic expression class for AST.
    eval - runtime function for Evaluator (return variable from environment by name).
    Example: x
    """
    def __init__(self, name):
        self.name = name
        self.context = 'get'
        self.type = None

    def eval(self, env):
        return interpreter.var_aexp(env, self.name)

    def compile_vm(self, commands, data):
        return compile_vm.var_aexp(commands, data, self.name, self.context, self.type)

    def compile_x86(self, compiler):
        return compile_x86.var_aexp(compiler, self.name, self.context, self.type)


class BinopAexp:
    """
    Binary operation arithmetic expression class for AST.
    eval - runtime function for Evaluator (return result of applying the aoperation to left and right values).
    Example: x + 54
    """
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def eval(self, env):
        return interpreter.binop_aexp(env, self.op, self.left, self.right)

    def compile_vm(self, commands, data):
        return compile_vm.binop_aexp(commands, data, self.op, self.left, self.right)

    def compile_x86(self, compiler):
        return compile_x86.binop_aexp(compiler, self.op, self.left, self.right)
