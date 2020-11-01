class BadBorrow(BaseException):
    def __init__(self, ctx):
        self.msg = ctx

    def __repr__(self):
        return f'Cannot borrow "{self.msg}".'

class BadReturn(BaseException):
    def __init__(self, ctx):
        self.msg = ctx

    def __repr__(self):
        return f'Cannot return "{self.msg}".'
