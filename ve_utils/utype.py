# -*- coding: utf-8 -*-
"""
Helper used to test and format data.

Contain only static methods.
"""
from typing import Optional, Union

__author__ = "Eli Serra"
__copyright__ = "Copyright 2020, Eli Serra"
__deprecated__ = False
__license__ = "MIT"
__status__ = "Production"
__version__ = "2.0.0"


class UType:
    """
    Helper class of static methods, used to test and format data, and some extra helper utilities.
    """

    @staticmethod
    def has_valid_length(test: bool,
                         value: any,
                         not_null: bool = False,
                         mini: int = None,
                         maxi: int = None,
                         eq: int = None,
                         source: str = 'void'
                         ) -> bool:
        """
        Helper used in type test methods, to validate the length of value.

        :Example :
            - $> value = 'txt'
            - $> UType.has_valid_length(test=isinstance(value, str), not_null=True)
            - $> True

        :param test: the result of test from caller method,
        :param value: input value tested
        :param not_null: if True, input value can't be null, False by default
        :param mini: Min length of input value,
            must be bigger or equal than 0,
            and smaller or equal than maxi
            (None by default)
        :param maxi: Max length of input value,
            must be bigger or equal than 0,
            and bigger than mini
            (None by default)
        :param eq: equal length of input value
        :param source: source of call (method name).
        :return: True if the test is True and the given value has valid length,
                 otherwise False.
        :raises AttributeError: if the mini and or maxi values are not valid
        :raises TypeError: If the test value is True
            And length of value can't be determined.
        """
        if (mini is not None and mini < 0) \
                or (eq is not None and eq < 0) \
                or (maxi is not None and maxi <= 0) \
                or (mini is not None
                    and maxi is not None
                    and maxi < mini):
            raise AttributeError(
                "[UType::%s::has_valid_length] Fatal error : "
                "Unable to validate the value length, "
                "eq  and/or mini and/or maxi are not valid."
                "eq: %s - mini: %s - maxi: %s " %
                (UType.get_str(source), eq, mini, maxi)
            )

        if not test:
            return False
        elif not not_null\
                and eq is None\
                and mini is None\
                and maxi is None:
            return True
        else:
            val_len = len(value)
            return (not not_null
                    or (not_null and val_len > 0))\
                and (eq is None
                     or val_len == eq)\
                and (mini is None
                     or eq is not None
                     or 0 <= mini <= val_len) \
                and (maxi is None
                     or eq is not None
                     or 0 < maxi >= val_len)

    @staticmethod
    def has_valid_value(test: bool,
                        value: any,
                        not_null: bool = False,
                        positive: bool = False,
                        negative: bool = False,
                        mini: int = None,
                        maxi: int = None,
                        eq: int = None,
                        source: str = 'void'
                        ) -> bool:
        """
        Helper used in type test methods, to validate the numeric value.

        :Example :
            - $> value = 5
            - $> UType.has_valid_value(test=isinstance(value, int), eq=5)
            - $> True

        :param test: the result of test from caller method,
        :param value: input value tested
        :param not_null: if True, input value can't be null, False by default
        :param positive: if True, input value must be positive, False by default
        :param negative: if True, input value must be negative, False by default
        :param mini: Min value of input
            must be bigger or equal than 0,
            and smaller or equal than maxi
            (None by default)
        :param maxi: Max value of input
            must be bigger or equal than 0,
            and bigger than mini
            (None by default)
        :param eq: equal value of input
        :param source: source of call (method name).
        :return: True if the test is True and the given value has valid length,
                 otherwise False.
        :raises AttributeError: if the mini and or maxi values are not valid
        :raises TypeError: If the test value is True
            And length of value can't be determined.
        """
        if (eq is not None
                and (maxi is not None
                     or mini is not None
                     or not_null is True
                     or positive is True
                     or negative is True)) \
                or (mini is not None
                    and maxi is not None
                    and maxi < mini):
            raise AttributeError(
                "[UType::%s::has_valid_value] Fatal error : "
                "Unable to validate the value of input, "
                "if eq value is provided : "
                "you can't provide not_null, positive, negative, mini or maxi values. "
                "Or maxi value is bigger than mini value. "
                "not_null: %s - eq: %s - mini: %s - maxi: %s " %
                (UType.get_str(source), not_null, eq, mini, maxi)
            )

        return test \
            and (not not_null
                 or (not_null and value != 0)) \
            and (not positive
                 or (positive and value > 0)) \
            and (not negative
                 or (negative and value < 0)) \
            and (eq is None
                 or value == eq) \
            and (mini is None
                 or eq is not None
                 or mini <= value) \
            and (maxi is None
                 or eq is not None
                 or maxi >= value)

    @staticmethod
    def is_str(value: any,
               not_null: bool = False,
               mini: Optional[int] = None,
               maxi: Optional[int] = None,
               eq: int = None
               ) -> bool:
        """
        Check if the given value is a str instance.

        :Example :
            - > UType.is_str( "tmp" ) => True
            - > UType.is_str(value="tmp", not_null=True) => True
            - > UType.is_str( 0 ) => False
        :param value: Input value to test
        :param not_null: if True, input value can't be null, False by default
        :param mini: Min length value
        :param maxi: Max length value
        :param eq: equal length of input value
        :return: True if the given value is a str instance, otherwise False.
        """
        return UType.has_valid_length(test=isinstance(value, str),
                                      value=value,
                                      not_null=not_null,
                                      mini=mini,
                                      maxi=maxi,
                                      eq=eq,
                                      source='is_str')

    @staticmethod
    def is_bool(value: any) -> bool:
        """
        Check if the given value is a bool instance.

        :Example :
            - > UType.is_bool( True )
            - > True
            - > UType.is_bool( 1 )
            - > True
        :param value: Input value to test
        :return: True if the given value is a bool instance, otherwise False.
        """
        return isinstance(value, bool)

    @staticmethod
    def is_int(value: any,
               not_null: bool = False,
               positive: bool = False,
               negative: bool = False,
               mini: Optional[int] = None,
               maxi: Optional[int] = None,
               eq: int = None
               ) -> bool:
        """
        Check if the given value is an int instance.

        :Example :
            - > UType.is_int( 1 )
            - > True
            - > UType.is_int( 1.2 )
            - > False
        :param value: Input value to test
        :param not_null: if True, input value can't be null, False by default
        :param positive: if True, input value must be positive, False by default
        :param negative: if True, input value must be negative, False by default
        :param mini: Min value of input
        :param maxi: Max value of input
        :param eq: equal value of input
        :return: True if the given value is an int instance, otherwise False.
        """
        return UType.has_valid_value(test=isinstance(value, int),
                                     value=value,
                                     not_null=not_null,
                                     positive=positive,
                                     negative=negative,
                                     mini=mini,
                                     maxi=maxi,
                                     eq=eq,
                                     source='is_int')

    @staticmethod
    def is_float(value: any,
                 not_null: bool = False,
                 positive: bool = False,
                 negative: bool = False,
                 mini: Optional[int] = None,
                 maxi: Optional[int] = None,
                 eq: int = None
                 ) -> bool:
        """
        Check if the given value is a float instance.

        :Example :
            - > UType.is_float( 1.2 )
            - > True
            - > UType.is_float( 1 )
            - > False
        :param value: Input value to test
        :param not_null: if True, input value can't be null, False by default
        :param positive: if True, input value must be positive, False by default
        :param negative: if True, input value must be negative, False by default
        :param mini: Min value of input
        :param maxi: Max value of input
        :param eq: equal value of input
        :return: True if the given value is a float instance, otherwise False.
        """
        return UType.has_valid_value(test=isinstance(value, float),
                                     value=value,
                                     not_null=not_null,
                                     positive=positive,
                                     negative=negative,
                                     mini=mini,
                                     maxi=maxi,
                                     eq=eq,
                                     source='is_float')

    @staticmethod
    def is_numeric(value: any,
                   not_null: bool = False,
                   positive: bool = False,
                   negative: bool = False,
                   mini: Optional[int] = None,
                   maxi: Optional[int] = None,
                   eq: int = None
                   ) -> bool:
        """
        Check if the given value is an int or float instance.

        :Example :
            - > UType.is_numeric( 1.2 )
            - > True
            - > UType.is_numeric( 1 )
            - > True
        :param value: Input value to test
        :param not_null: if True, input value can't be null, False by default
        :param positive: if True, input value must be positive, False by default
        :param negative: if True, input value must be negative, False by default
        :param mini: Min value of input
        :param maxi: Max value of input
        :param eq: equal value of input
        :return: True if the given value is an int or float instance,
                 otherwise False.
        """
        return UType.is_int(value,
                            not_null=not_null,
                            positive=positive,
                            negative=negative,
                            mini=mini, maxi=maxi,
                            eq=eq)\
            or UType.is_float(value,
                              not_null=not_null,
                              positive=positive,
                              negative=negative,
                              mini=mini,
                              maxi=maxi,
                              eq=eq)

    @staticmethod
    def is_dict(value: any,
                not_null: bool = False,
                min_items: Optional[int] = None,
                max_items: Optional[int] = None,
                eq: int = None
                ) -> bool:
        """
        Check if the given value is a dict instance.

        :Example :
            - > UType.is_dict( dict() )
            - > True
        :param value: Input value to test
        :param not_null: if True, input value can't be null, False by default
        :param min_items: Min dict items
        :param max_items: Max dict items
        :param eq: equal length of input value
        :return: True if the given value is a dict instance, otherwise False.
        """
        return UType.has_valid_length(test=isinstance(value, dict),
                                      value=value,
                                      not_null=not_null,
                                      mini=min_items,
                                      maxi=max_items,
                                      eq=eq,
                                      source='is_dict')

    @staticmethod
    def is_dict_key(value: any,
                    not_null: bool = False,
                    mini: Optional[int] = None,
                    maxi: Optional[int] = None,
                    eq: int = None
                    ) -> bool:
        """
        Check if the given value is a valid dict key.


        :param value: dict key to test
        :param not_null: if True, input value can't be null, False by default
        :param mini: Min value
        :param maxi: Max value
        :param eq: equal length of input value
        :return: True if the given value is a valid dict key, otherwise False.
        """
        return UType.is_int(value=value,
                            not_null=not_null,
                            mini=mini,
                            maxi=maxi,
                            eq=eq) or\
            UType.is_str(value,
                         not_null=True,
                         mini=mini,
                         maxi=maxi,
                         eq=eq) or\
            UType.is_tuple(value=value,
                           not_null=not_null,
                           min_items=mini,
                           max_items=maxi,
                           eq=eq)

    @staticmethod
    def is_str_dict_key(value: any,
                        mini: Optional[int] = None,
                        maxi: Optional[int] = None,
                        eq: int = None
                        ) -> bool:
        """
        Check if the given value is a valid string dict key.


        :param value: dict key to test
        :param mini: Min value length
        :param maxi: Max value length
        :param eq: equal length of input value
        :return: True if the given value is a valid dict key, otherwise False.
        """
        return UType.is_str(value=value,
                            not_null=True,
                            mini=mini,
                            maxi=maxi,
                            eq=eq)

    @staticmethod
    def is_tuple(value: any,
                 not_null: bool = False,
                 min_items: Optional[int] = None,
                 max_items: Optional[int] = None,
                 eq: int = None
                 ) -> bool:
        """
        Check if the given value is a tuple instance.

        :param value: Input value to test
        :param not_null: if True, input value can't be null, False by default
        :param min_items: Min tuple items
        :param max_items: Max tuple items
        :param eq: equal length of input value
        :return: True if the given value is a tuple instance, otherwise False.
        """
        return UType.has_valid_length(test=isinstance(value, tuple),
                                      value=value,
                                      not_null=not_null,
                                      mini=min_items,
                                      maxi=max_items,
                                      eq=eq,
                                      source='is_tuple')

    @staticmethod
    def is_list(value: any,
                not_null: bool = False,
                min_items: Optional[int] = None,
                max_items: Optional[int] = None,
                eq: int = None
                ) -> bool:
        """
        Check if the given value is a list instance.

        :param value: Input value to test
        :param not_null: if True, input value can't be null, False by default
        :param min_items: Min list items
        :param max_items: Max list items
        :param eq: equal length of input value
        :return: True if the given value is a list instance, otherwise False.
        """
        return UType.has_valid_length(test=isinstance(value, list),
                                      value=value,
                                      not_null=not_null,
                                      mini=min_items,
                                      maxi=max_items,
                                      eq=eq,
                                      source='is_list')

    @staticmethod
    def get_valid_data_type_string_test() -> list:
        """Return list of valid string data types to test"""
        return ["str", "bool", "int", "float", "numeric", "dict", "tuple", "list"]

    @staticmethod
    def get_valid_data_types_test() -> list:
        """Return list of valid data types to test"""
        return [str, bool, int, float, dict, tuple, list]

    @staticmethod
    def is_valid_format(value: any,
                        data_type: Union[str, type],
                        not_null: bool = False,
                        positive: bool = False,
                        negative: bool = False,
                        mini: Optional[int] = None,
                        maxi: Optional[int] = None,
                        eq: int = None
                        ) -> Optional[bool]:
        """
        Check if input value is a data_type format

        :param value: Input value to test the data type
        :param data_type: The data type to test format of the value
        :param not_null: if True, input value can't be null, False by default
        :param positive: if True, input value must be positive, False by default
            Only for numeric values
        :param negative: if True, input value must be negative, False by default
            Only for numeric values
        :param mini: Min length or value
        :param maxi: Max length or value
        :param eq: equal length of input value
        :return: True if correct data type, False if not.
                 Otherwise, it returns default value, if no data type found.
        """
        if data_type == "str" or data_type == str:
            return UType.is_str(value=value,
                                not_null=not_null,
                                mini=mini,
                                maxi=maxi,
                                eq=eq)
        elif data_type == "bool" or data_type == bool:
            return UType.is_bool(value)
        elif data_type == "int" or data_type == int:
            return UType.is_int(value,
                                not_null=not_null,
                                positive=positive,
                                negative=negative,
                                mini=mini,
                                maxi=maxi,
                                eq=eq)
        elif data_type == "float" or data_type == float:
            return UType.is_float(value,
                                  not_null=not_null,
                                  positive=positive,
                                  negative=negative,
                                  mini=mini,
                                  maxi=maxi,
                                  eq=eq)
        elif data_type == "numeric":
            return UType.is_numeric(value,
                                    not_null=not_null,
                                    positive=positive,
                                    negative=negative,
                                    mini=mini,
                                    maxi=maxi,
                                    eq=eq)
        elif data_type == "dict" or data_type == dict:
            return UType.is_dict(value,
                                 not_null=not_null,
                                 min_items=mini,
                                 max_items=maxi,
                                 eq=eq)
        elif data_type == "tuple" or data_type == tuple:
            return UType.is_tuple(value,
                                  not_null=not_null,
                                  min_items=mini,
                                  max_items=maxi,
                                  eq=eq)
        elif data_type == "list" or data_type == list:
            return UType.is_list(value,
                                 not_null=not_null,
                                 min_items=mini,
                                 max_items=maxi,
                                 eq=eq)
        raise AttributeError(
            "[UType::is_valid_format] Fatal error : "
            "Bad data_type value, "
            "must be in %s."
            "value: %s - data_type: %s " %
            (UType.get_valid_data_type_string_test(),
             UType.get_str(value),
             UType.get_str(data_type)
             )
        )

    @staticmethod
    def get_int(value: any, default: Optional[int] = 0) -> Optional[int]:
        """
        Take a value and returns it as an integer.

        :param value: Input value to return as an integer.
        :param default: Used to set a default value.
        :return: the integer part of the number that is passed to it,
                 otherwise it returns the default value.
        """
        try:
            return int(value)
        except Exception:
            return default

    @staticmethod
    def get_float(value: any, default: Optional[float] = 0.0) -> Optional[float]:
        """
        Take a value and returns it as a float value.

        :param value: Input value to return as a float.
        :param default: Used to define the default value.
        :return: a float if the argument is a number,
                 otherwise it returns the default value.
        """
        try:
            return float(value)
        except Exception:
            return default

    @staticmethod
    def get_rounded_float(nb: any,
                          rnd: int,
                          default: Optional[float] = 0.0
                          ) -> Optional[float]:
        """
        Return the rounded value of a float number.

        :param nb: Used to pass the value to be rounded.
        :param rnd: Used to specify the number of digits after the comma.
        :param default: Used to specify a default value.
        :return: the rounded float value of a number,
                 otherwise it returns the default value.
        """
        try:
            return round(UType.get_float(nb), rnd)
        except Exception:
            return default

    @staticmethod
    def get_str(value: any, default: Optional[str] = None) -> Optional[str]:
        """
        Take a value and returns it as a str value.

        :param value: Input value to return as a str.
        :param default: Used to define the default value.
        :return: a str if the argument is a str,
                 otherwise it returns the default value.
        """
        try:
            return str(value)
        except Exception:
            return default

    @staticmethod
    def get_valid_data_type_string_format() -> list:
        """Return list of valid string data types to test"""
        return ["str", "bool", "int", "float", "numeric", "time", "onOff", "intBool", "intString"]

    @staticmethod
    def format_by_type(value: any,
                       data_type: str,
                       float_round: Optional[int] = None
                       ):
        """
        Format value to data_type format.

        :param value: Input value to format.
        :param data_type: The data type to format the value.
        :param float_round:
            When data type is float,
            value can be rounded from number of decimal places.
            Defaults to None.
        :return: a formatted value, otherwise it returns None.
        """
        if data_type == "int":
            return UType.get_int(value)
        elif data_type in ["float", "numeric", "time"]:
            if float_round is not None:
                return UType.get_rounded_float(
                    value,
                    float_round
                    )
            return UType.get_float(value)
        elif data_type == "onOff":
            return UType.bool_to_on_off(value)
        elif data_type == "intBool":
            return UType.string_to_int_bool(value)
        elif data_type == "bool":
            return UType.str_to_bool(value)
        elif data_type == "str":
            return UType.get_str(value)
        elif data_type == "intString":
            return UType.int_to_formatted_string(value)
        raise AttributeError(
            "[UType::format_by_type] Fatal error : "
            "Bad data_type value, "
            "must be in %s."
            "value: %s - data_type: %s " %
            (UType.get_valid_data_type_string_format(),
             UType.get_str(value),
             UType.get_str(data_type)
             )
        )

    @staticmethod
    def int_to_formatted_string(
            nb: int,
            default: Optional[str] = None
            ) -> Optional[str]:
        """
        Take an integer and returns a string with the number formatted.

        Format the number than two digits (if the number is less than 10),
        :param nb: Used to store the number that will be converted to a string,
        :param default: Used to define the default value.
        :return:
            a string of the number nb formatted as a two-digit number
            if it is less than 10 and greater or equal to 0,
            and returns an empty string otherwise.
        """
        if UType.is_int(nb):
            if 10 > nb >= 0:
                return "0%s" % nb
            return "%s" % nb
        return default

    @staticmethod
    def str_to_bool(
            s: Union[str, int, bool],
            default: Optional[bool] = False
            ) -> Optional[bool]:
        """
        Convert a string or an int to a boolean.


        :param s: Used to pass the value to be converted.
        :param default: Used to set a default value for the parameter.
        :return:
            True if the input is 'True', '1',
            or other boolean-like values.
        """
        if UType.is_bool(s):  # do not convert if already a boolean
            return s
        elif UType.is_str(s):
            if s.lower() == 'true' \
                    or s == '1' \
                    or s.lower() == 'on' \
                    or s.lower() == 'ok':
                return True
            elif s.lower() == 'false' \
                    or s == '0' \
                    or s.lower() == 'off' \
                    or s.lower() == 'error':
                return False
        elif UType.is_int(s):
            return s == 1
        return default

    @staticmethod
    def bool_to_int_text(value: Union[str, int, bool]) -> str:
        """
        Take a boolean value and returns an integer.

        :param value: Used to check if the input is a boolean value.
        :return: the value of the value parameter.
        """
        if UType.str_to_bool(value):
            return "1"
        return "0"

    @staticmethod
    def bool_to_on_off(value: Union[str, int, bool]) -> str:
        """
        Convert a boolean value to either 'on' or 'off'.

        :param value:
            Used to pass a value that is to be converted into a boolean.
        :return:
            the string "on" if the value is True
            and returns the string "off" if it's False.
        """
        if UType.str_to_bool(value):
            return "On"
        return "Off"

    @staticmethod
    def bool_to_str_state(value: Union[str, int, bool]) -> str:
        """
        Take a boolean value and returns "Ok"/"Not Ok" string.

        :param value: Used to determine if the state is 'Ok' or not.
        :return: the boolean value of the string passed to it.
        """
        if UType.str_to_bool(value):
            return "Ok"
        return "Error"

    @staticmethod
    def string_to_int_bool(text: Union[str, int, bool]) -> int:
        """
        Convert a string to an integer.

        :param text: Used to convert the string to a boolean value.
        :return:
            the integer 1 if the string is true
            and 0 if the string is false.
        """
        if UType.str_to_bool(text):
            return 1
        else:
            return 0

    @staticmethod
    def string_to_float(
            text: str,
            default: Optional[float] = 0.0
            ) -> Optional[float]:
        """
        Convert a string to a float.

        :param text:
            Used to pass the string that is to be converted into a float.
        :param default: Used to set a default value for the function.
        :return: the float representation of the input text string.
        """
        if UType.is_str(text):
            try:
                text = text.replace(',', '.')
                return UType.get_float(text)
            except Exception:
                return default
        elif UType.is_float(text):
            return text
        return default

    @staticmethod
    def init_dict(data: Optional[dict]) -> dict:
        """
        Return an empty dictionary if data is not an instance of dict.

        :param data: Used to pass the property to initialise.
        :return: An empty dictionary if data is not an instance of dict.
        """
        if not UType.is_dict(data):
            data = dict()
        return data

    @staticmethod
    def init_dict_key(
            data: Optional[dict],
            key: Union[str, int, tuple],
            init_value: any
            ) -> dict:
        """
        Initialise the dictionary key value with init_value.

        If the dictionary key is not valid, raise ValueError.
        Set key value to init_value if is not an instance of init_value type.

        :param data: Used to pass the dictionary.
        :param key: Used to pass the dictionary key.
        :param init_value: Used to pass the default dictionary key value.
        :return: data with key value initialised to default value or
                 the data param.
        """
        if not UType.is_dict_key(key):
            raise ValueError(
                "[init_dict_key] Error : dictionary key is not valid."
                )

        data = UType.init_dict(data)
        if not isinstance(data.get(key), type(init_value)):
            data[key] = init_value
        return data

    @staticmethod
    def get_items_from_dict(data: dict, list_keys: list) -> dict:
        """
        Return a dictionary containing the keys from list_keys.

        :param data: Used to pass the dictionary to be searched.
        :param list_keys:
            Used to specify the keys,
            that we want to extract from the dictionary.
        :return: the list of keys found in the dictionary data.
        """
        res = dict()
        if UType.is_dict(data, not_null=True) and UType.is_list(list_keys, not_null=True):
            for key in list_keys:
                if UType.is_str(key) and key in data:
                    res[key] = data.get(key)
        return res
