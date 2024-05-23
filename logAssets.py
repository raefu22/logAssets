import tkinter as tk
from tkinter import filedialog
import csv
from datetime import date

filetypes = (
    ('Text files', '*.zip'),
    ('All files', '*.*'),
)

# open-file dialog
root = tk.Tk()
files = tk.filedialog.askopenfilenames(
    title='Select a file:',
    filetypes=filetypes,
)
root.destroy()
filepaths = list(files)
filenames = []
for filepath in filepaths:
    filename = filepath.split('/')[-1].split('.')[0]
    filenames.append(filename)

rows = []
today = date.today()
for name in filenames:
    rows.append([name, today])

#open file
with open(r'E:\python\importedToUnrealLog.csv', 'a', newline='') as csvfile:
    fieldnames = ['Filename','Date Imported to Unreal']
    csvwriter = csv.writer(csvfile)
 
    # writing the fields
    csvwriter.writerow(fieldnames)
    csvwriter.writerows(rows)
