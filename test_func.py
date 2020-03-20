def add(a, b):
    c = a + b
    return c

def test1():
    assert 1 == add(1, 0)

def test2():
    assert 1 != add(1, 1)