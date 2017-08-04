__author__ = 'anecula'

import os
src="C:\Work\Classification\Images\/0.800\Adult-Female"
dest="C:\Work\Classification\Testers\Script_2_0_37_100\Awomen"
dir = os.listdir(src)

dir_txt = os.listdir(dest)

for poza in dir:
    if not poza + ".txt" in dir_txt:
        os.remove(src + "\\" +  poza)
    else:
        print poza