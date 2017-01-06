# im2wireframe
To produce a wireframe plot from a matrix of randoom values, with default or specified X and Y coordinates

```
import make_mesh as mm
import numpy as np

mm.im2wireframe(np.random.rand)

mm.im2wireframe(np.random.rand(4,2),np.array([1,3,5,11]),[2,12])

mm.im2wireframe(np.random.rand(4,2),y_pnts=[2,12])
```


# im2mesh
Returns the 3 structures required to produce a mesh for waterfall plots, wireframes and other contour like visualizations where you have a matrix and need the X,Y and Z vectors from it

```
import make_mesh as mm
import numpy as np

mm.in2mesh(np.random.rand(4,2))
```
