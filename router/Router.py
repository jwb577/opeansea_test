from flask import current_app


class Router:

    def start():

        @current_app.route('/names/<name>', methods=['POST'])
        def update(name):
            
            
        @current_app.route('', methods=['GET'])
        def fetch():

        @current_app.route('', methods=['GET'])
        def delete():

        @current_app.route('/annotate')
        def annotate():
