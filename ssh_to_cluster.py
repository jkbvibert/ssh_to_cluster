#uses DBVis folder structure as an XML file to know clusters, which load balancer which is manually broken out into component servers here
while True:
    import xml.etree.ElementTree as etree
    import subprocess, random, sys, os
    tree = etree.parse('%s\\.dbvis\\config70\\dbvis.xml' % os.environ['USERPROFILE'])
    root = tree.getroot()
    server_arry = []
    print("SSH to which cluster?")
    def print_dbs():
        index = 1
        for each in root[3]:
            print("{0}.\t{1} ".format(index,each[0].text))
            server_arry.append(((each[1].text).split(':',3)[2])[2:])
            index += 1
        print("E.\tExit")
        index = 1
        return
    print_dbs()
    choice = input('Enter your choice: ')
    if str(choice).lower() == 'e':
            sys.exit(0)
    choice = int(choice)
    if choice <= len(root[3]) and choice > 0:
        server = server_arry[choice-1]
        if server == 'load_balancer1':
            server = random.choice(['server1','server2','server3'])
        elif server == 'load_balancer2':
            server = random.choice(['server1','server2','server3'])
        elif server == 'load_balancer4':
            server = random.choice(['server1','server2','server3'])
        p = subprocess.Popen('cmd.exe /c %s\\Desktop\\putty.exe -ssh vibertj@%s' % (os.environ['USERPROFILE'], server)) #USERPROFILE is a premade environment variable
        break
    else:
        print("Invalid input. Restarting...")
        continue
