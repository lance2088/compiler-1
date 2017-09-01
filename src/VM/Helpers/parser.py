from src.VM.commands import *
from pprint import pprint

COMMAND_SEPARATOR = '\n'
ARGS_SEPARATOR = ' '

command_class_relation_map = {
    'PUSH': Push,
    'POP': Pop,
    'NOP': Nop,
    'DUP': Dup,
    'LOAD': Load,
    'BLOAD': BLoad,
    'DLOAD': DLoad,
    'DBLOAD': DBLoad,
    'STORE': Store,
    'BSTORE': BStore,
    'DSTORE': DStore,
    'DBSTORE': DBStore,
    'ADD': Add,
    'MUL': Mul,
    'SUB': Sub,
    'DIV': Div,
    'MOD': Mod,
    'INVERT': Invert,
    'COMPARE': Compare,
    'LABEL': Label,
    'JUMP': Jump,
    'JZ': Jz,
    'JNZ': Jnz,
    'READ': Read,
    'WRITE': Write,
    'ENTER': Enter,
    'CALL': Call,
    'RETURN': Return,
    'ALLOCATE': Allocate,
    'DALLOCATE': DAllocate,
    'LOG': Log
}

def parse(program):
    commands = program.split(COMMAND_SEPARATOR)
    command_classes = []
    for command in commands:
        command = command.split(ARGS_SEPARATOR)
        args = []
        for arg in command[1:]:
            args.append(int(arg))
        command_classes.append(command_class_relation_map[command[0]](*args))

    return command_classes
