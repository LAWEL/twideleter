#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import conf
import time
from datetime import datetime
from datetime import timedelta

# const
api = twitter.Api(
    consumer_key = conf.consumer_key,
    consumer_secret = conf.consumer_secret,
    access_token_key = conf.access_token_key,
    access_token_secret = conf.access_token_secret,
)

t = datetime.now() + timedelta(weeks=-4)
ti = int(time.mktime(t.timetuple()))
max_id = -1
while True:
    status = twitter.Status
    if max_id == -1:
        status = api.GetUserTimeline(count=200)
    else:
        status = api.GetUserTimeline(count=200, max_id=max_id)
        pass
    status.reverse()
    if len(status) == 0:
        break
    for s in status:
        if ti < s.created_at_in_seconds:
            max_id = s.id - 1
            print("max_id = " + str(max_id) + " at " + s.created_at)
            break
        api.DestroyStatus(s.id)
        print("destroied tweet: " + s.text + " at " + s.created_at)
        pass
    pass
