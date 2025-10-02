import os

for lmbda in [0.002, 0.004, 0.008, 0.015, 0.025]: 
    for cuda, scene in enumerate(['truck', 'train']):
        one_cmd = f'CUDA_VISIBLE_DEVICES={0} python train.py -s /home/hxu/data/tandt/{scene} --eval --lod 0 --voxel_size 0.01 --update_init_factor 16 --iterations 30_000 -m outputs/tandt/{scene}/{lmbda} --lmbda {lmbda}'
        os.system(one_cmd)

#python train_script/run_shell_tnt.py
#python train_script/run_shell_tnt2.py
#python train_script/run_shell_tnt3.py
#python train_script/run_shell_tnt4.py