from flask import Flask, request

from twilio.twiml.messaging_response import MessagingResponse

from hotdog import hotdog_or_nothotdog

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_reply():
    resp = MessagingResponse()

    if request.form['NumMedia'] != '0':
        image_url = request.form['MediaUrl0']
        resp.message(hotdog_or_nothotdog(image_url))

    else: resp.message('Please send an image.')

    return str(resp)


if __name__ == '__main__':
    app.run()