from skimage import img_as_bool, io, color, morphology
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# You can run these functions in an interactive session
# Don't forget to use raw string if literals like "\" are necessary in the path

# Make a figure of original and outputs
def get_centerline_figure(img):
    image = img_as_bool(color.rgb2gray(io.imread(img)))
    out_skeleton = morphology.skeletonize(image)
    out_medial = morphology.medial_axis(image)

    fig, axs = plt.subplots(1, 3)
    axs[0].imshow(image, cmap='gray', interpolation='nearest')
    axs[1].imshow(out_skeleton, cmap='gray', interpolation='nearest')
    axs[2].imshow(out_medial, cmap='gray', interpolation='nearest')

    plt.tight_layout()
    
    fig.savefig('fig.png', dpi = 300, figsize = (10, 8))

# Process function
def get_centerline_data(img, method):
    image = img_as_bool(color.rgb2gray(io.imread(img)))
    
    medial_axis, medial_axis_distance = morphology.medial_axis(image, return_distance=True)
    skeleton = morphology.skeletonize(image)

    skeleton_distance = medial_axis_distance * skeleton

    nonzero = skeleton_distance.nonzero()

    df_coords = pd.DataFrame(data = np.transpose(nonzero), columns = ["y", "x"])
    df_distance = pd.DataFrame(data = skeleton_distance[nonzero])

    combined = pd.concat([df_coords, df_distance], axis = 1)

    return combined

# The scaling on the last image ('cross.jpg') makes the width of the rectangle 24.3 px. The calculated distance is ~12