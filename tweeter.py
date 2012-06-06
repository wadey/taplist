import time
import json

from twitter import Twitter, OAuth
import beanstalkc

import settings

beanstalk = beanstalkc.Connection(host='localhost', port=11300)
beanstalk.watch('twitter')

twitter = Twitter(
          auth=OAuth(
              settings.TOKEN,
              settings.TOKEN_KEY,
              settings.CON_SECRET,
              settings.CON_SECRET_KEY))

while True:
    job = beanstalk.reserve()
    try:
        body = json.loads(job.body)
        msg = body['msg']

        twitter.statuses.update(status=msg)
        job.delete()
        job = None
        print "%s: %s" % (time.time(), repr(msg))
        time.sleep(5)
    except Exception as e:
        print e
        if job is not None:
            job.release()
