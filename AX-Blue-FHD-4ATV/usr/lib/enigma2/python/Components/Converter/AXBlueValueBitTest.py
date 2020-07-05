from Converter import Converter
from Components.Element import cached

class AXBlueValueBitTest(Converter, object):

    def __init__(self, arg):
        Converter.__init__(self, arg)
        self.value = int(arg)

    @cached
    def getBoolean(self):
        return self.source.value & self.value and True or False

    boolean = property(getBoolean)
