import time
print("press enter to start the timer,CTRL c to stop")
while True:
    try:
        input()
        starttime=time.time()
        print("Timer has started")
        while True:
            print("Time elapsed:",round(time.time()-starttime,0),"secs",end='\n')
            time.sleep(1)

    except KeyboardInterrupt:
            print("Timer has stopped")
            endtime=time.time()
            print("Totaltime:",round(endtime-starttime,2),'secs')
            
            break
        
        