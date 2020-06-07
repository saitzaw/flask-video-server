# automatically run the vod or channel accroding to schedule 
# this program need cron job to push every 5 second 

import schedule 
import time 

def job(): 
  # to do here 
  pass 

while True: 
  schedule.run_pending() 
  time.sleep(1) 
