#!/usr/bin/env python

__author__ = 'taitooz -> elourbet@despegar.com'
import json
import logging
import os
import csv
import time
import requests

file_to_process = 'imdbfy.csv'
file_result = open("modified_imdb.csv", "w")

with open(file_to_process, 'rb') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for idx, row in enumerate(csv_reader):
        if idx != 0:
            row[8] = row[9].split('.')[0]
        file_result.write(','.join(['"'+str(x)+'"' for x in row]) + '\n')
file_result.close()
