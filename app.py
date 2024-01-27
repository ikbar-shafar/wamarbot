from flask import Flask, render_template, request
import pywhatkit
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_messages', methods=['POST'])
def send_messages():
    nums = request.form.get('numbers')
    message = request.form.get('message')
    delay = int(request.form.get('delay'))

    try:
        numbers = nums.split(',')
        for c in numbers:
            pywhatkit.sendwhatmsg_instantly(c.strip(), message, 30)
            print(f"Successfully sent to {c.strip()}")
            time.sleep(delay)
        return "Messages sent successfully!"

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Error sending messages."
if __name__ == '__main__':
    app.run(debug=True)
