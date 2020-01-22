
import time
import subprocess


blenderExcPath = "/home/pata/blender/blender-2.81a-linux-glibc217-x86_64/blender"
blenderFilePath = "/home/pata/data/test_cycles_cpu.blend"
outputPath = "/home/pata/nginx/html/rendered/frame_###"
frameNr = 8
def do_render():
    p = subprocess.run([
            blenderExcPath,
            "-b",
            blenderFilePath,
            "-o",
            outputPath,
            "-f",
            str(frameNr)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,#output error combine into stdout
        check=True)

    while True:
        time.sleep(2)
        stdout,stderr = p.communicate()
        print("std : " + stdout)
    

    return p # output std and err info via PIPE to caller
    # print(res.stdout)
    # print(res.returncode)  

    # print(res.stderr) # check=True will output trackback info about error


def newJob():

    p = do_render()
    while True:
        time.sleep(2)
        stdout,stderr = p.communicate()
        print("std : " + stdout)




if __name__ == '__main__':
    # newJob()
    do_render()
