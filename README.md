# About
This project aims to create a machine learning model that predicts a data science practitioner salary based on their job title, experience level, employment type, remote ratio, company size and company location. It makes use of a [dataset](https://www.kaggle.com/datasets/henryshan/2023-data-scientists-salary/data) from Kaggle.

# Technology
| Library       | Use Case                                      |
|---------------|-----------------------------------------------|
| Pandas        | Data manipulation and analysis                |
| Matplotlib    | Data visualization                            |
| Seaborn       | Statistical data visualization                |
| NumPy         | Numerical computing                           |
| AutoGluon     | AutoML for tabular, text, and image data      |
| Scikit-learn  | Machine learning algorithms and tools         |
| Catboost      | Gradient boosting on decision trees           |
| LightGBM      | Light Gradient Boosting Machine               |
| XGBoost       | Extreme Gradient Boosting                     |
| Pickle        | Serializing and de-serializing Python objects |
| Joblib        | Efficient serialization of large Python objects|
| Flask         | Web application framework                     |

# How to run the app
1. Install the packages from the `requirements.txt` file with the command:

```
pip install -r requirements.txt
```

This command will read the `requirements.txt` file and install all the packages listed in it. Make sure you run this command in the same directory where the `requirements.txt` file is located.

1. Run the Flask application by using the command: 

```
python application.py
```

1. The app will run on `localhost:5000`.

1. Login with given credentials.

1. Fill out the form values to perform predictions.

## Example requests and responses
```json
{
    "job_title": "Analytics Engineer",
    "experience_level": "Entry_level",
    "employment_type": "Contract",
    "remote_ratio": 0,
    "company_size": "Large",
    "company_location": "ES"
}
```

The predicted salary will be `$142560.89`

# Screenshots
## Login
![Login](/images/login.png)

## Prediction
![Predictions](/images/prediction.png)

## Available options for each feature
### Job title:
- Data Scientist
- Machine Learning Engineer
- Applied Scientist
- Data Analyst
- Data Modeler
- Research Engineer
- Analytics Engineer
- Business Intelligence Engineer
- Data Strategist
- Data Engineer
- Computer Vision Engineer
- Data Quality Analyst
- Data Architect
- Research Scientist
- ETL Engineer
- Data DevOps Engineer
- AI Specialist
- Head of Data
- Data Manager
- Data Specialist
- Autonomous Vehicle Technician
- Cloud Database Engineer
- Data Infrastructure Engineer
- Data Operations Engineer
- Deep Learning Researcher
- Business Intelligence Analyst
- Insight Analyst
- Deep Learning Engineer
- Big Data Architect
- Computer Vision Software Engineer
- Business Intelligence Developer
- Data Lead
- NLP Engineer

### Experience level
- Entry-level
- Mid-level
- Senior
- Executive

## Employment type
- Full-time
- Part-time
- Contract
- Freelance

## Remote ratio
- 0 (On-site)
- 50 (Hybrid)
- 100 (Remote)

## Company size
- Small
- Large
- Medium