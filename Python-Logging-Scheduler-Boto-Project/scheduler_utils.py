import shutil
import logging
import schedule
import time

logging.basicConfig(filename='system_Logs.txt',level=logging.INFO,format ='%(asctime)s %(message)s')

def check_disk():
    disk=shutil.disk_usage("/")
    per_used=(disk.total - disk.free)/disk.total * 100
    
    if per_used > 75:
        logging.warning("Disk Full !")
    elif per_used > 95:
        logging.critical("Critical Disk Full !")
    else:
        logging.info("Disk is about to fill")   
                
check_disk()  
        
schedule.every(10).seconds.do(check_disk)
while True:
    schedule.run_pending()
    time.sleep(1)
    