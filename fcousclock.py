import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('Remaining: ' + timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print('Time is up! Focus for {} minutes accomplished.'.format(minutes))

# Example usage - set timer for 25 minutes:
focus_timer(25)
