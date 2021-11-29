# unit test for util/true_or_false.py
import pytest

from true_or_false import true_or_false


@pytest.mark.parametrize("test_input,expected",
                         [
                            ('True', True),
                            ('true', True),
                            ('1', True),
                            ('t', True),
                            ('T', True),
                            ('y', True),
                            ('yes', True),
                            ('oui', True),
                            ('TRUE', True),
                            ('false', False),
                            ('0', False),
                            ('f', False),
                            ('F', False),
                            ('n', False),
                            ('non', False),
                            ('FALSE', False),
                            (True, True),
                            (False, False),
                            (None, False),
                            ([], False),
                            ([0], True),
                            ({}, False),
                            ({'a': 1}, True)
                         ])
def test_various(test_input, expected):
    assert eval('true_or_false(test_input)') == expected


def test_list():
    assert true_or_false([0, 1]) is True
