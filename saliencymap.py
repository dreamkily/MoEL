import cv2
import numpy as np
 
def heat_map(path):
    fix = cv2.imread(path)
    max_val = np.max(fix)
    min_val = np.min(fix)
    fix = (fix - min_val)/(max_val - min_val)
    fix *= 255
    pred_ = fix.astype(np.uint8)
    pred_heat_map = cv2.applyColorMap(pred_, cv2.COLORMAP_JET)
    cv2.imwrite('./fix_heat.png', pred_heat_map)
 
fix_path = '/mnt/workspace/workgroup/jiannan.wmz/dg_dataset/PACS/photo/person/253_0384.jpg'
heat_map(fix_path)