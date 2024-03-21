import pytest
from balance import balance

@pytest.mark.parametrize(
    'start_list,expected',
    (
            ['(((([{}]))))', 'Сбалансированно'],
            ['[([])((([[[]]])))]{()}', 'Сбалансированно'],
            ['{{[()]}}', 'Сбалансированно'],
            ['}{}', 'Несбалансированно'],
            ['{{[(])]}}', 'Несбалансированно'],
            ['[[{())}]', 'Несбалансированно'],
    )
)
def test_balance(start_list, expected):
    result = balance(start_list)
    assert result == expected
