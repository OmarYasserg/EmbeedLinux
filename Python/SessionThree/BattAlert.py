from pynotifier  import Notification
from plyer import notification

import psutil
battery = psutil.sensors_battery()
percentage = battery.percent
print(percentage)
message = "Battery is" + str(percentage) +"%"

notification = Notification(title="Battery percentage=", message = message,duration = 10)




# toaster = ToastNotifier()
# toaster.show_toast("Battery Status", message, duration=10)