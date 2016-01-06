#!/usr/bin/python
# -*- coding: utf-8 -*-

import twitter
import conf
import time
from datetime import datetime
from datetime import timedelta

def delete_tweets(api):
    period = int(time.mktime((datetime.now() + timedelta(weeks=-4)).timetuple()))
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
            if period < s.created_at_in_seconds:
                max_id = s.id - 1
                break
            api.DestroyStatus(s.id)
            print('destroied tweet: %s at %s' % (s.text, s.created_at))
            pass
        pass
    pass

def main():
    api = twitter.Api(
        consumer_key = conf.consumer_key,
        consumer_secret = conf.consumer_secret,
        access_token_key = conf.access_token_key,
        access_token_secret = conf.access_token_secret,
    )

    delete_tweets(api)
    pass

if __name__ == '__main__':
    main()
    pass
