import csv
from typing import Iterable, Any

def SaveToCSVDataset(file_name: str, elements: Iterable):
    # Set NewLine to Empty as using writerow function which adds newline itself
    with open(file_name, 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=',')
        count = 0
        for elem in elements:
            if elem is not None:
                wr.writerow(list(elem))
                print("Added ", count,elem.Path)
                count = count + 1

def ReadFromCSVDataset(file_name: str, result_type: Any) -> Iterable[Any]:
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
             if row is not None:
                 yield result_type(path=row[0], Hash=str(row[1]))
