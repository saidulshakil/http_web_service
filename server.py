#!/usr/bin/env python3

#
#   Description: A very simple web server
#
#   Date and Author: Saidul Islam
#

import requests
import logging
from flask import Flask
from flask import request
from flask import abort
from flask import Response
from flask import jsonify
from argparse import ArgumentParser
import os
import json
from re import finditer
import subprocess
from datetime import datetime

app = Flask(__name__)

DEFAULT_PORT = 8080

class ServerUtil:
    """
    Collection of utility methods for this server
    """
    @staticmethod
    def handle_arg_parser():
        """
        This function will take the command line arguments and process them
        for the apllication accordingly

        @return parser.parse_args() 
        """
        parser = ArgumentParser(description="A simple server")
        parser.add_argument("-p", "--port", required=False, default=DEFAULT_PORT, help="Port number to this server is "
                                                                                       "listening to")
        return parser.parse_args()

    
    @staticmethod
    def split_on_camel_case(data):
        """
        This function will parse the input argument and add blank spaces
        in the begining of the uppder cases. i.e. camel case separation by space    

        @param: string: data

        @return: string
        """
        matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', data)
        final_string = ''
        for match in matches:
            final_string += (match.group(0) + ' ')
        return final_string.strip()

    @staticmethod
    def write_log(**kwargs):
        app.logger.info(f"STATUS: {kwargs['status']}, REQUEST: {kwargs['msg']}")

    @staticmethod
    def set_up_environment(args):
        # Step 3 setting up the environment variable for the port
        # Though I am not sure by the instruction
        app.logger.info(args.port)
        os.environ['SERVERX_PORT'] = str(args.port)


# End ServerUtil

@app.route('/helloworld', methods=['GET', 'POST'])
def hello_world_with_arg():
    """
    Handles both the endpoint
    /helloworld and
    /helloworld?name=whatEverTheNameIs
    """
    try:
        name = request.args.get('name')
        ServerUtil.write_log(status=200, msg=request)
        return "Hello " + ServerUtil.split_on_camel_case(name)
    except Exception as e:
        pass

    ServerUtil.write_log(status=200, msg=request)
    return "Hello Stranger"

@app.route('/versionz', methods=['GET', 'POST'])
def version():
    """
    This function will handle the endpoint url:port/versionz

    @return: JSON
    """
    try:

        response_dict = {
            "git_hash": subprocess.check_output(["git", "describe", "--always"]).strip(),
            "project_name": "http_web_service",
            "time": datetime.now()
        }
        ServerUtil.write_log(status=200, msg=request)
        return jsonify(response_dict)
    except Exception as e:
        ServerUtil.write_log(status=400, msg=request)
        abort(400)

if __name__ == "__main__":
    logging.basicConfig(level='INFO', format='%(asctime)s: %(message)s')
    
    args =  ServerUtil.handle_arg_parser()
    ServerUtil.set_up_environment(args)
    app.run(debug=True, host="0.0.0.0", port=int(args.port))

