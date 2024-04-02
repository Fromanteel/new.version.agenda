class DayAgenda:
    def __init__(self):
        self.days = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }

    def add_task(self, day, task):
        if day in self.days:
            self.days[day].append(task)
            print("Task added successfully!")
        else:
            print("Invalid day.")

    def view_tasks(self, day):
        if day in self.days:
            tasks = self.days[day]
            if tasks:
                print(f"Tasks for {day}:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print(f"No tasks found for {day}.")
        else:
            print("Invalid day.")

    def delete_task(self, day, index):
        if day in self.days:
            try:
                del self.days[day][index]
                print("Task deleted successfully!")
            except IndexError:
                print("Invalid task index.")
        else:
            print("Invalid day.")

    def clear_agenda(self):
        for day in self.days:
            self.days[day] = []
        print("Agenda cleared successfully!")

    def view_week_tasks(self):
        print("Week's Agenda:")
        for day, tasks in self.days.items():
            if tasks:
                print(f"{day}:")
                for task in tasks:
                    print(f"- {task}")
            else:
                print(f"{day}: No tasks")


def main():
    agenda = DayAgenda()
    while True:
        print("\n7-Day Agenda System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. View Week's Tasks")
        print("5. Clear Whole Agenda")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            day = input("Enter the day of the week: ").capitalize()
            task = input("Enter the task: ")
            agenda.add_task(day, task)
        elif choice == '2':
            day = input("Enter the day of the week: ").capitalize()
            agenda.view_tasks(day)
        elif choice == '3':
            day = input("Enter the day of the week: ").capitalize()
            index = int(input("Enter the index of the task to delete: ")) - 1
            agenda.delete_task(day, index)
        elif choice == '4':
            agenda.view_week_tasks()
        elif choice == '5':
            agenda.clear_agenda()
        elif choice == '6':
            print("Exiting agenda system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
