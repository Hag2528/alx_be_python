# Get task details
task = input("Enter a single task: ")
priority = input("Enter priority (high, medium, low): ")
time_bound = input("Is this task time-bound (yes/no): ")

# Process task based on priority and time sensitivity
#reminder_message = ""
match priority:
  case "high":
    if time_bound == "yes":
      print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    if time_bound=="no":
      print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

    #reminder_message = "'High Priority Task:'" + task
  case "medium":
      if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
      if time_bound=="no":
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
  case "low":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    if time_bound=="no":
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
  case _:
    print("Invalid priority level.choosse the correct one.")
 