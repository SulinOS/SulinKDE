#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import kde
from inary.actionsapi import shelltools

def setup():
    shelltools.system("sed -i -e '/find_package.*QGpgme/d' CMakeLists.txt")
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

