#%% This is the original script
#from pyraabe import centerline

#cylinder_centerline = centerline.read(r".\cylinder_open_centerline.vtp")

# The modified script starts below

#%% Imports
import pyraabe
import os

#%% Get the [x,y,z] and radius
# Set the path to the file for which centerlines should be calculated
infile = r".\cylinder_open.stl"

# Set the filenames for output
filename_prefix = os.path.splitext(infile)[0]
centerline_path = os.path.join(filename_prefix + '_centerline.vtp')
data_path = os.path.join(filename_prefix + '_coords.csv')

# Extract centerline, unless it already exists (if you need to recalculate, change the name of the original)
if not os.path.exists(centerline_path):
    pyraabe.centerline.compute(infile, centerline_path)
else:
    print('{} already exists. Skipping centerline calculation.'.format(centerline_path))

# Get centerline data and write to csv
new_centerline = pyraabe.centerline.read(centerline_path)
data = pyraabe.centerline.to_dataframe(new_centerline)
data.to_csv(data_path)
# %%
