from flask import (Flask, render_template)
from sseclient import SSEClient

app = Flask(__name__)
app.secret_key = "This doesn't really matter"

# messages = SSEClient('http://live-test-scores.herokuapp.com/scores')


@app.route('/')
def get_homepage():
    return "what"


@app.route('/students')
def get_students():
    """Lists all users that have received at least one test score"""
    

    return render_template('students.html')


@app.route('/students/{id}')
def get_test_results_by_student_id():
    """Lists the test results for the specified student,
        and provides the student's average score across all exams"""
    pass


@app.route('/exams')
def get_exams():
    """Lists all the exams that have been recorded"""
    pass


@app.route('/exams/{number}')
def get_results_by_exam():
    """Lists all the results for the specified exam,
        and provides the average score across all students"""
    pass


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
