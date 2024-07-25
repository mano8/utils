# -*- coding: utf-8 -*-
"""
USys unittest class.

Use pytest package.
"""
import os
import inspect
from ve_utils.utype import UType as Ut
from ve_utils.usys import USys


class TestUSys:

    """USys unittest class."""

    @staticmethod
    def test_prints():
        """Test prints method."""
        print('\n Print tests : \n')
        USys.print_info('print_info')
        USys.print_success('print_success')
        USys.print_warning('print_warning')
        USys.print_danger('print_danger')
        USys.print_header('print_header')
        USys.print_purple('print_purple')
        USys.print_bold('print_bold')
        USys.print_underline('print_underline')

    @staticmethod
    def test_get_operating_system():
        """Test test_get_operating_system method."""
        assert Ut.is_str(USys.get_operating_system())

    @staticmethod
    def test_get_operating_system_type():
        """Test test_get_operating_system_type method."""
        assert Ut.is_tuple(USys.get_operating_system_type())

    @staticmethod
    def test_is_op_sys_type():
        """Test is_op_sys_type method."""
        assert USys.is_op_sys_type('unix') or USys.is_op_sys_type('win32')

    @staticmethod
    def test_is_op_sys():
        """Test is_op_sys method."""
        assert USys.is_op_sys('Linux') or USys.is_op_sys('MacOs') or USys.is_op_sys('Windows')

    @staticmethod
    def test_get_current_file_parent_parent_path():
        """Test is_op_sys method."""
        current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        assert Ut.is_str(USys.get_current_file_parent_parent_path(current_path))

    @staticmethod
    def test_get_current_file_parent_path():
        """Test get_current_file_parent_path method."""
        current_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        assert Ut.is_str(USys.get_current_file_parent_path(current_path))
