import json
import sys

from twitter import Twitter, OAuth

try:
    import settings
except:
    settings = None

twitter = None
if settings:
    twitter = Twitter(
              auth=OAuth(
                  settings.TOKEN,
                  settings.TOKEN_KEY,
                  settings.CON_SECRET,
                  settings.CON_SECRET_KEY))

def load(name):
    with open(name) as f:
        return set([e['name'] for e in json.load(f)])

old = load(sys.argv[1])
current = load(sys.argv[2])
brewery = sys.argv[3]

if not old:
    print "error, no last data"
elif not current:
    print "error, no current data"
else:
    new = current - old

    if new:
        for beer in new:
            msg = "New beer at %s: %s" % (brewery, beer)
            if twitter:
                twitter.statuses.update(status=msg)
            print msg
    else:
        print 'nothing new'
