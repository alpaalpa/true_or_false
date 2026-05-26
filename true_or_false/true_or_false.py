from logging import getLogger
from typing import Any
import os

logger = getLogger(__name__)


def true_or_false(s: Any, none_is_false: bool = True, blank_is_false: bool = True) -> bool | None:
    ''' Determine (educated guess) whether an input value is True
    or False.  Input can be a bool, dict, int or str.  This is
    useful for determining the value of a parameter as passed
    in via environment variable, cli, config file or plain
    python code.

    Examples of True values:
        str: ['true', 't', '1', 'yes', 'y', 'oui', '是', 'はい', '예']
        bool: True
        dict: {'a': 1} # any non empty dictionary
        list: [0]  # any non-empty list
    Examples of False values:
        str: ['false', 'f', '0', 'no', 'n', 'non', '不', 'いいえ', '아니요']
        bool: False
        dict: {}  # empty dictionary
        list: []  # empty list

    Parameters
    ----------
    none_is_false: bool
        if none_is_false is True, treat None as False
        if none_is_false is False, return None if `s` is None
    blank_is_false: bool
        if blank_is_false is True, treat empty string as False
        if blank_is_false is False, return None if 's' is ''

    '''
    TRUES = [
        # English
        'true', 't', '1', 'yes', 'y',
        # European languages
        'oui', 'ja', 'si', 'da', 'ano', 'jah', 'haan',
        # Chinese (Simplified & Traditional)
        '是', '对', '對', '正确', '正確', '真',
        # Japanese
        'はい',
        # Korean
        '예', '네',
    ]
    FALSES = [
        # English
        'false', 'f', '0', 'no', 'n',
        # European languages
        'non', 'nein', 'net', 'ne', 'nee', 'nej', 'nahin',
        # Chinese (Simplified & Traditional)
        '不', '否', '不对', '不對', '不是', '假',
        # Japanese
        'いいえ',
        # Korean
        '아니요', '아니',
    ]

    if s is None:
        if none_is_false:
            return False
        else:
            return None
    if isinstance(s, bool):
        return s
    if isinstance(s, int):
        if s == 0:
            return False
        else:
            return True
    if isinstance(s, list):
        return len(s) != 0
    if isinstance(s, dict):
        return bool(s)
    if isinstance(s, str):
        if s.strip() == '':
            if blank_is_false:
                return False
            else:
                return None
        if s.strip().lower() in TRUES:
            return True
        elif s.strip().lower() in FALSES:
            return False
        else:
            logger.warning(f"Cannot determine True/False from {s}")
            return None
    else:
        logger.warning(f"Cannot determine True/False from {s}")
        return None


def environ_true_or_false(env_var: str, default: Any = None) -> bool | None:
    ''' Check whether `env_var` contains a 'true' like value such as
           1, true, y, yes, t, oui
        Use default value if the environment variable does not exist.

        Parameters
        ----------
        env_var: str
            A valid environment variable string
        default:
            The default value if `env_var` is not set

        Returns
        -------
        bool or None

    '''
    return true_or_false(os.environ.get(env_var, default), none_is_false=False)
