#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pepkobot Copyright © 2018 Il'ya Marshal Semyonov
# License: https://www.gnu.org/licenses/gpl-3.0.en.html
import os


telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN')

DB = {
    'host': os.environ.get('ec2-34-192-30-15.compute-1.amazonaws.com'),
    'port': int(os.environ.get('5432')),
    'user': os.environ.get('bbhgpvqaiehmtx'),
    'password': os.environ.get('5615c25deae22f2bc3c1d70b0f42c42a678be0baf89e8b1197323ac1699f660f'),
    'db': os.environ.get('d7ksl4qe7dm863'),
    'charset': 'utf8mb4'
}
