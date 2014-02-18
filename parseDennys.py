#!/usr/bin/env python

import sys
from xml.dom.minidom import parse
dom = parse(sys.argv[1])
tags = ("uid", "address1", "address2", "city", "state", "country", "latitude", "longitude")
print ",".join(tags)
for poi in dom.getElementsByTagName("poi"):
    values = []
    for tag in tags:
        if len( poi.getElementsByTagName(tag)[0].childNodes ) == 1:
            values.append( poi.getElementsByTagName(tag)[0].firstChild.nodeValue )
        else:
            values.append("")
    print ",".join( map(lambda x: '"'+str(x)+'"', values) )