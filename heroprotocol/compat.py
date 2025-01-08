#!/usr/bin/env python
#
# Copyright 2015-2020 Blizzard Entertainment. Subject to the MIT license.
# See the included LICENSE file for more information.
#

import json
import six


def defaultJsonHandler(obj):
    try:
        if type( obj ) is bytes:
            return obj.decode('utf-8')
        else:
            return obj
    except:
        if type( obj ) is bytes:
            return obj.hex()
        else:
            return None

def json_dumps(obj, encoding):
    if six.PY3:
        return json.dumps(obj, default=defaultJsonHandler, ensure_ascii=True)
    else:
        return json.dumps(obj, default=defaultJsonHandler, encoding=encoding)
