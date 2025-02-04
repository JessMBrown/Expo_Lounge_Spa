import requests
import json
from flask import Flask, jsonify, request
from treatments_table import treatments
from employee_table import employees
from db_utils import get_all_treatments

app = Flask(__name__)


@app.route("/")
def hello():
    return {"Hello": 'Welcome to the Expo Lounge Hotel Spa Clinic'}


@app.route("/treatments")
def get_treatments_local():
    treatments_endpoint = input('Would you like to know what treatments we have on offer? ')

    if treatments_endpoint.lower() != "yes":
        return "<html><body> <h1>Ok. Thank you for looking </h1></body></html>"

    else:
        return jsonify(treatments)


@app.route('/Employees', methods=["GET"])
def get_employees_local():
    employees_endpoint = input('Would you like to know ALL employees details? (Yes/No')

    if employees_endpoint.lower() != "yes":
        return "<html><body> <h1>Ok. No employee data to display </h1></body></html>"

    else:
        return jsonify(employees)


@app.route('/Employees', methods=['POST'])
def add_new_employee_local():
    employee_to_be_added = request.get_json()
    employees.append(employee_to_be_added)
    return employee_to_be_added


# ### POST body for postman http://127.0.0.1:5000/Employees ### #
# {
#     "employee_ID": "0004",
#     "role": "Nail_Technician",
#     "salary": 40000,
#     "work_days": [
#         "MON, TUE, SAT, SUN"
#     ],
#     "start_time": "10:00:00",
#     "finish_time": "14:00:00"
# }


# NOTE: Due to the TIME column in bookings I cannot deserialize the response - so I'm using the more simple treatments
@app.route('/treatments/remote')
def get_treatments_remote():
    res = get_all_treatments()
    return jsonify(res)


# NOTE: Same as the above the insert will have use the treatments table
@app.route('/treatment', method=['PUT'])
def add_new_treatment_remote():
    treatments = request.get_json()
    # new_treatment(
    #     Treatment_Name=treatments['Treatment_Name'],
    #     Price_Per_Treatment=treatments['Price_Per_Treatment']
    #               )
    # return treatments

treatment_to_add = {"Treatment_Name": "Body_Massage",
    "Price_Per_Treatment": 125.00}

headers = {'content-type': 'application/json'}
result = requests.put(f'http://127.0.0.1:5001/treatment/', headers=headers, data=json.dumps(treatment_to_add))
print(result.status_code)


@app.route('/Bookings', methods=['POST'])
def gather_new_booking_details():
    date = input('What date would you like to book your treatment for? (YYYY-MM-DD): ')
    print()
    time = input('What time would you like to book your treatment for? (HH:MM:SS): ')
    print()
    treatment = input('What treatment would you like to book ? (1-11): ')
    print()
    employee = input('What date would you like to book your appointment for? (1-6): ')
    print('Thank you for all the details')
    add_new_treatment_remote(date, time, treatment, employee)
    print('Booking complete')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
