from src.Parser.Language.AST.boolean_exprs import *
from src.Parser.Language.Parsers.arithmetic_exprs import aexp, any_operator_in_list, process_group

from src.Parser.Language.Parsers.basic import *

"""
Convert boolean expression value to object of AST-class 'RelopBexp'.
"""
def process_relop(parsed):
    ((left, op), right) = parsed
    return RelopBexp(op, left, right)

"""
Parsing boolean expression (arithmetic expression + compare operator + arithmetic expression).
"""
def bexp_relop():
    relops = ['<', '<=', '>', '>=', '=', '!=']
    return aexp() + any_operator_in_list(relops) + aexp() ^ process_relop

"""
Parsing 'not' expression (convert expression to object of AST-class 'NotBexp').
"""
def bexp_not():
    return keyword('not') + Lazy(bexp_term) ^ (lambda parsed: NotBexp(parsed[1]))

"""
Parse the binary expression in parentheses.
"""
def bexp_group():
    return keyword('(') + Lazy(bexp) + keyword(')') ^ process_group

"""
Parse the binary expression.
Try to first parse as 'not' expression,
if not possible - as just binary expressions,
if not possible - as a parentheses group of binary expressions.
"""
def bexp_term():
    return bexp_not() | bexp_relop() | bexp_group()