from api import init_api
# from job.job import create_jobs
from .job_arg import argument_to_job_create
# from gevent.pywsgi import WSGIServer
from waitress import serve
''' Waitress is a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones which live in the Python standard library'''
import os

application = init_api()

# --
# a process that runs in the background
# create_jobs()
# --

# -r API_AND_BACKGROUND
def main():
    app = init_api()
    
    # --
    # arguments for BACKGROUND with events
    argument_to_job_create()
    
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    
    app.run(port=5000, debug=True) if os.environ.get("run-environment") == 'dev' else serve(app, host="0.0.0.0", port=5000)

    

if __name__ == "__main__":
    main()