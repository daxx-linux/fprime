'''
Created on Jan 9, 2015
@author: reder
'''
# Exception classes for all controllers modules

class GseControllerException(Exception):
    def __init__(self,val):
        self.except_msg = val
        super(GseControllerException, self).__init__(val)
    def getMsg(self):
        return self.except_msg

class GseControllerUndefinedDirectoryException(GseControllerException):
    def __init__(self, val):
        super(GseControllerUndefinedDirectoryException,self).__init__("Path does not exist: %s!" % str(val))

class GseControllerUndefinedFileException(GseControllerException):
    def __init__(self, val):
        super(GseControllerUndefinedFileException,self).__init__("Path does not exist: %s!" % str(val))

class GseControllerParsingException(GseControllerException):
    def __init__(self, val):
        super(GseControllerParsingException,self).__init__("Parsing error: %s!" % str(val))

class GseControllerMnemonicMismatchException(GseControllerException):
    def __init__(self, val1, val2):
        super(GseControllerMnemonicMismatchException,self).__init__("ID mismatch (%s, %s)!" % (str(val1),str(val2)))

class GseControllerStatusUpdateException(GseControllerException):
    def __init__(self, val):
        super(GseControllerStatusUpdateException,self).__init__("Bad status update mode: %s!" % str(val))

