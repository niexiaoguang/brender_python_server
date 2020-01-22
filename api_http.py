from flask import Flask
from flask import request
import utils
import settings
import render_task as RenderTask
import user_manager as UserManager
from flask import abort, jsonify


logger = logging.getLogger(__name__)

def initLogger():

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler(settings.logFilePath 
                                        +__name__ 
                                        + '_' 
                                        + str(int(time.time())) 
                                        + '.log'
                                        )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)






app = Flask(__name__)

# echo server 
@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route(apiHttpRenderFrameUrl,methods=['POST'])
def apiFrame():
	apiHandle(apiHttpRenderFrameUrl,request)


@app.route(apiHttpRenderAnimUrl,methods=['POST'])
def apiAnim():
	apiHandle(settings.apiHttpRenderAnimUrl,request)


@app.route(apiHttpJobInfoUrl,methods=['GET'])
def apiJonInfo():
	apiHandle(settings.apiHttpJobInfoUrl,request)


def apiHandle(path,request):
	res = None
    if UserManager.authReq(request):
    	logger.info(request)
    	if path == apiHttpRenderFrameUrl:
    		res = RenderTask.handleReqFrame(request)
    	else if path == apiHttpRenderAnimUrl:
    		res = RenderTask.handleReqAnim(request)
    	else if path == apiHttpJobInfoUrl:
    		res = RenderTask.handleReqJobInfo(request)
    	else:
    		logger.error('no match request : ' + request)

    	
	else:
		logger.warning(request)
		res = handleHttpReqAuthErr(request)

	return res



def handleHttpReqAuthErr(request):
	return jsonify(error=str(e)), 404  # auth error response  TODO
initLogger()