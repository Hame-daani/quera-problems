from pyranj import PyRanj as pyranj


@pyranj
def f1():
    # goes into self.fn
    raise Exception("x1")


f1()
# [EXCEPTION] :: x1###############################

pyrannnnnnnj = pyranj()()(prefix="Hey")()


@pyrannnnnnnj(prefix="You")
def f2():
    # goes into fn
    raise Exception("x2")


f2()
# You :: x2#####################################

with pyranj(prefix="Yes")()()()()():
    raise Exception("x3")
# [EXCEPTION] :: x3 ####################################


class A(pyranj):
    def run(self, num):
        raise Exception("x" * num)


A().run(5)
# [EXCEPTION] :: xxxxx     ########################################


class B(pyranj()()(prefix="Hey there is an error")):
    def run(self):
        raise Exception("run ...")


B().run()
# Hey there is an error :: run ...
