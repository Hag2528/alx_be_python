task=input("Enter your task:") 
priority=input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        print(f"'{task}'{priority} is.")
    case "medium":
        print(f"'{task}'{priority}")
    case "low":
        if time_bound=="yes":
         print(f"'{task}'{priority}")

