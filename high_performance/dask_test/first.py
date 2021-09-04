import numpy as np
import dask.array as da

arr1 = np.random.random(10)
print(arr1)

dask_arr1 = da.random.random(10, chunks=3)
print(dask_arr1)
print(dask_arr1.compute())
print(dask_arr1.chunks)


dask_arr2 = da.from_array(arr1, chunks=2)
print(dask_arr2.compute())

dask_arr3 = da.random.random(1000000, chunks=100)
dask_arr4 = da.random.random(1000000, chunks=100)

dask_arr5 = da.add(dask_arr3, dask_arr4)

#print(dask_arr5.compute())
print(dask_arr5.chunks)
