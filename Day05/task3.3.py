meetings = [
    ["Monday", " 3:30 PM", "Joe", "Sam"] ,
    ["Monday", " 4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"] ,
    ["Tuesday", "9:30 AM", "Joe", "Bob"]
]

def getMeetings(name: str) -> None:
    days = {}
    for meet in meetings:
        if name in meet:
            days[meet[0]] = days.get(meet[0], []) + [meet[1]]
    for day, hours in days.items():
        print(day + "'s meetings :")
        print(*hours, sep=", ")

getMeetings("Joe")