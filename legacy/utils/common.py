import re
import sys
import collections

def print_err(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def sanitize_name(name, verbose=True):
    """
        Transform name to lowercase, replace ' ' and '_' to '-'
        :param name
        :param verbose
    """
    sanitized_name = name
    sanitized_name = sanitized_name.lower()
    sanitized_name = sanitized_name.replace(' ', '-')
    sanitized_name = sanitized_name.replace('_', '-')
    sanitized_name = sanitized_name.replace('.', '-')
    if sanitized_name != name and verbose:
        print('[Warning] Name {} is replaced by {}.'.format(name, sanitized_name))
    check_valid_dns(sanitized_name)
    return sanitized_name

_DNS_RE = re.compile('^[a-z0-9]([-a-z0-9]*[a-z0-9])?$')

def check_valid_dns(name):
    """
    experiment name is used as namespace, which must conform to DNS format
    """
    if not _DNS_RE.match(name):
        raise ValueError(name + ' must be a valid DNS name with only lower-case '
            'letters, 0-9 and hyphen. No underscore or dot allowed.')

def is_sequence(obj):
    """
    Returns:
      True if the sequence is a collections.Sequence and not a string.
    """
    return (isinstance(obj, collections.Sequence)
            and not isinstance(obj, str))


class CompilationError(Exception):
    pass

