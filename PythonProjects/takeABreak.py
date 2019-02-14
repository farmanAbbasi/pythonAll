import webbrowser
import time
# open web browser every 30 minute
current_time = time.ctime() # get current time
print ("start time = " + current_time)
i = 0
while(i<5):
    time.sleep(0.5*60*60)
    url="https://www.youtube.com/watch?v=kxYkhmbw2zM" 
    webbrowser.open(url)
    i=i+1
