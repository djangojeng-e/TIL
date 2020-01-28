def func():
    compute = 5 / 0
    return compute


try:
    func()
except ZeroDivisionError:
    print('It is a ZeroDivisionError')
except Exception:
    print('There is an error')
finally:
    print('The func() has been tried')
