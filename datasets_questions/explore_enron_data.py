#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


def number_of_datapoints():
    count = 0
    for person in enron_data:
        count += 1
        print person
    return count
# print number_of_datapoints()


def number_of_features():
    count = 0
    for feature in enron_data['SKILLING JEFFREY K']:
        count += 1
        print feature
    return count
print number_of_features()


def number_of_poi():
    count = 0
    print 'Number of POI'
    for person in enron_data:
        # count += 1
        for feature in enron_data[person]:
            if feature == "poi" and enron_data[person][feature] == 1:
                count += 1
                # print person, enron_data[person][feature]
    return count
print number_of_poi()


def display_info(name, feature):
    print 'Name: ', name
    return enron_data[name][feature]
# print display_info("FASTOW ANDREW S", "total_payments")
# print display_info("SKILLING JEFFREY K", "total_payments")
# print display_info("LAY KENNETH L", "total_payments")
# print display_info("KRAUTZ MICHAEL", "total_payments")

def has_quantified_salary():
    count = 0
    for person in enron_data:
        if enron_data[person]["salary"] != "NaN":
            print enron_data[person]["salary"]
            count += 1
    return count
# print has_quantified_salary() # 146

def has_known_email():
    count = 0
    for person in enron_data:
        # print enron_data[person]["email_address"]
        if enron_data[person]["email_address"] != "NaN":
            count += 1
    return count
# print has_known_email()

# REMEMBER: Difference between != and 'is not'


def has_nan_total_payments():
    count = 0
    print 'Total Payments as NaN'
    for person in enron_data:
        # print enron_data[person]["email_address"]
        if enron_data[person]["total_payments"] == "NaN":
            count += 1
    return count
# print has_nan_total_payments()  # 21


def poi_with_nan_total_payments():
    count = 0
    print 'POI with NaN Total Payments'
    for person in enron_data:
        # print enron_data[person]["email_address"]
        if enron_data[person]["total_payments"] == "NaN" and \
                        enron_data[person]["poi"] == 1:
            count += 1
    return count
# print poi_with_nan_total_payments()
