def outer(arg):
    print('inside outer')
    def inner():
        print('inner is executed')
        arg()
    return inner
@outer
def fun():
    print('fubn is executed')
fun()
