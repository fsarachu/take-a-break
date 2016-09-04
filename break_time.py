import time
import webbrowser

total_breaks = 3
break_count = 0

print "Program started at " + time.ctime()

while break_count < total_breaks:
    time.sleep(5)
    print "It's time to give it a break! " + time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    break_count += 1
