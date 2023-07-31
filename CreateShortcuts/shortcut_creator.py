import os, winshell
from win32com.client import Dispatch

def shortcut_creator(target_path, working_dir_path, icon_path=''):
    desktop = winshell.desktop()
    path = os.path.join(desktop, working_dir_path.split('\\')[-1] + ".lnk")    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = working_dir_path
    if icon_path == '':
        pass
    else:
        shortcut.IconLocation = icon_path
    shortcut.save()
    
    
    
# if __name__ == '__main__':
#     shortcut_creator(r"C:\Users\Mario Moysen\anaconda3\envs\digital_sign\digital_sign\PDFs Firmados",
#               r"C:\Users\Mario Moysen\anaconda3\envs\digital_sign\digital_sign\PDFs Firmados")    