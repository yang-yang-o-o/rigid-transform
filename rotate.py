import numpy as np
from math import cos,sin

# 绕x轴旋转

# 绕y轴旋转

# 绕z轴旋转

# 绕任意轴旋转
def rotation_k_θ(k,θ):
    '''
    input:
        k   :   [x,y,z], symmetry_axis
        θ   :   rad, rotation angle
    output:
        R   :   rotation matrix R(k,θ)
    '''
    return np.array([[k[0]*k[0]*(1-cos(θ))+cos(θ)     , k[1]*k[0]*(1-cos(θ))-k[2]*sin(θ), k[2]*k[0]*(1-cos(θ))+k[1]*sin(θ)],
                        [k[0]*k[1]*(1-cos(θ))+k[2]*sin(θ), k[1]*k[1]*(1-cos(θ))+cos(θ)     , k[2]*k[1]*(1-cos(θ))-k[0]*sin(θ)],
                        [k[0]*k[2]*(1-cos(θ))-k[1]*sin(θ), k[1]*k[2]*(1-cos(θ))+k[0]*sin(θ), k[2]*k[2]*(1-cos(θ))+cos(θ)]])
