#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import conf
import time
from datetime import datetime

# const
api = twitter.Api(
    consumer_key = conf.consumer_key,
    consumer_secret = conf.consumer_secret,
    access_token_key = conf.access_token_key,
    access_token_secret = conf.access_token_secret,
)

def tweet():
    content = datetime.now().isoformat()
    status = api.PostUpdate(content)

tweet()
