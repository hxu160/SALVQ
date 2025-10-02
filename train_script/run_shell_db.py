import os

for lmbda in [0.002, 0.004, 0.008, 0.015, 0.025]:  
    for cuda, scene in enumerate(['playroom', 'drjohnson']):
        one_cmd = f'CUDA_VISIBLE_DEVICES={0} python train.py -s /home/hxu/data/db/{scene} --eval --lod 0 --voxel_size 0.005 --update_init_factor 16 --iterations 30_000 -m outputs/db/{scene}/{lmbda} --lmbda {lmbda}'
        os.system(one_cmd)
