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

app = Flask(__name__)

DEFAULT_PORT = 8080

class ServerUtil:
    """
    Collection of utility methods for this server
    """
    @staticmethod
    def handle_arg_parser():
        parser = ArgumentParser(description="A simple server")
        parser.add_argument("-p", "--port", required=False, default=DEFAULT_PORT, help="Port number to this server is "
                                                                                       "listening to")
        return parser.parse_args()

    
    @staticmethod
    def split_on_camel_case(data):
        matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', data)
        final_string = ''
        for match in matches:
            final_string += (match.group(0) + ' ')
        return final_string.strip()

    @staticmethod
    def write_log(**kwargs):
        app.logger.info(f"STATUS: {kwargs['status']}, REQUEST: {kwargs['msg']}")


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


if __name__ == "__main__":
    logging.basicConfig(level='INFO', format='%(asctime)s: %(message)s')
    
    args =  ServerUtil.handle_arg_parser()
    app.run(debug=True, host="0.0.0.0", port=int(args.port))

