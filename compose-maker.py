#! /usr/bin/env python3
# Generate docker-compose.yml files for patroni

import yaml, shutil, os
from string import Template

yamlfile = './compose-maker.yaml'
templatefile = 'docker-compose-template.yml'
installfile = 'distribute-config.sh'

dist = open(installfile, "w")
print("#! /bin/sh \n# do not edit: generated!", file = dist)

t = Template(open(templatefile).read())

d = yaml.load(open(yamlfile).read(), Loader=yaml.loader.SafeLoader)
 
for serverrecord in d['server']:
  s = serverrecord['name']
  ip = serverrecord['ip']
  try:
    os.mkdir("hosts/%s" % s)
  except:
    print("Directory hosts/%s already there" % s)
  compose = t.substitute(server1 = d['server'][0]['name'], server1ip = d['server'][0]['ip'],
                     server2 = d['server'][1]['name'], server2ip = d['server'][1]['ip'],
                     server3 = d['server'][2]['name'], server3ip = d['server'][2]['ip'],
                     thisserver = s,
                     thisip = ip)
  open("hosts/%s/docker-compose.yaml" % s, "w").write(compose)
  shutil.copyfile(src = 'patroni.env', dst = "hosts/%s/patroni.env" % s)
  print("ssh root@%s mkdir -p /opt/patroni" % s, file = dist)
  print("scp hosts/%s/* root@%s:/opt/patroni/" % (s,s), file = dist)
  print('ssh root@%s "mkdir -p /opt/patroni/pg-data; chown 999:999 /opt/patroni/pg-data; chmod 750 /opt/patroni/pg-data; chcon -Rt svirt_sandbox_file_t /opt/patroni/pg-data"' % s, file = dist)
  print('ssh root@%s "mkdir -p /opt/patroni/etcd-data; chown 999:999 /opt/patroni/etcd-data; chmod 750 /opt/patroni/etcd-data; chcon -Rt svirt_sandbox_file_t /opt/patroni/etcd-data"' % s, file = dist)
  
dist.close()