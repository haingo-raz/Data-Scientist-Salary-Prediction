from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import joblib
import numpy as np
import traceback

app = Flask(__name__)

VALID_USERNAME ='admin'
VALID_PASSWORD ='Admin@123'

# Secret key session management
app.secret_key ='_5y2L"F4Q8z\n\xec]/'

# Load model and model columns
catboost_model = joblib.load('model.pkl')
print('Model loaded')
model_columns = joblib.load('model_columns.pkl')
print('Model columns loaded')


# Define mappings
experience_level_map = {'Senior': 3, 'Mid-level': 2, 'Entry-level': 0, 'Executive': 1}
employment_type_map = {'Contract': 0, 'Part-time': 1, 'Full-time': 2, 'Freelance': 3}
remote_ratio_map = {100: 2, 0: 0, 50: 1}
company_location_map = {
    'ES': 0.857142857142857, 'US': 3, 'CA': 0, 'DE': 0.428571428571428, 'GB': 1.71428571428571,
    'IN': 2.14285714285714, 'FR': 1.28571428571428, 'Other': 2.57142857142857
}
company_size_map = {'Medium': 1, 'Large': 3, 'Small': 2}
job_title_map = {
    'Data Scientist': 1.96875, 'Machine Learning Engineer': 2.71875, 'Applied Scientist': 0.1875, 
    'Data Analyst': 1.03125, 'Data Modeler': 1.6875, 'Research Engineer': 2.90625, 
    'Analytics Engineer': 0.09375, 'Business Intelligence Engineer': 0.65625, 
    'Data Strategist': 2.15625, 'Data Engineer': 1.3125, 'Computer Vision Engineer': 0.84375, 
    'Data Quality Analyst': 1.875, 'Data Architect': 1.125, 'Research Scientist': 3, 
    'ETL Engineer': 2.4375, 'Data DevOps Engineer': 1.21875, 'AI Specialist': 0, 
    'Head of Data': 2.53125, 'Data Manager': 1.59375, 'Data Specialist': 2.0625, 
    'Autonomous Vehicle Technician': 0.28125, 'Cloud Database Engineer': 0.75, 
    'Data Infrastructure Engineer': 1.40625, 'Data Operations Engineer': 1.78125, 
    'Deep Learning Researcher': 2.34375, 'Business Intelligence Analyst': 0.46875, 
    'Insight Analyst': 2.625, 'Deep Learning Engineer': 2.25, 'Big Data Architect': 0.375, 
    'Computer Vision Software Engineer': 0.9375, 'Business Intelligence Developer': 0.5625, 
    'Data Lead': 1.5, 'NLP Engineer': 2.8125
}

@app.route('/')
def home():
    # User is redirected to the predict page if already logged in
    if session.get('logged_in'):
        return render_template('predict.html')
    return render_template('home.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # User is redirected to the predict page if already logged in
    if session.get('logged_in'):
        return render_template('predict.html')
    feedback_text = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        feedback_text = "Login successful"
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            return render_template('predict.html')
        else:
            feedback_text = "Invalid credentials."
    return render_template('login.html', feedback=feedback_text)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # The API cannot be accessed if the user is not logged in
    if not session.get('logged_in'):
        return redirect(url_for('home'))
    if catboost_model:
        try:
            # Get form values
            job_title = request.form['job_title']
            experience_level = request.form['experience_level']
            employment_type = request.form['employment_type']
            remote_ratio = request.form['remote_ratio']
            company_size = request.form['company_size']
            company_location = request.form['company_location']

            # Transform values using the mappings
            job_title_en = job_title_map.get(job_title)
            experience_level_en = experience_level_map.get(experience_level)
            employment_type_en = employment_type_map.get(employment_type)
            remote_ratio_en = remote_ratio_map.get(remote_ratio)
            company_size_en = company_size_map.get(company_size)
            company_location_en = company_location_map.get(company_location)

            # Create input array for prediction
            arr = np.array([[job_title_en, experience_level_en, employment_type_en, 
                            remote_ratio_en, company_size_en, company_location_en]])

            # Predict
            pred = catboost_model.predict(arr)

            # Prepare input data for display
            input_data = {
                'Job Title': job_title,
                'Experience Level': experience_level,
                'Employment Type': employment_type,
                'Remote Ratio': remote_ratio,
                'Company Size': company_size,
                'Company Location': company_location
            }

            return render_template('predict.html',
                                   prediction_text='Predicted salary: ${:.2f}'.format(pred[0]),
                                   features=input_data)
        except Exception as e:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('No model to use.')
        return jsonify({'trace': 'No model to use.'})
    
# Logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
