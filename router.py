from flask import request, g, render_template, current_app
import data
import json
import re

def create_routes():
    
        @current_app.route('/', methods=['GET'])
        def index():
            db = get_db()
            #return render_template('index.html', links={'google': 'http://www.google.com'})
            return render_template('index.html', data=db.hlink_names)

        @current_app.route('/names/<name>', methods=['POST'])
        def update(name):
            db = get_db()
            if request.method == 'POST':
                current_app.logger.debug(request.get_json())
                rv = request.args
                if 'url' in rv.keys() and pass_regex(name) != False:
                    current_app.logger.debug('HTTP: POST -- %s:%s Added to DB' % (name, rv['url']))
                    db.put(name, rv['url'])
                    return json.dumps(db.hlink_names), 200
                else: abort(400)

            return render_template('index.html', data=db.hlink_names)

        @current_app.route('/names/<name>', methods=['GET'])
        def fetch(name):
            if request.method == 'GET':
                db = get_db()
                return db.get(name)
            else: abort(404)

        @current_app.route('/names', methods=['DELETE'])
        def delete():
            if request.method == 'DELETE':
                db = get_db()
                db.delete()
            else: abort(404)

        @current_app.route('/annotate')
        def annotate():
            pass

        def get_db():
            if 'db' not in g:
                g.db = data.NamelinkDB()
            return g.db

        def pass_regex(name):
            r = re.findall('[A-Za-z0-9]+', name)
            if len(r) == 1:
                return r[0]
            else:
                return False