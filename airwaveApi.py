import requests
import xml.etree.ElementTree as ET

data = 'credential_0=xxxxx&credential_1=xxxxx&destination=/&login=Log In'
headers={'Content-Type': 'application/x-www-form-urlencoded','Cache-Control':'no-cache'}

ampsession = requests.Session()
loginamp = ampsession.post('https://xxx.xx.xx.xxx/LOGIN',headers=headers, data=data, verify=False)

result=ampsession.get('https://xxx.xx.xx.xxx/ap_list.xml',headers=headers, verify=False)

aplist = result.content

tree=ET.fromstring(aplist)

for i in tree.iter('ap'):
    id=i.attrib
    
    if i.find('lan_ip')!=None:
        ip=i.find('lan_ip').text
    else: ip=" "    
        
    if i.find('lan_mac')!=None:
        mac=i.find('lan_mac').text
    else: mac=" "
    
    if i.find('model')!=None:
        model=i.find('model').text
    else: model=" "
    
    if i.find('name')!=None:
        name=i.find('name').text
    else: name=" "

    if i.find('operating_mode')!=None:
        op_mode=i.find('operating_mode').text
    else: op_mode=" "
        
    print "\n"+"*"*30
    print "#### Details of AP :{}".format(id).ljust(30)
    print "*"*30
    print "#### AP Name       :{}".format(name).ljust(30)
    print "#### MAC Address   :{}".format(mac).ljust(30)
    print "#### IP Address    :{}".format(ip).ljust(30)
    print "#### Model         :{}".format(model).ljust(30)
    print "#### Operating Mode:{}".format(op_mode).ljust(30)
    print "*" * 30