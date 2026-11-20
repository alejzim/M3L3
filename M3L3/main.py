from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)


def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    return size * home_coef + lights * light_coef + device * devices_coef


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:size>')
def lights(size):
    return render_template('lights.html', size=size)


@app.route('/<int:size>/<int:lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)


@app.route('/<int:size>/<int:lights>/<int:device>')
def end(size, lights, device):
    result = result_calculate(size, lights, device)
    return render_template('end.html', result=result)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    address = request.form.get('address', '').strip()
    date = request.form.get('date', '').strip()

    with (Path(__file__).resolve().parent / 'form.txt').open('a', encoding='utf-8') as f:
        f.write(f'{name}\n{email}\n{address}\n{date}\n\n')

    return render_template(
        'form_result.html', name=name, email=email, address=address, date=date
    )


if __name__ == '__main__':
    app.run(debug=True)
