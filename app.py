from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home page route for Regex Matcher
@app.route('/')
def home():
    return render_template('index.html')

# Route for regex matching
@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex = request.form['regex']
    
    try:
        matches = re.findall(regex, test_string)
    except re.error:
        matches = ["Invalid regex pattern"]
    
    return render_template('index.html', matches=matches)

# Route for email validation
@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        
        # Simple regex for validating an email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if re.match(email_regex, email):
            validation_result = "Valid Email"
        else:
            validation_result = "Invalid Email"
        
        return render_template('validate_email.html', email_validation=validation_result)
    
    # Render the validation page when the user accesses it via GET
    return render_template('validate_email.html')

if __name__ == '__main__':
    app.run(debug=True)
