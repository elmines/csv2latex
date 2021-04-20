import sys
import csv

end = " \\\\\n"
filename = sys.argv[1]
with open(filename, "r", encoding="utf-8") as r:
    reader = csv.DictReader(r)
    fieldnames = reader.fieldnames
    print( " & ".join(fieldnames), end=end)
    for r in reader:
        print(" & ".join(r[f] for f in fieldnames), end=end)

