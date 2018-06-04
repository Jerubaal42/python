import subprocess
for ping in range(1,255):
    address="*.*.*."+str(ping)
    res=subprocess.call(['ping','-c','3',address],stdout=subprocess.PIPE)
    if res==0:
        print(address,'Successful')
