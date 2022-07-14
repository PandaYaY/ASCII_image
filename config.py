import os

# 70 * 50
clr_scr = lambda: os.system('cls')

size = 'mode 70, 50'
window_size = lambda: os.system(size)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
