import json
import threading
import time
from comment_bot import comment

keyword = "crypto"
message = "is bitcoin still worth trading? #crypto  "

with open("data.json", 'r') as f :
    auths = json.loads(f.read())

thread_list = list()
for i in range(len(auths)) : 
    user = auths[i]["userId"]
    psswrd = auths[i]["password"]
    
    t = threading.Thread(name='Test {}'.format(i), target=lambda: comment(user,psswrd,keyword,message))
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

