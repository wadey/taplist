import json
import sys

from twitter import Twitter, OAuth

import settings

twitter = Twitter(
          auth=OAuth(
              settings.TOKEN,
              settings.TOKEN_KEY,
              settings.CON_SECRET,
              settings.CON_SECRET_KEY))

old = None
current = None

with open(sys.argv[1]) as f:
    old = set([e['name'] for e in json.load(f)])

with open(sys.argv[2]) as f:
    current = set([e['name'] for e in json.load(f)])

brewery = sys.argv[3]

if old and current:
    new = current - old

    if new:
        for beer in new:
            msg = "New beer at %s: %s" % (brewery, beer)
            twitter.statuses.update(status=msg)
            print msg
    else:
        print 'nothing new'
