
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += "."
    case "medium":
        reminder_message = f"Reminder: '{task}' is a medium priority task."
        if time_bound == "yes":
            reminder_message += " Please try to complete it soon!"
        else:
            reminder_message += " You can do this when you have some time."
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task."
        if time_bound == "yes":
            reminder_message += " However, it still requires attention today."
        else:
            reminder_message += " Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority level entered."

print(reminder_message)

print("Well done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")
