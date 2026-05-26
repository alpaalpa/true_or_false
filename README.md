# true_or_false
A simple python function to determine whether an input is True or False

Determine (educated guess) whether an input value is True
or False.  Input can be a bool, dict, int or str.  This is
useful for determining the value of a parameter as passed
in via environment variable, cli, config file or plain
python code.

Examples of True values:
  str: ['true', 't', '1', 'yes', 'y', 'oui']
  bool: True
  dict: {'a': 1} # any non empty dictionary
  list: [0]  # any non-empty list

Examples of False values:
  str: ['false', 'f', '0', 'no', 'n', 'non']
  bool: False
  dict: {}  # empty dictionary
  list: []  # empty list

## Installation

  pip install true-or-false

## Usage

```python
from true_or_false import true_or_false

b = true_or_false(1)
print(b)
>> True
```

### Optional parameters

```python
true_or_false(s, none_is_false=True, blank_is_false=True)
```

- `none_is_false` — when `True` (default), `None` returns `False`; when `False`, `None` returns `None`
- `blank_is_false` — when `True` (default), a blank string returns `False`; when `False`, a blank string returns `None`

Unrecognized input (a string not in the known lists, or an unsupported type) returns `None`.

## environ_true_or_false

A convenience wrapper that reads an environment variable and interprets its value.
Returns `None` if the variable is unset and no default is provided.

```python
from true_or_false import environ_true_or_false

# Returns True if MY_FLAG is set to 'true', '1', 'yes', etc.
# Returns None if MY_FLAG is not set.
result = environ_true_or_false('MY_FLAG')

# Provide a default in case the variable is not set.
result = environ_true_or_false('MY_FLAG', default='false')
```
