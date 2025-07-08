from faker import Faker
import pandas as pd
import random

fake = Faker()

# Predefined meaningful data
SYMPTOMS_LIST = [
    "fever", "cough", "fatigue", "headache", "shortness of breath",
    "nausea", "chest pain", "dizziness", "sore throat", "rash"
]

DIAGNOSIS_LIST = [
    "Common Cold", "Flu", "Migraine", "Asthma", "Diabetes",
    "Hypertension", "Food Poisoning", "Anemia", "Bronchitis", "Allergy"
]

def generate_healthcare_data(num_records=10):
    data = []
    for _ in range(num_records):
        record = {
            "Age": random.randint(18, 90),
            "Gender": random.choice(["Male", "Female", "Other"]),
            "Symptoms": ", ".join(random.sample(SYMPTOMS_LIST, 3)),
            "Diagnosis": random.choice(DIAGNOSIS_LIST),
            "DateOfVisit": fake.date_between(start_date="-1y", end_date="today")
        }
        data.append(record)
    return pd.DataFrame(data)
def generate_finance_data(num_records=10):
    data = []
    for _ in range(num_records):
        record = {
            "TransactionID": fake.uuid4(),
            "AccountHolder": fake.name(),
            "Amount": round(random.uniform(100, 5000), 2),
            "Type": random.choice(["Credit", "Debit"]),
            "Timestamp": fake.date_time_this_year(),
            "Location": fake.city()
        }
        data.append(record)
    return pd.DataFrame(data)
