#!/usr/bin/env python

__author__ = 'taitooz -> elourbet@despegar.com'
import json
import logging
import os
import csv
import time
import requests

file_to_process = 'imdb.csv'
file_result = open("modified_imdb.csv", "w")

with open(file_to_process, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_reader:
        row_array = []
        for idx, column_data in enumerate(row):
            row_array.append('"' + column_data + '"')
        file_result.write(','.join(row_array) + '\n')
file_result.close()
