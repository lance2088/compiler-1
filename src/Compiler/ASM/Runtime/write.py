from ..Core.registers import Registers
from ..Core.commands import Commands
from ..Core.types import Types

from .base import Base
from .itoa_and_write import ItoaWrite


class Write(Base):
    is_loaded = False

    def __init__(self, compiler):
        Base.__init__(self, compiler)

        if Write.is_loaded:
            return

        self.load('write.asm', 'write')
        Write.is_loaded = True

    def call(self, value_type):
        if value_type == Types.INT or True:
            ItoaWrite(self.compiler)
            self.compiler.code.add(Commands.POP, Registers.EAX)
            self.compiler.code.add(Commands.CALL, ['itoa_and_write'])
            self.compiler.code.add(Commands.MOV, [Registers.EAX, 10])
            self.compiler.code.add(Commands.CALL, ['write'])
        else:
            pass
