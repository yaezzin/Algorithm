from datetime import datetime

current_time_str = input()
start_time_str = input()

current_time = datetime.strptime(current_time_str, "%H:%M:%S")
start_time = datetime.strptime(start_time_str, "%H:%M:%S")
time_difference = start_time - current_time

hours, remainder = divmod(time_difference.seconds, 3600)
minutes, seconds = divmod(remainder, 60)
remaining_time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

print(remaining_time_str)