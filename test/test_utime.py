# -*- coding: utf-8 -*-
"""
UTime unittest class.

Use pytest package.
"""
import time
from datetime import datetime
import pytest
from ve_utils.utype import UType as Ut
from ve_utils.utime import UTime, PerfStats


class TestUTime:
    """UTime unittest class."""

    @staticmethod
    def test_get_timestamp_from_datetime():
        """Test get_timestamp_from_datetime method."""
        assert UTime.get_timestamp_from_datetime(None) is None
        assert Ut.is_float(UTime.get_timestamp_from_datetime(datetime.now()))

    @staticmethod
    def test_time_to_string():
        """Test time_to_string method."""
        assert UTime.time_to_string(
            UTime.get_utc_timestamp(1630193115.6428988)
        ) == '28/08/2021 23:25:15'
        assert UTime.time_to_string(
            UTime.get_utc_timestamp(1630193115.6428988),
            True
        ) == '28/08/2021 23:25:15 642899'
        assert UTime.time_to_string(None) is None
        assert UTime.time_to_string(
            99999999999999999999999999999999999999999999999999999999999999999999999999
            ) is None

    @staticmethod
    def test_get_elapsed_time():
        """Test get_elapsed_time method."""
        assert UTime.get_elapsed_time(32) <= Ut.get_int(time.time() + 32)
        assert UTime.get_elapsed_time(None) is None

    @staticmethod
    def test_string_to_time():
        """Test string_to_time method."""
        assert Ut.is_float(
            UTime.get_utc_timestamp(
                UTime.string_to_time('29/08/2021', '%d/%m/%Y')
            ),
            not_null=True
        )
        assert UTime.string_to_time('hello', 'world') is None
        assert UTime.string_to_time(dict(), list()) is None

    @staticmethod
    def test_get_time_search():
        """Test get_time_search method."""
        assert Ut.is_float(
            UTime.get_utc_timestamp(
                UTime.get_time_search(1630188000.0, '10:12:58')
            ),
            not_null=True
        )
        assert UTime.get_time_search(None) is None
        assert UTime.get_time_search(
            99999999999999999999999999999999999999999999999999999999999999999999999999999999999.99
        ) is None


@pytest.fixture(name="helper_manager", scope="class")
def helper_manager_fixture():
    """Json Schema test manager fixture"""
    class HelperManager:
        """Json Helper test manager fixture Class"""
        def __init__(self):
            self.obj = PerfStats()

    return HelperManager()


class TestPerfStats:
    """PerfStats unittest class."""
    def test_perf_methods(self, helper_manager):
        """Test perf methods."""
        assert not helper_manager.obj.has_perf()
        assert not helper_manager.obj.has_perf_key("myKey")

        helper_manager.obj.init_perf_key("myKey")
        assert helper_manager.obj.has_perf_key("myKey")
        data = {
                "start": 0.0,
                "counter": 0,
                "sum": 0.0,
                "avg": 0.0,
                "min": 0.0,
                "max": 0.0,
            }
        assert helper_manager.obj.get_perf_key("myKey") == data
        assert helper_manager.obj.get_perf_key_stat("myKey", "counter") == 0
        data = {
            "counter": 0,
            "avg": 0.0,
            "min": 0.0,
            "max": 0.0,
        }
        assert helper_manager.obj.serialize_perf_key("myKey") == data

        helper_manager.obj.init_perf(reset=True)
        assert not helper_manager.obj.has_perf()
        assert not helper_manager.obj.has_perf_key("myKey")

        helper_manager.obj.start_perf_key("myKey")
        assert helper_manager.obj.has_perf_key("myKey")
        assert helper_manager.obj.get_perf_key_stat("myKey", "start") > 0
        helper_manager.obj.init_perf(reset=True)

    def test_start_end_perf_methods(self, helper_manager):
        """Test perf methods."""
        for i in range(1, 6):
            helper_manager.obj.start_perf_key("myKey")
            time.sleep(0.2 * i)
            helper_manager.obj.end_perf_key("myKey")

        assert helper_manager.obj.has_perf_key("myKey")
        assert helper_manager.obj.get_perf_key_stat("myKey", "counter") == 5
        assert round(helper_manager.obj.get_perf_key_stat("myKey", "sum"), 0) == 3
        assert round(helper_manager.obj.get_perf_key_stat("myKey", "avg"), 1) == 0.6
        assert round(helper_manager.obj.get_perf_key_stat("myKey", "min"), 1) == 0.2
        assert round(helper_manager.obj.get_perf_key_stat("myKey", "max"), 0) == 1
