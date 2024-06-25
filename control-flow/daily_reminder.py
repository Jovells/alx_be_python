# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify the reminder if the task is time-bound
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print("Reminder:", reminder)

