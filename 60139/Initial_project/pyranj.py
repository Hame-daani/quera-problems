from logger import logger


class PyRanj(object):
    def __init__(self, fn=None, prefix="[EXCEPTION]", child=None):
        # print(type(fn))
        self.fn = fn
        self.prefix = prefix
        if child:
            self.child = child["run"]
        else:
            self.child = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_value:
            logger.log(f"{self.prefix} :: {str(exc_value)}")
        return True

    def __call__(self, fn=None, prefix=None):
        # print(self.fn, self.prefix, fn, prefix)
        if prefix:
            self.prefix = prefix
        if fn:

            def wrapper(*args, **kwargs):
                # print("inside fn")
                try:
                    res = fn(*args, **kwargs)
                    self.prefix = "[EXCEPTION]"
                    # return res
                    return self
                except Exception as e:
                    logger.log(f"{self.prefix} :: {str(e)}")
                    self.prefix = "[EXCEPTION]"
                    return self

            return wrapper
        elif self.fn:
            try:
                # print(f"inside {self.fn}")
                res = self.fn()
                self.prefix = "[EXCEPTION]"
                # return res
                return self
            except Exception as e:
                logger.log(f"{self.prefix} :: {str(e)}")
                self.prefix = "[EXCEPTION]"
                return self
        if not (fn or prefix):
            self.prefix = "[EXCEPTION]"
        return self

    def __getattribute__(self, __name: str):
        if __name == "run":

            def wrapper(*arg, **kwargs):
                try:
                    print(f"inside run {self}")
                    # if self.child:
                    #     result = self.child(self, *arg, **kwargs)
                    # else:
                    #     result = object.__getattribute__(self, __name)(*arg, **kwargs)
                    # self.prefix = "[EXCEPTION]"
                    # return result
                except Exception as e:
                    logger.log(f"{self.prefix} :: {str(e)}")
                    self.prefix = "[EXCEPTION]"

            return wrapper
        else:
            # print(f"here for {__name} inside {self}")
            return object.__getattribute__(self, __name)
