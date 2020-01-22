blenderExcPath = "/home/pata/blender/blender-2.81a-linux-glibc217-x86_64/blender"
testBlenderFilePath = "/home/pata/data/test_cycles_cpu.blend"
testOutputPath = "/home/pata/nginx/html/rendered/frame_#####"

jobMetaOuput = 'output'
debug = True


apiHttpRenderFrameUrl = '/render_frame'
apiHttpRenderAnimUrl = '/render_anim'
apiHttpJobInfoUrl = '/job_info'


subProcTimeout = 3600 # 1 hour to run subprocess of render

devMode = True
debugMode = True
logLevel = 'debug' # 'info' 'warning' 'error' 'critical'
logFilePath = './logs/'

