#!/usr/bin/python
# encoding: utf-8

from workflow import Workflow3

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def main(wf):
    # 获取查询关键字
    query = wf.args[0]
    # upcase
    supper = query.upper()
    # lowercase
    slower = query.lower()
    # Parse the JSON returned by pinboard and extract the ganks
    wf.add_item(subtitle='Upper Case', title=supper, arg=supper, valid=True, icon='upcase.gif')
    wf.add_item(subtitle='Lower Case', title=slower, arg=slower, valid=True, icon='upcase.gif')
    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but Alfred won't be listening
    # any more...
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))