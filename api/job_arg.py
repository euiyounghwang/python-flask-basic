
from job.job import create_jobs
from argparse import ArgumentParser
import os


def argument_to_job_create():
    parser = ArgumentParser()
    
    parser.add_argument('-r')
    parser.add_argument('-e')
    
    args = parser.parse_args()
    
    if args.r:
        os.environ['API_AND_BACKGROUND'] = args.r
        
        if os.environ.get("API_AND_BACKGROUND") == 'API_AND_BACKGROUND':
            create_jobs()
            
    if args.e:
        ''' dev, stating, prod'''
        os.environ['run-environment'] = args.e
    else:
        os.environ['run-environment'] = 'dev'
