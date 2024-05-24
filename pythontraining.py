#error and exception
class valueTooHigherrer():
    pass





def test_value(x):
    if x>100:
        raise valueTooHigherrer('value is too high')
try:
    test_value(200)
except valueTooHigherrer as e:
    print(e)