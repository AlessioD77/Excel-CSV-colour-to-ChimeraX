import numpy as np
import pandas as pd


#This script generates a pasteable ChimeraX command for coloring glycans according to
# color co-ordinates for the BG505 SOSIP.664 pdb from a .csv

#load csv file containing colours for each PNGS
filename = input('Enter a file name: ')
ab = pd.read_csv(filename)
print(ab)

def set_color(color_name, site, color):
    print(f'color {color_name} {color}')

sites = ab.columns

for i, site in enumerate(sites):
    A = 'N' + site[1:]
    color = ab[site].values[0]
    # i + 2 becuase chain ID usually starts above 0, with #1 usually representing the underlying protein
    set_color('#' + str(i+2), A, color)