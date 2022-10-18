#!/usr/bin/env python3
from build.lib import dev_aberto
from dev_aberto.dev_aberto import hello
from babel import dates
from datetime import datetime
import gettext
gettext.install('hello', localedir='locale') 

if __name__ == '__main__':
    date, name = hello()
    format_data = "%Y-%m-%dT%H:%M:%SZ"
    date = datetime.strptime(date, format_data)
    
    last_commit_ = _('Last commit in')
    by_ = _('by')
    print(last_commit_, dates.format_date(date, 'full'), by_, name)
