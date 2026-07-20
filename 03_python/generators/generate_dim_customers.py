import random
from datetime import date

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

NUM_CUSTOMERS = 10000

COUNTRIES = [
    "India",
    "United States",
    "United Kingdom",
    "Canada",
    "Australia"
]

ACQUISITION_CHANNELS = [
    "Organic Search",
    "Google Ads",
    "Instagram Ads",
    "Facebook Ads",
    "Youtube",
    "Referral",
    "Email Campaign",
    "App Store",
    "Play Store"
]

ACCOUNT_STATUS = [
    "Active",
    "Suspended",
    "Closed"
]

INCOME_BANDS = [
    "Low",
    "Medium",
    "High"
]

GENDERS = [
    "Male",
    "Female",
    "Other"
]

def generate_customers(num_customers):
    customers = []
    
    for customer_id in range(1, num_customers + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}{customer_id}@streamflow.com"
        customer = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        customers.append(customer)
    return pd.DataFrame(customers)

if __name__ == "__main__":

    df_customers = generate_customers(NUM_CUSTOMERS)

    print(df_customers.head())
    
