# -*- coding: utf-8 -*-
"""
Os and sys helper methods.

Contain static and class methods.
"""
import os
import sys
import time
from typing import Optional
from ve_utils.utype import UType
from ve_utils.utime import UTime

__author__ = "Eli Serra"
__copyright__ = "Copyright 2020, Eli Serra"
__deprecated__ = False
__license__ = "MIT"
__status__ = "Production"
__version__ = "2.0.0"


class USys:
    """Sys Helper methods."""

    color_list = dict(
        PURPLE='\033[95m',
        BLUE='\033[94m',
        GREEN='\033[92m',
        YELLOW='\033[93m',
        RED='\033[91m',
        ENDLINE='\033[0m',
        BOLD='\033[1m',
        UNDERLINE='\033[4m'
    )

    @classmethod
    def pipe_print(cls, *args):
        """Print args."""
        print(*args)

    @classmethod
    def get_text_to_print(cls,
                          text_to_print: str,
                          color: str,
                          with_time=True
                          ) -> str:
        """Append formatted time to printed string."""
        res = UType.get_str(text_to_print)
        if with_time:
            res = f"{UTime.time_to_string(time.time())} - {res}"

        if cls.color_list.get(color) is not None:
            res = f"{cls.color_list[color]}{res}{cls.color_list['ENDLINE']}"
        return res

    @classmethod
    def print_info(cls,
                   text_to_print: str,
                   with_time: bool = True
                   ) -> None:
        """Print text with info format, with BLUE color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "BLUE", with_time)
        )

    @classmethod
    def print_success(cls,
                      text_to_print: str,
                      with_time: bool = True
                      ) -> None:
        """Print text with success format, with GREEN color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "GREEN", with_time)
        )

    @classmethod
    def print_warning(cls,
                      text_to_print: str,
                      with_time: bool = True
                      ) -> None:
        """Print text with warning format, with YELLOW color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "YELLOW", with_time)
        )

    @classmethod
    def print_danger(cls,
                     text_to_print: str,
                     with_time: bool = True
                     ) -> None:
        """Print text with danger format, with YELLOW color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "RED", with_time)
        )

    @classmethod
    def print_header(cls,
                     text_to_print: str,
                     with_time: bool = True
                     ) -> None:
        """Print text with header format."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "HEADER", with_time)
        )

    @classmethod
    def print_purple(cls,
                     text_to_print: str,
                     with_time: bool = True
                     ) -> None:
        """Print text with purple color."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "PURPLE", with_time)
        )

    @classmethod
    def print_bold(cls,
                   text_to_print: str,
                   with_time: bool = True
                   ) -> None:
        """Print bold text."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "BOLD", with_time)
        )

    @classmethod
    def print_underline(cls,
                        text_to_print: str,
                        with_time: bool = True
                        ) -> None:
        """Print underlined text."""
        USys.pipe_print(
            USys.get_text_to_print(text_to_print, "UNDERLINE", with_time)
        )

    @staticmethod
    def get_operating_system() -> str:
        """
        Return the operating system of the computer running this code.

        :return: the name of the operating system (Linux, MacOs or Windows).
        """

        platform = sys.platform
        if platform.startswith('linux') or platform.startswith('cygwin'):
            return "Linux"
        elif platform.startswith('darwin'):
            return "MacOs"
        elif platform.startswith('win'):
            return "Windows"
        else:
            raise EnvironmentError('Unsupported platform')

    @staticmethod
    def get_operating_system_type() -> Optional[str]:
        """
        Return the operating system type.

        :return: the operating system type (unix or win32).
        """
        try:
            op = USys.get_operating_system()
            if op == "Linux" or op == "MacOs":
                return "unix", op
            elif op == "Windows":
                return "win32", op
        except Exception:
            return None
        return None

    @staticmethod
    def is_op_sys_type(system: str) -> bool:
        """
        Return True if the operating system type is sys.

        :param system: Used to determine the operating system type.
        :return:
            True if the operating system type is equal to sys,
            and False otherwise.
        """
        op_sys = USys.get_operating_system_type()
        return op_sys is not None and op_sys[0] == system

    @staticmethod
    def is_op_sys(system: str) -> bool:
        """
        Return True if the operating system is sys, and False otherwise.

        :param system: Used to determine which operating system is being used.
        :return:
            True if the operating system is equal to sys,
            and False otherwise.
        """
        op_sys = USys.get_operating_system()
        return op_sys is not None and op_sys == system

    @staticmethod
    def get_current_file_parent_parent_path(current_script_path: str) -> str:
        """
        Return the parent of the parent directory of this file.

        :param current_script_path: Used to get the path of the current script.
        :return: the parent of the parent of the current script's path.
        """
        return os.path.normpath(
            os.path.join(current_script_path, os.pardir, os.pardir)
        )

    @staticmethod
    def get_current_file_parent_path(current_script_path: str) -> str:
        """
        Return the parent path of the current file.

        :param current_script_path: Used to get the path of the current script.
        :return: the parent path of the current script.
        """
        return os.path.normpath(
            os.path.join(current_script_path, os.pardir)
        )
