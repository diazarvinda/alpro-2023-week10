from flask import Flask, render_template, request, jsonify, session
import pandas as pd

app = Flask(__name__)
app.secret_key = 'kingofblokm'

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/ach')
def achievements():
    return render_template('ach.html') 

@app.route('/project')
def project():
    return render_template('project.html')  

@app.route('/hobby')
def hobby():
    return render_template('hobby.html')  
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('fname')
        email = request.form.get('email')
        message = request.form.get('message')

        contact_data = session.get('contact_data', [])
        contact_data.append({'name': name, 'email': email, 'message': message})
        session['contact_data'] = contact_data

        return render_template('contact.html', success_message="Message Sent!")

    return render_template('contact.html')

@app.route('/fibo', methods=['GET', 'POST'])
def fibonaci():
    fibonacci_sequence = None

    if request.method == 'POST':
        length = int(request.form['fibonacci-length'])
        fibonacci_sequence = generate_fibonacci(length)

    return render_template('fibo.html', fibonacci_sequence=fibonacci_sequence)

def generate_fibonacci(length):
    fibo_sequence = [1, 1]

    while len(fibo_sequence) < length:
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])

    return fibo_sequence

@app.route('/json')
def json():
    csv_file_path = 'static/datapribadi.csv'

    try:
        df = pd.read_csv(csv_file_path)
        json_data = df.to_json(orient='records')
        return render_template('json.html', json_data=json_data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/cont-log')
def log_contact():
    contact_data = session.get('contact_data', [])

    return render_template('log-contact.html', contact_data=contact_data)

if __name__ == '__main__':
    app.run(debug=True)

