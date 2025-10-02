import os

#for lmbda in [0.015, 0.025]:  # Optionally, you can try: 0.003, 0.002, 0.001, 0.0005
for lmbda in [0.002, 0.004, 0.008, 0.015, 0.025]:
    for cuda, scene in enumerate(['bicycle', 'garden', 'stump', 'room', 'counter', 'kitchen', 'bonsai', 'flowers', 'treehill']):
        one_cmd = f'CUDA_VISIBLE_DEVICES={0} python train.py -s /home/hxu/data/mip360/{scene} --eval --lod 0 --voxel_size 0.001 --update_init_factor 16 --iterations 30_000 -m outputs/mipnerf360/{scene}/{lmbda} --lmbda {lmbda}'
        os.system(one_cmd)

