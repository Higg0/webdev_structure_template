'''
Contains all of the site views. Basically a ToC.
This will be a lot of the meat of the app.
'''

from flask import render_template
from app import app

@app.route('/')
@app.route('/splash')
def splash():
    section='Splash Page'
    desc='Homepage the users first reach.'
    links=[['sample-link-1','1st Sample Link'],
           ['sample-link-2','2nd Sample Link']]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
@app.route('/sample-link-1')
def sample_link_1():
    section='1st Sample Link'
    desc='The first page you can link to.'
    links=[['','Home']]
    return render_template('sample.html', section=section, desc=desc, links=links)
    
@app.route('/sample-link-2')
def sample_link_2():
    section='2nd Sample Link'
    desc='The second page you can link to.'
    links=[['','Home']]
    return render_template('sample.html', section=section, desc=desc, links=links)