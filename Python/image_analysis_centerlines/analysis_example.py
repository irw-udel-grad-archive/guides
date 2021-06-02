from skimage import img_as_bool, io, color, morphology
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Testing process
# Import images
one = img_as_bool(color.rgb2gray(io.imread('1.jpg')))
cross = img_as_bool(color.rgb2gray(io.imread('cross.jpg')))
grid = img_as_bool(color.rgb2gray(io.imread('grid.jpg')))

# Get skeleton
one_skel = morphology.skeletonize(one)
cross_skel = morphology.skeletonize(cross)
grid_skel = morphology.skeletonize(grid)

# Get medial axis
one_med, one_med_distance = morphology.medial_axis(one, return_distance=True)
cross_med, cross_med_distance = morphology.medial_axis(cross, return_distance=True)
grid_med, grid_med_distance = morphology.medial_axis(grid, return_distance=True)

# Get skeleton distance
one_skel_distance = one_med_distance*one_skel

# Data processing for "1.jpg"
one_skel_nonzero = one_skel_distance.nonzero()
trans = np.transpose(one_skel_nonzero)

df_coords = pd.DataFrame(data = trans, columns = ["y", "x"])
df_dist = pd.DataFrame(data = one_skel_distance[one_skel_nonzero])

combined = pd.concat([df_coords, df_dist], axis=1)