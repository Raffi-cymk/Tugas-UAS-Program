class StudentView:
    @staticmethod
    def display_table(data):
        table = PrettyTable()
        table.field_names = ["No", "Name", "Score"]
        for i, student in enumerate(data, start=1):
            table.add_row([i, student["name"], student["score"]])
        print(table)

    @staticmethod
    def display_message(message):
        print(message)