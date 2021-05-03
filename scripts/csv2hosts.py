import csv
import yaml

csv_file = open('scripts/data.csv')
rd = csv.DictReader(csv_file)

hosts = []
for host_data in rd:
  host_vars = 'host_vars/' + host_data['hostname'] + '.yml'
  hosts.append( host_data['hostname'] )
  with open(host_vars,'w+') as host_yaml:
    host_yaml.write(yaml.dump(host_data,explicit_start=True,default_flow_style=False))

# now write the 'hosts' file

#with open('hosts','w+') as hosts_file:
#  for h in hosts: hosts_file.write(h+'\n')
