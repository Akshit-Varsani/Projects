import pandas as pd
from datetime import datetime

file = pd.ExcelFile('test.xlsx')
pd.read_excel(file, 0)

class Route:
    def __init__(self, file):
        self.file = file

    def route_name(self):
        names = self.file.sheet_names
        return list(names)

    def stop_lists(self, index1):
        sheet = pd.read_excel(self.file, index1)
        stops = sheet[sheet.columns[0]]
        return list(stops)

    def next_three(self, index1, index2):
        # read all respective timings
        sheet = pd.read_excel(self.file, index1)
        timings = list(sheet.iloc[index2])
        timings.pop(0)

        # get current time
        current_time = datetime.now().time()

        # Get next 3 timings
        upcoming_three = []
        options_available = len(timings)
        iterations = 0
        n = 0

        # run through each timing for the chosen route and stop
        for timing in timings:
            iterations = iterations + 1

            # check if the bus time is great than current time and have not found 3 timings
            if (timing >= current_time) or (n != 3):
                n = n + 1
                upcoming_three.append(timing)

            # if 3 timings not found then they must be times from early next day
            elif iterations == options_available:
                if n == 0:
                    upcoming_three.append(timings[0:3])
                    n = 3
                elif n == 1:
                    upcoming_three.append(timings[0:2])
                    n = 3
                elif n == 2:
                    upcoming_three.append(timings[0])
                    n = 3

        return upcoming_three


# test code
my = Route(file)
my.route_name()
my.stop_lists(1)
my.next_three(1,2)