def wrap():
    def decorate(func):
        def call(*args, **kwargs):
            
            # WRITE YOUR CODE HERE
            result = func(*args, **kwargs)
            return result

        return call

    return decorate
