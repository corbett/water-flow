#Plot arrays

# User set parameters
res = int(45*2**5)
print("res = " + str(res))

# Path to memory location for arrays of a particular resolution
thisdir = "/home/handmer/Documents/Mars/water-flow/"

inputpath = thisdir + "res"+str(res)+"/"
#inputpath = thisdir + "res"+str(res)+"-clean/"

gratextents = [1,1]

import numpy as np
from matplotlib import pyplot as plt

subsample = 1

big_array = np.zeros([int(res*gratextents[0]/subsample),int(res*gratextents[1]/subsample)])

# Allocate graticule memory
# Mola, metric, depth, flowEW, flowNS, positive flow, negative flow, norm
graticule_space = np.zeros([res+4,res+4,9])

depth_moment_1 = 0
#total_heights = 0
total_water = 0

# loop over graticules
for latindex in range(gratextents[0]):
    for lonindex in range(gratextents[1]):
        # Load graticule
        graticule_space = np.load(inputpath+"/array"+str(1+latindex)+str(6+lonindex)+".npy")
        depth_moment_1 += np.sum((graticule_space[2:-2,2:-2,0])*graticule_space[2:-2,2:-2,1]*graticule_space[2:-2,2:-2,2])
        #total_heights += np.sum(graticule_space[2:-2,2:-2,0])
        total_water += np.sum(graticule_space[2:-2,2:-2,2])#*graticule_space[2:-2,2:-2,1])

        #plt.imshow(graticule_space[1:-1,1:-1,5])
        #plt.show()

        #graticule_space[2:-2,2:-2,0] = graticule_space[2:-2,2:-2,2]
        #graticule_space[2:-2,2:-2,0] = graticule_space[2:-2,2:-2,2]*graticule_space[2:-2,2:-2,1]
        #graticule_space[2:-2,2:-2,0] = ((0.25*graticule_space[1:-3,1:-3,5]
        #                                +0.25*graticule_space[2:-2,2:-2,5]
        #                                +0.25*graticule_space[1:-3,2:-2,5]
        #                                +0.25*graticule_space[2:-2,1:-3,5]
        #)*graticule_space[2:-2,2:-2,7])**0.2
        #graticule_space[2:-2,2:-2,0] /= (10+graticule_space[2:-2,2:-2,2])
        graticule_space[2:-2,2:-2,0] = (graticule_space[2:-2,2:-2,3]**2 + graticule_space[2:-2,2:-2,4]**2)**0.1
        #graticule_space[2:-2,2:-2,0] = graticule_space[2:-2,2:-2,5]
        big_array[int(res*latindex/subsample):int(res*(latindex+1)/subsample),
                  int(res*lonindex/subsample):int(res*(lonindex+1)/subsample)] = graticule_space[2:-2,2:-2,2]#(graticule_space[2:-2,2:-2,0]+8142)*graticule_space[2:-2,2:-2,1]
        #print([int(res*latindex/subsample),int(res*(latindex+1)/subsample)])

# average volume per pixel. Should be normalized to 1
#print(np.sum(big_array/(res*res*4*8))*np.pi/300)
#print(np.min(big_array))
#print(np.max(big_array))

#print(depth_moment_1/(32*res)**2)
print(total_water/(32*res**2))
print(depth_moment_1/total_water)

#print(np.min(big_array))
#print(np.max(big_array))

plt.figure(figsize = (20,40))
plt.imshow(big_array)
plt.show()

#plt.imshow(np.load(inputpath+"/test"+str(0)+str(0)+".npy")[:,:,2])
#plt.imshow(big_array[360:720+360,360:720+360])
#plt.show()

print(total_water)
#print(np.sum(np.load(inputpath+"/test"+str(0)+str(0)+".npy")[2:-2,2:-2,2]))

#print(np.load(inputpath+"/test"+str(3)+str(4)+".npy")[21:26,21:26,2])




#for latindex in range(gratextents[0]):
#    for lonindex in range(gratextents[1]):
#        print([latindex, lonindex, 4*np.sum(np.load(thisdir + "res"+str(res)+"/"+"/test"+str(latindex)+str(lonindex)+".npy")[2:-2,2:-2,2])/np.sum(np.load(thisdir + "res"+str(2*res)+"/"+"/test"+str(latindex)+str(lonindex)+".npy")[2:-2,2:-2,2])])
