import numpy as np
"""
Section 8
Generate arc points to make blade curve in x-y plane
"""

def generate_arc_points(N, ordered_vertices, width, y_coords):
    
    
    arc_array = np.zeros((38, 3, N))
    arc1_x = []
    arc1_z = []
    arc1_y = []
    
    for j in range(N):
        arc_offset = j * 56
        
        R = np.sqrt(width**2 + (y_coords[j])**2) 
        
        arc1_x = (ordered_vertices[16 + arc_offset][0] + ordered_vertices[0 + arc_offset][0])/2    
        arc1_z = (ordered_vertices[16 + arc_offset][2] + ordered_vertices[0 + arc_offset][2])/2     
        arc1_y = np.sqrt(R**2 -arc1_x**2) 
        
        arc_array[0, :, j] = np.array([[arc1_x, arc1_y, arc1_z]])
        
        arc2_x = (ordered_vertices[17 + arc_offset][0] + ordered_vertices[1 + arc_offset][0])/2    
        arc2_z = (ordered_vertices[17 + arc_offset][2] + ordered_vertices[1 + arc_offset][2])/2     
        arc2_y = np.sqrt(R**2 -arc2_x**2)
        
        arc_array[1, :, j] = np.array([[arc2_x, arc2_y, arc2_z]])
        
        arc3_x = (ordered_vertices[18 + arc_offset][0] + ordered_vertices[2 + arc_offset][0])/2    
        arc3_z = (ordered_vertices[18 + arc_offset][2] + ordered_vertices[2 + arc_offset][2])/2     
        arc3_y = np.sqrt(R**2 -arc3_x**2)
        
        arc_array[2, :, j] = np.array([[arc3_x, arc3_y, arc3_z]])
        
        arc4_x = (ordered_vertices[19 + arc_offset][0] + ordered_vertices[3 + arc_offset][0])/2    
        arc4_z = (ordered_vertices[19 + arc_offset][2] + ordered_vertices[3 + arc_offset][2])/2     
        arc4_y = np.sqrt(R**2 -arc4_x**2)
        
        arc_array[3, :, j] = np.array([[arc4_x, arc4_y, arc4_z]])
        
        arc5_x = (ordered_vertices[20 + arc_offset][0] + ordered_vertices[4 + arc_offset][0])/2    
        arc5_z = (ordered_vertices[20 + arc_offset][2] + ordered_vertices[4 + arc_offset][2])/2     
        arc5_y = np.sqrt(R**2 -arc5_x**2)
        
        arc_array[4, :, j] = np.array([[arc5_x, arc5_y, arc5_z]])
        
        arc6_x = (ordered_vertices[21 + arc_offset][0] + ordered_vertices[5 + arc_offset][0])/2    
        arc6_z = (ordered_vertices[21 + arc_offset][2] + ordered_vertices[5 + arc_offset][2])/2     
        arc6_y = np.sqrt(R**2 -arc6_x**2)
        
        arc_array[5, :, j] = np.array([[arc6_x, arc6_y, arc6_z]])
        
        arc7_x = (ordered_vertices[22 + arc_offset][0] + ordered_vertices[6 + arc_offset][0])/2    
        arc7_z = (ordered_vertices[22 + arc_offset][2] + ordered_vertices[6 + arc_offset][2])/2     
        arc7_y = np.sqrt(R**2 -arc7_x**2)
        
        arc_array[6, :, j] = np.array([[arc7_x, arc7_y, arc7_z]])
        
        arc8_x = (ordered_vertices[23 + arc_offset][0] + ordered_vertices[7 + arc_offset][0])/2    
        arc8_z = (ordered_vertices[23 + arc_offset][2] + ordered_vertices[7 + arc_offset][2])/2     
        arc8_y = np.sqrt(R**2 -arc8_x**2)
        
        arc_array[7, :, j] = np.array([[arc8_x, arc8_y, arc8_z]])
        
        arc9_x = (ordered_vertices[24 + arc_offset][0] + ordered_vertices[8 + arc_offset][0])/2    
        arc9_z = (ordered_vertices[24 + arc_offset][2] + ordered_vertices[8 + arc_offset][2])/2     
        arc9_y = np.sqrt(R**2 -arc9_x**2)
        
        arc_array[8, :, j] = np.array([[arc9_x, arc9_y, arc9_z]])
        
        arc10_x = (ordered_vertices[25 + arc_offset][0] + ordered_vertices[9 + arc_offset][0])/2    
        arc10_z = (ordered_vertices[25 + arc_offset][2] + ordered_vertices[9 + arc_offset][2])/2     
        arc10_y = np.sqrt(R**2 -arc10_x**2)
        
        arc_array[9, :, j] = np.array([[arc10_x, arc10_y, arc10_z]])
        
        arc11_x = (ordered_vertices[26 + arc_offset][0] + ordered_vertices[10 + arc_offset][0])/2    
        arc11_z = (ordered_vertices[26 + arc_offset][2] + ordered_vertices[10 + arc_offset][2])/2     
        arc11_y = np.sqrt(R**2 -arc11_x**2)
        
        arc_array[10, :, j] = np.array([[arc11_x, arc11_y, arc11_z]])
        
        arc12_x = (ordered_vertices[27 + arc_offset][0] + ordered_vertices[11 + arc_offset][0])/2    
        arc12_z = (ordered_vertices[27 + arc_offset][2] + ordered_vertices[11 + arc_offset][2])/2     
        arc12_y = np.sqrt(R**2 -arc12_x**2)
        
        arc_array[11, :, j] = np.array([[arc12_x, arc12_y, arc12_z]])
        
        arc13_x = (ordered_vertices[28 + arc_offset][0] + ordered_vertices[12 + arc_offset][0])/2    
        arc13_z = (ordered_vertices[28 + arc_offset][2] + ordered_vertices[12 + arc_offset][2])/2     
        arc13_y = np.sqrt(R**2 -arc13_x**2)
        
        arc_array[12, :, j] = np.array([[arc13_x, arc13_y, arc13_z]])
        
        arc14_x = (ordered_vertices[29 + arc_offset][0] + ordered_vertices[13 + arc_offset][0])/2    
        arc14_z = (ordered_vertices[29 + arc_offset][2] + ordered_vertices[13 + arc_offset][2])/2     
        arc14_y = np.sqrt(R**2 -arc14_x**2)
        
        arc_array[13, :, j] = np.array([[arc14_x, arc14_y, arc14_z]])
        
        arc15_x = (ordered_vertices[30 + arc_offset][0] + ordered_vertices[14 + arc_offset][0])/2    
        arc15_z = (ordered_vertices[30 + arc_offset][2] + ordered_vertices[14 + arc_offset][2])/2     
        arc15_y = np.sqrt(R**2 -arc15_x**2)
        
        arc_array[14, :, j] = np.array([[arc15_x, arc15_y, arc15_z]])
        
        arc16_x = (ordered_vertices[31 + arc_offset][0] + ordered_vertices[15 + arc_offset][0])/2    
        arc16_z = (ordered_vertices[31 + arc_offset][2] + ordered_vertices[15 + arc_offset][2])/2     
        arc16_y = np.sqrt(R**2 -arc16_x**2)
        
        arc_array[15, :, j] = np.array([[arc16_x, arc16_y, arc16_z]])
        
        arc17_x = (ordered_vertices[32 + arc_offset][0] + ordered_vertices[16 + arc_offset][0])/2    
        arc17_z = (ordered_vertices[32 + arc_offset][2] + ordered_vertices[16 + arc_offset][2])/2     
        arc17_y = np.sqrt(R**2 -arc17_x**2)
        
        arc_array[16, :, j] = np.array([[arc17_x, arc17_y, arc17_z]])
        
        arc18_x = (ordered_vertices[33 + arc_offset][0] + ordered_vertices[17 + arc_offset][0])/2    
        arc18_z = (ordered_vertices[33 + arc_offset][2] + ordered_vertices[17 + arc_offset][2])/2     
        arc18_y = np.sqrt(R**2 -arc18_x**2)
        
        arc_array[17, :, j] = np.array([[arc18_x, arc18_y, arc18_z]])
        
        arc19_x = (ordered_vertices[34 + arc_offset][0] + ordered_vertices[18 + arc_offset][0])/2    
        arc19_z = (ordered_vertices[34 + arc_offset][2] + ordered_vertices[18 + arc_offset][2])/2     
        arc19_y = np.sqrt(R**2 -arc19_x**2)
        
        arc_array[18, :, j] = np.array([[arc19_x, arc19_y, arc19_z]])
        
        arc20_x = (ordered_vertices[42 + arc_offset][0] + ordered_vertices[22 + arc_offset][0])/2    
        arc20_z = (ordered_vertices[42 + arc_offset][2] + ordered_vertices[22 + arc_offset][2])/2     
        arc20_y = np.sqrt(R**2 -arc20_x**2)
        
        arc_array[19, :, j] = np.array([[arc20_x, arc20_y, arc20_z]])
        
        arc21_x = (ordered_vertices[43 + arc_offset][0] + ordered_vertices[23 + arc_offset][0])/2    
        arc21_z = (ordered_vertices[43 + arc_offset][2] + ordered_vertices[23 + arc_offset][2])/2     
        arc21_y = np.sqrt(R**2 -arc21_x**2)
        
        arc_array[20, :, j] = np.array([[arc21_x, arc21_y, arc21_z]])
        
        arc22_x = (ordered_vertices[44 + arc_offset][0] + ordered_vertices[24 + arc_offset][0])/2    
        arc22_z = (ordered_vertices[44 + arc_offset][2] + ordered_vertices[24 + arc_offset][2])/2     
        arc22_y = np.sqrt(R**2 -arc22_x**2)
        
        arc_array[21, :, j] = np.array([[arc22_x, arc22_y, arc22_z]])

        arc23_x = (ordered_vertices[45 + arc_offset][0] + ordered_vertices[25 + arc_offset][0])/2    
        arc23_z = (ordered_vertices[45 + arc_offset][2] + ordered_vertices[25 + arc_offset][2])/2     
        arc23_y = np.sqrt(R**2 -arc23_x**2)
        
        arc_array[22, :, j] = np.array([[arc23_x, arc23_y, arc23_z]])
        
        arc24_x = (ordered_vertices[46 + arc_offset][0] + ordered_vertices[26 + arc_offset][0])/2    
        arc24_z = (ordered_vertices[46 + arc_offset][2] + ordered_vertices[26 + arc_offset][2])/2     
        arc24_y = np.sqrt(R**2 -arc24_x**2)
        
        arc_array[23, :, j] = np.array([[arc24_x, arc24_y, arc24_z]])

        arc25_x = (ordered_vertices[54 + arc_offset][0] + ordered_vertices[30 + arc_offset][0])/2    
        arc25_z = (ordered_vertices[54 + arc_offset][2] + ordered_vertices[30 + arc_offset][2])/2     
        arc25_y = np.sqrt(R**2 -arc25_x**2)
        
        arc_array[24, :, j] = np.array([[arc25_x, arc25_y, arc25_z]])
        
        arc26_x = (ordered_vertices[55 + arc_offset][0] + ordered_vertices[31 + arc_offset][0])/2    
        arc26_z = (ordered_vertices[55 + arc_offset][2] + ordered_vertices[31 + arc_offset][2])/2     
        arc26_y = np.sqrt(R**2 -arc26_x**2)
        
        arc_array[25, :, j] = np.array([[arc26_x, arc26_y, arc26_z]])
        
        arc27_x = (ordered_vertices[35 + arc_offset][0] + ordered_vertices[36 + arc_offset][0])/2    
        arc27_z = (ordered_vertices[35 + arc_offset][2] + ordered_vertices[36 + arc_offset][2])/2     
        arc27_y = np.sqrt(R**2 -arc27_x**2)
        
        arc_array[26, :, j] = np.array([[arc27_x, arc27_y, arc27_z]])

        arc28_x = (ordered_vertices[36 + arc_offset][0] + ordered_vertices[37 + arc_offset][0])/2    
        arc28_z = (ordered_vertices[36 + arc_offset][2] + ordered_vertices[37 + arc_offset][2])/2     
        arc28_y = np.sqrt(R**2 -arc28_x**2)
        
        arc_array[27, :, j] = np.array([[arc28_x, arc28_y, arc28_z]])

        arc29_x = (ordered_vertices[37 + arc_offset][0] + ordered_vertices[38 + arc_offset][0])/2    
        arc29_z = (ordered_vertices[37 + arc_offset][2] + ordered_vertices[38 + arc_offset][2])/2     
        arc29_y = np.sqrt(R**2 -arc29_x**2)
        
        arc_array[28, :, j] = np.array([[arc29_x, arc29_y, arc29_z]])

        arc30_x = (ordered_vertices[38 + arc_offset][0] + ordered_vertices[39 + arc_offset][0])/2    
        arc30_z = (ordered_vertices[38 + arc_offset][2] + ordered_vertices[39 + arc_offset][2])/2     
        arc30_y = np.sqrt(R**2 -arc30_x**2)
        
        arc_array[29, :, j] = np.array([[arc30_x, arc30_y, arc30_z]])
        
        arc31_x = (ordered_vertices[39 + arc_offset][0] + ordered_vertices[40 + arc_offset][0])/2    
        arc31_z = (ordered_vertices[39 + arc_offset][2] + ordered_vertices[40 + arc_offset][2])/2     
        arc31_y = np.sqrt(R**2 -arc31_x**2)
        
        arc_array[30, :, j] = np.array([[arc31_x, arc31_y, arc31_z]])
        
        arc32_x = (ordered_vertices[40 + arc_offset][0] + ordered_vertices[41 + arc_offset][0])/2    
        arc32_z = (ordered_vertices[40 + arc_offset][2] + ordered_vertices[41 + arc_offset][2])/2     
        arc32_y = np.sqrt(R**2 -arc32_x**2)
        
        arc_array[31, :, j] = np.array([[arc32_x, arc32_y, arc32_z]])
        
        arc33_x = (ordered_vertices[47 + arc_offset][0] + ordered_vertices[48 + arc_offset][0])/2    
        arc33_z = (ordered_vertices[47 + arc_offset][2] + ordered_vertices[48 + arc_offset][2])/2     
        arc33_y = np.sqrt(R**2 -arc33_x**2)
        
        arc_array[32, :, j] = np.array([[arc33_x, arc33_y, arc33_z]])
        
        arc34_x = (ordered_vertices[48 + arc_offset][0] + ordered_vertices[49 + arc_offset][0])/2    
        arc34_z = (ordered_vertices[48 + arc_offset][2] + ordered_vertices[49 + arc_offset][2])/2     
        arc34_y = np.sqrt(R**2 -arc34_x**2)
        
        arc_array[33, :, j] = np.array([[arc34_x, arc34_y, arc34_z]])

        arc35_x = (ordered_vertices[49 + arc_offset][0] + ordered_vertices[50 + arc_offset][0])/2    
        arc35_z = (ordered_vertices[49 + arc_offset][2] + ordered_vertices[50 + arc_offset][2])/2     
        arc35_y = np.sqrt(R**2 -arc35_x**2)
        
        arc_array[34, :, j] = np.array([[arc35_x, arc35_y, arc35_z]])
        
        arc36_x = (ordered_vertices[50 + arc_offset][0] + ordered_vertices[51 + arc_offset][0])/2    
        arc36_z = (ordered_vertices[50 + arc_offset][2] + ordered_vertices[51 + arc_offset][2])/2     
        arc36_y = np.sqrt(R**2 -arc36_x**2)
        
        arc_array[35, :, j] = np.array([[arc36_x, arc36_y, arc36_z]])
        
        arc37_x = (ordered_vertices[51 + arc_offset][0] + ordered_vertices[52 + arc_offset][0])/2    
        arc37_z = (ordered_vertices[51 + arc_offset][2] + ordered_vertices[52 + arc_offset][2])/2     
        arc37_y = np.sqrt(R**2 -arc37_x**2)
        
        arc_array[36, :, j] = np.array([[arc37_x, arc37_y, arc37_z]])

        arc38_x = (ordered_vertices[52 + arc_offset][0] + ordered_vertices[53 + arc_offset][0])/2    
        arc38_z = (ordered_vertices[52 + arc_offset][2] + ordered_vertices[53 + arc_offset][2])/2     
        arc38_y = np.sqrt(R**2 -arc38_x**2)
        
        arc_array[37, :, j] = np.array([[arc38_x, arc38_y, arc38_z]])

        
    return arc_array
        
        
        
        
        
        
        
        
        

        
