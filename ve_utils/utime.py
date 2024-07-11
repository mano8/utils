# -*- coding: utf-8 -*-
"""
Time and date helper methods.

Contain only static methods.
"""
import time
from datetime import datetime
from typing import Optional, Union
from ve_utils.utype import UType as Ut

__author__ = "Eli Serra"
__copyright__ = "Copyright 2020, Eli Serra"
__deprecated__ = False
__license__ = "MIT"
__status__ = "Production"
__version__ = "2.0.0"


class UTime:
    """Time Helper methods."""

    @staticmethod
    def get_timestamp_from_datetime(date_time: datetime
                                    ) -> Optional[float]:
        """Get timestamp from datetime object."""
        result = None
        if isinstance(date_time, datetime):
            result = datetime.timestamp(date_time)
        return result

    @staticmethod
    def get_utc_timestamp(timestamp: Union[int, float]) -> float:
        """Get timestamp from datetime object."""
        result = None
        if Ut.is_numeric(timestamp, not_null=True):
            result = UTime.get_timestamp_from_datetime(
                datetime.utcfromtimestamp(timestamp)
            )
        return result

    @staticmethod
    def time_to_string(
                       timestamp: Union[int, float],
                       micro: bool = False
                       ) -> Optional[str]:
        """
        Convert a time in seconds to a string.

        :Example :
            >>> UTime.time_to_string(1664666756.1650662)
            >>> '02/10/2022 01:25:56'
        :param timestamp: Used to convert the time in seconds to a string,
        :param micro:
            Used to specify whether the microseconds
            should be included in the string.
        :return:
            a string representation of the time passed,
            if it is not a float then it returns None.
        """
        result = None
        if Ut.is_numeric(timestamp):
            try:
                date_time = datetime.fromtimestamp(timestamp)
                if micro:
                    result = date_time.strftime('%d/%m/%Y %H:%M:%S %f')
                else:
                    result = date_time.strftime('%d/%m/%Y %H:%M:%S')

            except Exception:
                pass

        return result

    @staticmethod
    def get_elapsed_time(
                            tim: Union[int, float],
                            default: Optional[Union[int, float]] = None
                            ) -> Optional[Union[int, float]]:
        """
        Return the elapsed time between two timestamps.

        :Example :
            >>> UTime.get_elapsed_time(time.time() - 1)
            >>> 1
        :param tim: Used to pass in the time that is being converted,
        :param default:
            Used to specify a default value to return
            if the input is not an integer or float.
        :return:
            the time if it's an integer or float,
            otherwise it returns default value.
        """
        result = default
        if Ut.is_numeric(tim):
            result = time.time()-Ut.get_float(tim)
        return result

    @staticmethod
    def string_to_time(
            text: str,
            time_format: str,
            default: Optional[float] = None
            ) -> Optional[float]:
        """
        Convert a string to a time object.

        :Example :
            >>> UTime.string_to_time('02/10/2022 01:25:56', '%d/%m/%Y %H:%M:%S')
            >>> 1664666756.0
        :param text: Used to specify the string to be converted,
        :param time_format:
            Used to specify the format of the string
            that is being converted to a time object,
        :param default: Used to set a default value for the function.
        :return: a time object converted from the given string and format.
        """
        result = default
        if Ut.is_str(text) and Ut.is_str(time_format):
            try:
                result = time.mktime(time.strptime(text, time_format))
            except Exception:
                pass
        return result

    @staticmethod
    def get_time_search(
            timestamp: Union[int, float],
            time_search: str = '23:59:59'
            ) -> Union[int, float]:
        """
        Return formatted time.

        :Example :
            >>> UTime.get_time_search(1664666756.0, '10:50:20')
            >>> 1664614220
        :param timestamp: Used to pass the time in seconds since epoch,
        :param time_search:
            Used to set the time to 23:59:59,
            so that all logs from that day are returned.
        :return: the time search given the timeB.
        :doc-author: Trelent
        """
        result = None
        if Ut.is_float(timestamp):
            try:
                gmt_tuple = time.gmtime(timestamp)
                result = time.mktime(
                    time.strptime(
                        "%s-%s-%s %s" % (
                            str(gmt_tuple[2]),
                            str(gmt_tuple[1]),
                            str(gmt_tuple[0]),
                            str(time_search)
                        ),
                        "%d-%m-%Y %H:%M:%S"
                    )
                )
            except Exception:
                pass
        return result


class PerfStats:
    """Perf Helper Class."""

    def __init__(self):
        self.perf = dict()

    def _set_sum(self, key: str, elapsed: float):
        """Set sum of elapsed times for key."""
        self.perf[key]['sum'] += elapsed

    def _set_min(self, key: str, elapsed: float):
        """Set min time elapsed for key."""
        if elapsed < self.perf[key]['min'] > 0 \
                or self.perf[key]['min'] == 0:
            self.perf[key]['min'] = elapsed

    def _set_max(self, key: str, elapsed: float):
        """Set max time elapsed for key."""
        if elapsed > self.perf[key]['max'] >= 0:
            self.perf[key]['max'] = elapsed

    def _set_avg(self, key: str):
        """Set avg time elapsed for key."""
        if self.perf[key]['counter'] > 0:
            self.perf[key]['avg'] = self.perf[key]['sum'] / self.perf[key]['counter']

    def _set_stats(self, key: str, elapsed: float):
        """Set Perf stats for key."""
        if self.has_perf_key(key) \
                and Ut.is_float(elapsed, positive=True):
            self.perf[key]['counter'] += 1
            self._set_sum(key=key, elapsed=elapsed)
            self._set_min(key=key, elapsed=elapsed)
            self._set_max(key=key, elapsed=elapsed)
            self._set_avg(key=key)

    def has_perf(self):
        """Test if instance has perf property."""
        return Ut.is_dict(self.perf, not_null=True)

    def init_perf(self, reset: bool = False):
        """Init perf property."""
        if not Ut.is_dict(self.perf) or reset is True:
            self.perf = dict()

    def has_perf_key(self, key: str):
        """Test if instance has perf property."""
        return self.has_perf() and Ut.is_dict(self.perf.get(key), not_null=True)

    def init_perf_key(self, key: str, reset: bool = False):
        """Init perf key."""
        self.init_perf()
        if not self.has_perf_key(key) or reset is True:
            self.perf[key] = {
                "start": 0.0,
                "counter": 0,
                "sum": 0.0,
                "avg": 0.0,
                "min": 0.0,
                "max": 0.0,
            }

    def get_perf_key(self, key: str):
        """Get Perf key stats."""
        result = None
        if self.has_perf_key(key):
            result = self.perf.get(key)
        return result

    def get_perf_key_stat(self, key: str, stat: str):
        """Get particular stat for key."""
        result = None
        if self.has_perf_key(key):
            result = self.perf[key].get(stat)
        return result

    def serialize_perf_key(self, key: str):
        """Serialize Perf Stats for key."""
        result = None
        if self.has_perf_key(key):
            result = Ut.get_items_from_dict(
                self.perf.get(key),
                ['counter', 'avg', 'min', 'max']
            )
        return result

    def start_perf_key(self, key: str):
        """Start perf stats for key."""
        self.init_perf_key(key)
        self.perf[key]['start'] = time.perf_counter()

    def end_perf_key(self, key: str):
        """End perf stats for key."""
        result = 0.0
        if self.has_perf_key(key) \
                and Ut.is_float(self.perf[key].get('start'), positive=True):
            result = PerfStats.get_elapsed(self.perf[key]['start'])
            self._set_stats(key, result)
        return result

    @staticmethod
    def get_elapsed(start: float) -> float:
        """Get elapsed time."""
        return time.perf_counter() - start
