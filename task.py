import requests
import subprocess

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

def oscmd():
	# p = subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)
	# p = subprocess.Popen(["/home/pata/blender/blender-2.81a-linux-glibc217-x86_64/blender","-b","/home/pata/data/test_cycles_cpu.blend","-o", "/home/pata/nginx/html/rendered/frame_#####","-f","3"], stdout=subprocess.PIPE) 

	# p = subprocess.Popen("/home/pata/blender/blender-2.81a-linux-glibc217-x86_64/blender -b /home/pata/data/test_cycles_cpu.blend -o /home/pata/nginx/html/rendered/frame3.png -f 3",stdout=subprocess.PIPE)

	p = subprocess.run(["/home/pata/blender/blender-2.81a-linux-glibc217-x86_64/blender","-b","/home/pata/data/test_cycles_cpu.blend","-o","/home/pata/nginx/html/rendered/frame_###","-f","5"])	
	print(p.communicate())
