# -*- coding: utf-8 -*-

"""
    pyeez.template
    ~~~~~~~~~~~~~~
    
    This module implements pyeez template class
    
    :copyright: (c) 2015 by Mehdy Khoshnoody.
    :license: GPLv2, see LICENSE for more details.
"""

import sys


class Template(object):
    """
        The Template object implements a template string to be showed and
        updated inside application windows.

    :param template_str: The string to be used a template
    :type template_str: str
    """

    def __init__(self, template_str):
        self.template_str = template_str

    def update(self, *args, **kwargs):
        """
            Updates the template and refresh the screen.
        :param args:
        :param kwargs:
        :return:
        """
        final = self.template_str.format(*args, **kwargs)
        sys.stdout.write(final)
        sys.stdout.flush()
