# -*- coding: utf-8 -*-
"""
Json helper methods.
Optional module.
"""
import simplejson as json
from typing import Optional

__author__ = "Eli Serra"
__copyright__ = "Copyright 2020, Eli Serra"
__deprecated__ = False
__license__ = "MIT"
__status__ = "Production"
__version__ = "2.0.0"


class UJson:
    """Json Helper methods."""

    @staticmethod
    def loads_json(data: str, raise_errors: bool = True, **kwargs) -> Optional[object]:
        """
        Return object from json string data.

        :Example :
            >>> UJson.loads_json("[0, 1, 2]")
            >>> [0, 1, 2]
            >>> UJson.loads_json("{key1")
            >>> {JSONDecodeError}Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
            # to desactivate exceptions set raise_errors to False
            # and method return None if exception occurs
            >>> UJson.loads_json("{key1", raise_errors=False)
            >>> None
            # you can set original simplejson loads parameters, egg :
            >>> UJson.loads_json("[0, 1, 2]", parse_float=Decimal)

        :param data: str: Original parameters from simplejson loads method
            the first parameter is string data to deserialize
        :param raise_errors: bool=True: Active or disable trowed exceptions.
            If False don't trow any exception only return None
        :return: Optional[object]:
            Deserialized json string, or None if raise_errors is False and exception is trowed
        :raises json.JSONDecodeError: will be raised if the given JSON string is not valid.
        .. seealso::  https://simplejson.readthedocs.io/en/latest/#simplejson.loads
        """
        result = None
        try:
            kwargs['s'] = data
            result = json.loads(**kwargs)
        except Exception as ex:
            if raise_errors:
                raise ex
        return result

    @staticmethod
    def load_json(data: object, raise_errors: bool = True, **kwargs) -> Optional[object]:
        """
        Return object from json file object.

        :Example :
            >>> with open("/xyz/json_data.json", "r") as content:
            >>>     UJson.load_json(content)
            >>> [0, 1, 2]
            # to desactivate exceptions set raise_errors to False
            # and method return None if exception occurs
            >>> with open("/xyz/bad_json.json", "r") as content:
            >>>     UJson.load_json(content, raise_errors=False)
            >>> None
            # you can set original simplejson load parameters, egg :
            >>> UJson.load_json(content, parse_float=Decimal)

        :param data: str: Json data to deserialize
        :param raise_errors: bool=True: Active or disable trowed exceptions.
            If False don't trow any exception only return None
        :return: Optional[object]:
            Deserialized json file, or None if raise_errors is False and exception is trowed
        :raises json.JSONDecodeError: will be raised if the given JSON document is not valid.
        .. seealso::  https://simplejson.readthedocs.io/en/latest/#simplejson.load
        """
        result = None
        try:
            result = json.load(data, **kwargs)
        except Exception as ex:
            if raise_errors:
                raise ex
        return result

    @staticmethod
    def dumps_json(data: object, raise_errors: bool = True, *args, **kwargs):
        """
        Return serialized json string from object.

        :Example :
            >>> UJson.dumps_json([0, 1, 2])
            >>> '[0, 1, 2]'
            # to desactivate exceptions set raise_errors to False
            # and method return None if exception occurs
            >>> UJson.dumps_json(UJson, raise_errors=False)
            >>> None
            # you can set original simplejson dumps parameters, egg :
            >>> UJson.dumps_json(content, parse_float=Decimal)

        :param data: str: Json data to deserialize
        :param raise_errors: bool=True: Active or disable trowed exceptions.
            If False don't trow any exception only return None
        :return: Optional[object]:
            Serialized json object as string, or None if raise_errors is False and exception is trowed
        .. seealso::  https://simplejson.readthedocs.io/en/latest/#simplejson.dumps
        """
        result = None
        try:
            result = json.dumps(data)
        except Exception as ex:
            if raise_errors:
                raise ex

        return result
