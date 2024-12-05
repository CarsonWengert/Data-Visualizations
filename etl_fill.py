import numpy as np
import matplotlib.pyplot as plt

import matplotlib.patches as mpatches
import matplotlib.path as mpath

def make_circle_arc(r:int, start_radians:int=0, end_radians:int=2*np.pi) -> np.ndarray:
    t = np.arange(start_radians, end_radians, 0.01)
    t = t.reshape((len(t), 1)) # do this to stack them later into x, y points!
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.hstack((x, y))
    
def make_dee(inner_r, outer_r, start_radians:int=0, end_radians:int=2*np.pi, hshift=0) -> mpath.Path:
    """
    1. Draw straight line from the inner circle to the outer circle
    2. Draw the outer circle arc
    3. Draw straight line from the outer circle to the inner circle
    4. Draw the inner circle arc
    """
    # 1. Draw straight line from the inner circle to the outer circle
    start_line_vertices = np.array([
        [inner_r*np.cos(start_radians), inner_r*np.sin(start_radians)],
        [outer_r*np.cos(start_radians), outer_r*np.sin(start_radians)]
    ])
    # 2. Draw the outer circle arc
    outside_circle_vertices = make_circle_arc(outer_r, start_radians, end_radians)
    # 3. Draw straight line from the outer circle to the inner circle
    end_line_vertices = np.array([
        [inner_r*np.cos(end_radians), inner_r*np.sin(end_radians)],
        [outer_r*np.cos(end_radians), outer_r*np.sin(end_radians)]
    ])
    # 4. Draw the inner circle arc
    inside_circle_vertices = make_circle_arc(inner_r, start_radians, end_radians)

    codes = np.ones(
        len(inside_circle_vertices)+2, dtype=mpath.Path.code_type
    ) * mpath.Path.LINETO
    codes[0] = mpath.Path.MOVETO

    # Concatenate all the paths together
    vertices = np.concatenate((
        start_line_vertices,
        outside_circle_vertices, 
        end_line_vertices[::-1], 
        inside_circle_vertices[::-1]
    ))
    vertices[:, 0] += hshift

    # The codes will be all "LINETO" commands, except for "MOVETO"s at the beginning of each subpath
    all_codes = np.concatenate((codes, codes))
    
    return mpath.Path(vertices, all_codes)

fig, ax = plt.subplots(figsize=(8, 8))

spacing = 0.3
ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi/2, 3*np.pi/2, -spacing/2), facecolor='white'))
ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, -np.pi/2, np.pi/2, spacing/2), facecolor='white'))

fillfraclist = [[0.88, 'cyan'], [0.625, 'teal'], [0.125, 'blue']] #necessarily decreasing
fillstyle = 3
for i in fillfraclist:
    if fillstyle == 1:
        #fill symmetric from bottom
        ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi/2 + (1-i[0]) * np.pi, 3*np.pi/2, -spacing/2), facecolor=i[1]))
        ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, -np.pi/2, -np.pi/2 + i[0] * np.pi, spacing/2), facecolor=i[1]))
    elif fillstyle == 2:
        #fill clockwise from left
        if i[0] <= 0.25:
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi - i[0] * 2 * np.pi, np.pi, -spacing / 2), facecolor=i[1]))
        elif i[0] > 0.25 and i[0] <= 0.75:
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi - i[0] * 2 * np.pi, np.pi / 2, spacing / 2), facecolor=i[1]))
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi / 2, np.pi, -spacing / 2), facecolor=i[1]))
        elif i[0] > 0.75:
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi - i[0] * 2 * np.pi, -np.pi / 2, -spacing / 2), facecolor=i[1]))
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, -np.pi / 2, np.pi / 2, spacing / 2), facecolor=i[1]))
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi / 2, np.pi, -spacing / 2), facecolor=i[1]))
    elif fillstyle == 3:
        #fill clockwise from bottom    
        if i[0] <= 0.5:
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, 3 * np.pi / 2 - i[0] * 2 * np.pi, 3 * np.pi / 2, -spacing / 2), facecolor=i[1]))
        elif i[0] > 0.5:
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, 3 * np.pi / 2 - i[0] * 2 * np.pi, np.pi / 2, spacing / 2), facecolor=i[1]))
            ax.add_patch(mpatches.PathPatch(make_dee(0.75, 2.0, np.pi / 2, 3 * np.pi / 2, -spacing / 2), facecolor=i[1]))


ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect(1.0)
#ax.axvline(0, color='purple', lw=2)
#ax.axhline(0, color='purple', lw=2)
plt.axis('off')
plt.show()