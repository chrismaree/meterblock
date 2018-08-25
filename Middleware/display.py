import sys
import os
import time
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Power Consumed(W)", "Elapsed Time(s)", "Energy Consumed (mWh)", "Wallet Balance (uKraG)","isConsuming"]

def addRow(row):
    table.add_row(row)

def displayTable():
    os.system('clear')
    print(table)
