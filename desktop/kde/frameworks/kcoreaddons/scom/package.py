 # -*- coding: utf-8 -*-

from inary.version import Version

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/update-mime-database /usr/share/mime > /dev/null")


