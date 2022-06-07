class Proxy(object):
    def __init__(self, obj):
        object.__setattr__(self, "_obj", obj)
        object.__setattr__(self, "call_stack", [])

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except:
            try:
                attr = getattr(self._obj, name)
                self.call_stack.append(name)
                return attr
            except:
                raise Exception("No Such Method")

    def __delattr__(self, name):
        delattr(object.__getattribute__(self, "_obj"), name)

    def __setattr__(self, name, value):
        setattr(object.__getattribute__(self, "_obj"), name, value)

    def last_invoked_method(self):
        try:
            return self.call_stack[-1]
        except:
            raise Exception("No Method Is Invoked")

    def count_of_calls(self, method_name):
        return self.call_stack.count(method_name)

    def was_called(self, method_name):
        return method_name in self.call_stack


class Radio:
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on
