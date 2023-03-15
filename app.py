# from flask import Flask, render_template
# import requests

# app = Flask(__name__)

# def check_google_status():
#     try:
#         response = requests.get('https://www.google.com')
#         return response.status_code == 200
#     except:
#         return False

# @app.route('/')
# def index():
#     status = check_google_status()
#     return render_template('index.html', status=status)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template
import requests

app = Flask(__name__)

sites = [
    {'name': 'Google', 'url': 'https://www.google.com'},
    {'name': 'Facebook', 'url': 'https://www.facebook.com'},
    {'name': 'Twitter', 'url': 'https://www.twitter.com'},
    {'name': 'LinkedIn', 'url': 'https://www.linkedin.com'}
]

def check_status(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

@app.route('/')
def index():
    status_list = []
    for site in sites:
        status_list.append({
            'name': site['name'],
            'status': 'Available' if check_status(site['url']) else 'Unavailable'
        })
    return render_template('index.html', status_list=status_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
