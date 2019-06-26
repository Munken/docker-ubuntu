#!/usr/bin/env python

from collections import namedtuple
from string import Template
import os
import sys

Distro = namedtuple("Distro", ["baseimage", "tag", "template"])
Distro.__new__.__defaults__ = (None,) * len(Distro._fields)

debian_template = Template(
"""FROM $dist:$tag

RUN sed -i -e "s/security./old-releases./" /etc/apt/sources.list
RUN sed -i -e "s/archive./old-releases./" /etc/apt/sources.list
"""    
)

distros = [
    Distro("ubuntu", ["zesty", "artful"], debian_template),
]


basedir = sys.argv[1] if len(sys.argv) == 2 else "."


for d in distros:
    i = d.baseimage
    for t in d.tag:
        path = "{}/{}".format(basedir,t)
        print path
        try:
            os.makedirs(path)
        except OSError:
            pass
        
        with open("{}/Dockerfile".format(path), "w") as f:
            s = d.template.substitute(dist=i, tag=t)
            f.write(s)
            
