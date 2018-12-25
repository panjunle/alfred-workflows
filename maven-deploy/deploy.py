#!/usr/bin/python
# encoding: utf-8

from workflow import Workflow3

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def main(wf):
    #获取所有参数
    acmd = wf.args[0]
    spmd = acmd.split(' ')
    arglen = 0
    for xx in spmd:
        if len(xx) > 0:
            arglen = arglen + 1
    #arglen = len(spmd)
    if arglen == 4:
        # 获取groupid
        groupid = spmd[0]
        # 获取artifactid
        artid = spmd[1]
        # 获取version
        ver = spmd[2]
        # 获取filepath
        fpath = spmd[3]
        dprel = 'mvn deploy:deploy-file -DgroupId=' + groupid + ' -DartifactId=' + artid + ' -Dversion=' + ver + ' -Dpackaging=jar -Dfile=' + fpath + ' -Durl=http://192.168.32.22:8081/nexus/content/repositories/releases -DrepositoryId=releases'
        dpsnp = 'mvn deploy:deploy-file -DgroupId=' + groupid + ' -DartifactId=' + artid + ' -Dversion=' + ver + ' -Dpackaging=jar -Dfile=' + fpath + ' -Durl=http://192.168.32.22:8081/nexus/content/repositories/snapshots -DrepositoryId=snapshots'
        # Parse the JSON returned by pinboard and extract the ganks
        wf.add_item(subtitle='copy deploy releases cmd', title='http://192.168.32.22:8081/nexus/content/repositories/releases', arg=dprel, icon='release.png' ,valid=True)
        wf.add_item(subtitle='copy deploy snapshots cmd', title='http://192.168.32.22:8081/nexus/content/repositories/snapshots', arg=dpsnp, icon='snapshot.png' ,valid=True)
        # Send output to Alfred. You can only call this once.
        # Well, you *can* call it multiple times, but Alfred won't be listening
        # any more...
    elif arglen == 1:
        wf.add_item(subtitle='', title='input ArtifactId next,separated by space', arg='', valid=True)
    elif arglen == 2:
        wf.add_item(subtitle='', title='input Version next,separated by space', arg='', valid=True)
    elif arglen == 3:
        wf.add_item(subtitle='', title='input Jar-File-Path next,separated by space', arg='', valid=True)
    else:
        wf.add_item(subtitle='error', title='input args size must eq 4,now is ' + str(arglen), arg='', valid=True)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))