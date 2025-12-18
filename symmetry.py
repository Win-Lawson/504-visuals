from vedo import *
import numpy as np
import time
settings.default_backend='vtk'

#Definitions of shapes
shapes = [IcoSphere(alpha=1),Cube(alpha=.5)]
shape = 1 #setting to select shape
doTex = True #setting for whether or not to apply a texture to the mesh. I couldn't quite get this to work, so doesn't look right. This still demonstrates the symmetry operations


#Definition of cloud
cloud = Points(shapes[shape].vertices, r=10,c=[255,0,0])
if doTex:
    solid = shapes[shape].texture('NewTennisBallColor.jpg',interpolate=False, repeat=True,edge_clamp=False)
npts = cloud.npoints
id_s = 0
pos_s = cloud.points[id_s]
reset_colors = cloud.cellcolors




#Transformation Settings
nfold = 1

#annimation setting

t_total = 2
nframes = t_total*60
dt = t_total/nframes

def rot_s_animate(a,b):



    kwargs = dict(
        rad=True,
        angle=2 * np.pi / nfold / nframes,
        axis=pos_s,
    )


    for frame in range(nframes):
        
        cloud.rotate(**kwargs)
        solid.rotate(**kwargs)
        plt.render()
        time.sleep(dt)

def select(evt):
    if not evt.object:
        return
    global id_s
    global pos_s
    id_s = cloud.closest_point(evt.picked3d,return_cell_id=True)
    pos_s = cloud.points[id_s]

    cloud.cellcolors=reset_colors
    cloud.cellcolors[id_s]=[0,255,0,255]




plt = Plotter(axes=1)
folds = [1,2,3,4,6]
fi=0
def set_fold(a,b):
    global fi
    global nfold
    fi+=1
    fi%=5
    nfold=folds[fi]
fold_setting = ButtonWidget(
    set_fold,
    states=['N_fold = 1','N_fold = 2','N_fold = 3','N_fold = 4','N_fold = 6'],
    c = ['white','white','white','white','white'],
    bc= ['black','black','black','black','black'],
    size=200,
    plotter=plt,
)
fold_setting.pos([0,0]).enable()
rotateccw = ButtonWidget(
    rot_s_animate,
    states=['N_fold rot on selected point'],
    c = ['white'],
    bc = ['black'],
    size=600,
    plotter = plt,

)
rotateccw.pos([1,0]).enable()



plt.add(cloud)
plt.add(solid)
plt.add_callback('LeftButtonPress', select)
plt.show()
plt.close()


