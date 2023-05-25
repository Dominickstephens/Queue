from chalice import Chalice
import requests

import text

app = Chalice(app_name='helloworld')

Q = []


def send_message(msg):
    if msg == "":
        return "No message to send"
    response = text.send_sms(msg)
    return response


def reset_q():
    Q.clear()
    return Q


def add_customer(phone_number, name, party_size):
    Q.append([phone_number, name, party_size])
    return Q


def notify_ready():
    notify_customer = Q[0]
    text = "Hi, " + notify_customer[1] + ". Your table is ready. Please come to the front desk."

    return send_message(text)

def remove_first():
    Q.pop(0)
    return Q


def check_q_stats():
    return Q


def check_q_position(phone_number):
    for i in range(len(Q)):
        if Q[i][0] == phone_number:
            return "Your position in the queue is " + str(i + 1)
    return "You are not in the queue"


def cancel_request(phone_number):
    for i in range(len(Q)):
        if Q[i][0] == phone_number:
            Q.pop(i)
            return "Your request has been cancelled"
    return "You are not in the queue"



@app.route('/')
def index():
    return {'hello': 'world'}

# Employee routes


@app.route('/employee')
def employee():
    return {'hello': 'employee'}


@app.route('/employee/reset')
def reset():
    return {'response': reset_q()}


@app.route('/employee/add')
def add():
    phone_number = app.current_request.query_params.get('phone_number', '')
    name = app.current_request.query_params.get('name', '')
    party_size = app.current_request.query_params.get('party_size', '')
    return {'response': add_customer(phone_number, name, party_size)}


@app.route('/employee/notify')
def notify():
    return {'response': notify_ready()}

@app.route('/employee/remove')
def remove():
    return {'response': remove_first()}

@app.route('/employee/stats')
def stats():
    return {'response': check_q_stats()}

# Customer routes

@app.route('/customer')
def customer():
    return {'hello': 'customer'}

@app.route('/customer/cancel')
def cancel():
    phone_number = app.current_request.query_params.get('phone_number', '')
    return {'response': cancel_request(phone_number)}

@app.route('/customer/position')
def position():
    phone_number = app.current_request.query_params.get('phone_number', '')
    return {'response': check_q_position(phone_number)}

