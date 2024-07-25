# -*- coding: utf-8 -*-
"""
UJson unittest class.

Use pytest package.
"""
import os
import inspect
import pytest
import simplejson as json
from ve_utils.ujson import UJson
from ve_utils.utype import UType as Ut


class TestUJson:

    """UJson unittest class."""
    @staticmethod
    def test_loads_json():
        """Test loads_json method."""
        json_data = '{'\
            '"key1": "my value", '\
            '"key2": ["array_value_1"], '\
            '"key3": false, '\
            '"key4": 10, '\
            '"key5": "0.0258001"'\
        '}'
        data = UJson.loads_json(json_data)
        assert Ut.is_dict(data, not_null=True) and len(data) == 5
        assert data.get("key1") == "my value"
        assert data.get("key2") == ["array_value_1"]
        assert data.get("key3") is False
        assert data.get("key4") == 10
        assert data.get("key5") == "0.0258001"

        assert UJson.loads_json("{key1", raise_errors=False) is None
        with pytest.raises(json.JSONDecodeError):
            UJson.loads_json("{key1")

    @staticmethod
    def test_load_json():
        """Test load_json method."""
        current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        jpath = os.path.join(current_path, "dummy_data", "dummy.json")
        with open(jpath, "r", encoding="utf-8") as content:
            data = UJson.load_json(content)
        assert Ut.is_dict(data, not_null=True) and len(data) == 5
        assert data.get("key1") == "my value"
        assert data.get("key2") == ["array_value_1", "array_value_2"]
        assert data.get("key3") is False
        assert data.get("key4") == 10
        assert data.get("key5") == 0.0258001

        assert UJson.load_json("{key1", raise_errors=False) is None
        with pytest.raises(AttributeError):
            UJson.load_json("{key1")

    @staticmethod
    def test_dumps_json():
        """Test dumps_json method."""
        json_data = {
            "key1": "my value",
            "key2": ["array_value_1"],
            "key3": False,
            "key4": 10,
            "key5": 0.0258001
        }
        data = UJson.dumps_json(json_data)
        assert Ut.is_str(data, not_null=True)
        assert data == '{'\
            '"key1": "my value", '\
            '"key2": ["array_value_1"], '\
            '"key3": false, '\
            '"key4": 10, '\
            '"key5": 0.0258001'\
        '}'

        assert UJson.dumps_json(Ut, raise_errors=False) is None
        with pytest.raises(TypeError):
            UJson.dumps_json(Ut)
