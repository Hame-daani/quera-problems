class ExceptionProxy(Exception):
    def __init__(self, e, f):
        self.msg = e
        self.function = f


def transform_exceptions(func_ls):
    tr_ls = []
    for func in func_ls:
        try:
            func()
            tr = ExceptionProxy("ok!", func)
        except Exception as e:
            tr = ExceptionProxy(str(e), func)
        tr_ls.append(tr)
    return tr_ls
