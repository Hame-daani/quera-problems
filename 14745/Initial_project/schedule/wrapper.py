from datetime import datetime, timedelta


def wrap():
    def decorate(func):
        def call(*args, **kwargs):
            # WRITE YOUR CODE HERE
            result = func(*args, **kwargs)
            name = func.__name__
            if name == "to":
                a = result.interval
                b = result.latest
                result.interval = b
                result.latest = a + b
            if name == "__repr__":
                result = result.replace("Every", "Har")
            if name == "should_run":
                now = datetime.now()
                target = datetime(2010, 1, 6, 13, 16)
                diff = timedelta(seconds=59)
                # TODO: now working!
                if now - target <= diff:
                    return False
            return result

        return call

    return decorate
