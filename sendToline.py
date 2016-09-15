from line import LineClient, LineGroup, LineContact

try:
    #client = LineClient("ID", "PASSWORD")
    client = LineClient(authToken="AUTHENTOKEN")
except:
    print "Login Failed"

group = client.getGroupByName('Web Capture Monitor')
#group.sendMessage("Test Line Bot")
group.sendImage("/tmp/webcapture.png")

#print client.groups
