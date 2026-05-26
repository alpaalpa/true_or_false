import pytest

from true_or_false import true_or_false, environ_true_or_false


@pytest.mark.parametrize("test_input,expected", [
    # Booleans
    (True, True),
    (False, False),
    # Integers
    (1, True),
    (0, False),
    # None
    (None, False),
    # Lists
    ([], False),
    ([0], True),
    ([0, 1], True),
    # Dicts
    ({}, False),
    ({'a': 1}, True),
    # English strings
    ('true', True),
    ('True', True),
    ('TRUE', True),
    ('t', True),
    ('T', True),
    ('1', True),
    ('yes', True),
    ('y', True),
    ('false', False),
    ('False', False),
    ('FALSE', False),
    ('f', False),
    ('F', False),
    ('0', False),
    ('no', False),
    ('n', False),
    # Multilingual
    ('oui', True),    # French
    ('non', False),   # French
    ('ja', True),     # German/Dutch/Afrikaans
    ('nein', False),  # German
    ('si', True),     # Spanish/Italian
    ('da', True),     # Russian/Bulgarian/Serbian
    ('net', False),   # Russian
    ('ano', True),    # Czech/Slovak
    ('ne', False),    # Czech/Ukrainian
    ('nee', False),   # Dutch
    ('nej', False),   # Swedish/Danish/Norwegian
    ('jah', True),    # Afrikaans
    ('haan', True),   # Hindi
    ('nahin', False), # Hindi
    # Blank string
    ('', False),
])
def test_various(test_input, expected):
    assert true_or_false(test_input) == expected


def test_none_is_false_false():
    assert true_or_false(None, none_is_false=False) is None


def test_blank_is_false_false():
    assert true_or_false('', blank_is_false=False) is None


def test_unrecognized_string_returns_none():
    assert true_or_false('maybe') is None


def test_environ_true_or_false_set_true(monkeypatch):
    monkeypatch.setenv('TEST_VAR', 'true')
    assert environ_true_or_false('TEST_VAR') is True


def test_environ_true_or_false_set_false(monkeypatch):
    monkeypatch.setenv('TEST_VAR', '0')
    assert environ_true_or_false('TEST_VAR') is False


def test_environ_true_or_false_unset_returns_none():
    assert environ_true_or_false('_NONEXISTENT_VAR_TRUE_OR_FALSE') is None


def test_environ_true_or_false_default(monkeypatch):
    monkeypatch.delenv('TEST_VAR', raising=False)
    assert environ_true_or_false('TEST_VAR', default='yes') is True
