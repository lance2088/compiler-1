from .Core.types import *
from .Utils.read import Read
from .Utils.write import Write


def read_statement(compiler):
    Read(compiler).call()
    return compiler.types.set(Types.INT)


def write_statement(compiler, aexp):
    value_type = aexp.compile_asm(compiler)
    compiler.types.pop()
    Write(compiler).call(value_type)
