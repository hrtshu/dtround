
from datetime import datetime, date, timedelta

from math import floor as _floor, ceil as _ceil
_round = round

from sys import version_info

if version_info[0] == 3 and version_info[1] >= 2:
    _td_div = lambda a, b: a / b
    _td_mul = lambda d, i: d * i
elif version_info[0] == 2 and version_info[1] >= 7:
    _td_div = lambda a, b: a.total_seconds() / b.total_seconds()
    def _td_mul(d, i):
        def _sec_to_delta(sec):
            s = int(sec)
            return timedelta(seconds=sec, microseconds=int((sec - s) * 1000000))
        return _sec_to_delta(d.total_seconds() * i)
else:
    raise ImportError('This Python version is not supported. '
                      'Supported versions are 2.7+ and 3.2+')

def _base_func(dt, unit, base, round):
    if type(dt) not in (datetime, date):
        raise TypeError('`dt` must be type of `datetime.datetime` '
                        'or `datetime.date`')
    if type(unit) != timedelta:
        raise TypeError('`unit` must be type of `datetime.timedelta`')
    if base is None:
        base = dt.__class__(1970, 1, 1)
        if type(dt) == datetime:
            base = base.replace(tzinfo=dt.tzinfo)
    elif type(dt) != type(base):
        raise TypeError('`dt` and `base` must be same types')
    return base + _td_mul(unit, int(round(_td_div((dt - base), unit))))

def floor(dt, unit=timedelta(days=1), base=None):
    """
    Round down datetime/date object

    Parameters
    ----------
    dt : datetime.datetime or datetime.date
        datetime/date object to be rounded down
    unit : datetime.timedelta, optional
        rounding-down unit. Default is `datetime.timedelta(days=1)`.
    base : datetime.datetime or datetime.date, optional
        base datetime/date object. Default is `None`. If `None`, 
        `datetime.datetime(1970, 1, 1, tzinfo=dt.tzinfo)`/`datetime.date(1970,
        1, 1)` is used for this. This type must be the same as the type of
        `dt`.

    Returns
    -------
    output : datetime.datetime or datetime.date
        a value rounded down to the nearest `unit`.
        equal to `base + math.floor((dt - base) / unit) * unit`

    See Also
    --------
    ceil : Round up datetime/date object
    round : Round off datetime/date object

    Examples
    --------
    >>> dt = datetime.datetime(2048, 4, 16, 8, 32, 2, 65536)
    >>> unit = datetime.timedelta(minutes=15)
    >>> dtround.floor(dt, unit)
    datetime.datetime(2048, 4, 16, 8, 30)

    Using `base` parameter:

    >>> dt = datetime.datetime(2048, 4, 22, 16, 32)
    >>> unit = datetime.timedelta(weeks=1)
    >>> base = datetime.datetime(2048, 4, 10)
    >>> dtround.floor(dt, unit, base)
    datetime.datetime(2048, 4, 17, 0, 0)

    Combination with `fday_month`(`fday_year`) function:

    >>> dt = datetime.datetime(2048, 4, 16, 8, 32)
    >>> unit = datetime.timedelta(weeks=1)
    >>> base = dtround.fday_month(dt)
    >>> dtround.floor(dt, unit, base)
    datetime.datetime(2048, 4, 15, 0, 0)
    """
    return _base_func(dt, unit, base, _floor)

def ceil(dt, unit=timedelta(days=1), base=None):
    """
    Round up datetime/date object

    Parameters
    ----------
    dt : datetime.datetime or datetime.date
        datetime/date object to be rounded up
    unit : datetime.timedelta, optional
        rounding-up unit. Default is `datetime.timedelta(days=1)`.
    base : datetime.datetime or datetime.date, optional
        base datetime/date object. Default is `None`. If `None`, 
        `datetime.datetime(1970, 1, 1, tzinfo=dt.tzinfo)`/`datetime.date(1970,
        1, 1)` is used for this. This type must be the same as the type of
        `dt`.

    Returns
    -------
    output : datetime.datetime or datetime.date
        a value rounded up to the nearest `unit`.
        equal to `base + math.ceil((dt - base) / unit) * unit`

    See Also
    --------
    floor : Round down datetime/date object
    round : Round off datetime/date object

    Examples
    --------
    >>> dt = datetime.datetime(2048, 4, 16, 8, 32, 2, 65536)
    >>> unit = datetime.timedelta(minutes=15)
    >>> dtround.ceil(dt, unit)
    datetime.datetime(2048, 4, 16, 8, 45)

    Using `base` parameter:

    >>> dt = datetime.datetime(2048, 4, 22, 16, 32)
    >>> unit = datetime.timedelta(weeks=1)
    >>> base = datetime.datetime(2048, 4, 10)
    >>> dtround.ceil(dt, unit, base)
    datetime.datetime(2048, 4, 24, 0, 0)

    Combination with `fday_month`(`fday_year`) function:

    >>> dt = datetime.datetime(2048, 4, 16, 8, 32)
    >>> unit = datetime.timedelta(weeks=1)
    >>> base = dtround.fday_month(dt)
    >>> dtround.ceil(dt, unit, base)
    datetime.datetime(2048, 4, 22, 0, 0)
    """
    return _base_func(dt, unit, base, _ceil)

def round(dt, unit=timedelta(days=1), base=None):
    """
    Round off datetime/date object

    Parameters
    ----------
    dt : datetime.datetime or datetime.date
        dtetime/date object to be rounded off
    unit : datetime.timedelta, optional
        rounding-off unit. Default is `datetime.timedelta(days=1)`.
    base : datetime.datetime or datetime.date, optional
        base datetime/date object. Default is `None`. If `None`, 
        `datetime.datetime(1970, 1, 1, tzinfo=dt.tzinfo)`/`datetime.date(1970,
        1, 1)` is used for this. This type must be the same as the type of
        `dt`.

    Returns
    -------
    output : datetime.datetime or datetime.date
        a value rounded off to the nearest `unit`.
        equal to `base + builtins.round((dt - base) / unit) * unit`

    See Also
    --------
    floor : Round down datetime/date object
    ceil : Round up datetime/date object

    Examples
    --------
    >>> dt = datetime.datetime(2048, 4, 16, 8, 32, 2, 65536)
    >>> unit = datetime.timedelta(minutes=15)
    >>> dtround.round(dt, unit)
    datetime.datetime(2048, 4, 16, 8, 30)

    Using `base` parameter:

    >>> dt = datetime.datetime(2048, 4, 22, 16, 32)
    >>> unit = datetime.timedelta(weeks=1)
    >>> base = datetime.datetime(2048, 4, 10)
    >>> dtround.round(dt, unit, base)
    datetime.datetime(2048, 4, 24, 0, 0)

    Combination with `fday_month`(`fday_year`) function:

    >>> dt = datetime.datetime(2048, 4, 16, 8, 32)
    >>> unit = datetime.timedelta(weeks=1)
    >>> base = dtround.fday_month(dt)
    >>> dtround.round(dt, unit, base)
    datetime.datetime(2048, 4, 15, 0, 0)

    Notes
    -----
    Import with `from` statement overrides built-in `round` function.
    To avoid this use alias: `from dtround import round as dtround`.
    """
    return _base_func(dt, unit, base, _round)

def fday_month(dt):
    """
    Return the first day of the month of datetime/date object

    Parameters
    ----------
    dt : datetime.datetime or datetime.date

    Returns
    -------
    output : datetime.datetime or datetime.date
        the first day of the month of `dt`

    See Also
    --------
    fday_year : Return the first day of the year of datetime/date object

    Examples
    --------
    >>> dt = datetime.datetime(2048, 4, 22, 16, 32)
    >>> dtround.fday_month(dt)
    datetime.datetime(2048, 4, 1, 0, 0)
    """
    if type(dt) not in (datetime, date):
        raise TypeError('`dt` must be type of `datetime.datetime` '
                        'or `datetime.date`')
    return dt.__class__(dt.year, dt.month, 1)

def fday_year(dt):
    """
    Return the first day of the year of datetime/date object

    Parameters
    ----------
    dt : datetime.datetime or datetime.date

    Returns
    -------
    output : datetime.datetime or datetime.date
        the first day of the year of `dt`

    See Also
    --------
    fday_month : Return the first day of the month of datetime/date object

    Examples
    --------
    >>> dt = datetime.datetime(2048, 4, 22, 16, 32)
    >>> dtround.fday_year(dt)
    datetime.datetime(2048, 1, 1, 0, 0)
    """
    if type(dt) not in (datetime, date):
        raise TypeError('`dt` must be type of `datetime.datetime` '
                        'or `datetime.date`')
    return dt.__class__(dt.year, 1, 1)
