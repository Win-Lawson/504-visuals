from vedo import *
import scipy
import numpy as np
settings.default_backend='vtk'
import sys

last=-1

def func(evt):
   print('click')
   if not evt.object:
      return
   clicked = evt.picked3d
   id = point_cloud.closest_point(clicked,return_cell_id=True)
   
   n = point_cloud.npoints
   rgba = [255, 0, 0, 255]   # r, g, b, alpha (0–255)

   colors = np.full((n, 4), rgba, dtype=np.uint8)
   colors[id]=[0,0,255,255]
   global last 
   last = id
   
   point_cloud.cellcolors=colors

   print('clicked ', id)

def animate_rotate(evt):
   print('trigger rotate')
   for i in range(100):
      point_cloud.rotate(rad=True, angle=np.pi/100,axis=point_cloud.points[last])
      plt.render()

plt = Plotter(interactive=True)
pts = np.random.randn(10, 3)
point_cloud = Points(Sphere().vertices,r=20,c=[0,255,0])
test = point_cloud.points
cctest = point_cloud.cellcolors
#test[0] = [5,5,5]
#cctest[0] = [255,0,0,255]
point_cloud.points = test
#point_cloud.cellcolors = cctest
plt.add(point_cloud)

plt.add_callback('LeftButtonPress', func)
plt.add_callback('RightButtonPress',animate_rotate)


plt.show(axes=1, interactive=True)
plt.close()
print(last)
lastpoint = point_cloud.points[last]
print(lastpoint)