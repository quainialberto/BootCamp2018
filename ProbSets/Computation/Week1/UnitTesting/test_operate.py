import pytest
import operate as op

def test_operate():
    with pytest.raises(TypeError) as excinfo:
        op.operate(4, 0, 0)
    assert excinfo.value.args[0] == "oper must be a string"
    assert op.operate(4, 1, '+') == 5, "failed +"
    assert op.operate(4, 1, '-') == 3, "failed -"
    assert op.operate(4, 1, '*') == 4, "failed *"
    assert op.operate(4, 2, '/') == 2, "failed /"
    with pytest.raises(ZeroDivisionError) as excinfo:
        op.operate(4, 0, '/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        op.operate(4, 0, '?')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
