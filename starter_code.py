# -*- coding: utf-8 -*-
"""Starter Code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G3xct475mfdmZFBraP3QbVLxf0HbvivB

Unit Test-someda

Below is the starting code that includes the data pipeline functions. You should focus on writing unit tests for these functions using the unittest framework.
"""

import pandas as pd
import unittest

def data_extraction(file_path):
    data = pd.read.csv("/content/billing_data.csv")
    return data

def data_transformation(data):
    data = data.drop_duplicates()
    data['billing_amount'] = data['billing_amount'].str.replace('$', '').astype(float)
    data['total_charges'] = data['billing_amount'] + data['tax_amount']
    return data

def data_loading(data, output_file):
    data.to_csv(output_file, index=False)

class TestDataPipeline(unittest.TestCase):
    def setupclass(self):
        self.input_file = 'billing_data.csv'
        self.output_file = 'output.csv'

    def test_data_extraction(self):
        result = data_extraction(self.file_path)

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 5)
        self.assertEqual(list(result.columns), ['customer_id', 'billing_amount', 'tax_amount'])

    def test_data_transformation(self):
        input_data = pd.DataFrame({
            'customer_id': [1, 2, 3, 4, 5],
            'billing_amount': ['$100', '$200', '$300', '$400', '$500'],
            'tax_amount': [10, 20, 30, 40, 50]
        })

        result = data_transformation(input_data)

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 5)
        self.assertEqual(list(result.columns), ['customer_id', 'billing_amount', 'tax_amount', 'total_charges'])
        self.assertEqual(result['total_charges'].tolist(), [110, 220, 330, 440, 550])

    def test_data_loading(self):
        input_data = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'billing_amount': [100, 200, 300],
            'tax_amount': [10, 20, 30],
            'total_charges': [110, 220, 330]
        })

        data_loading(input_data, self.output_file)

        result = pd.read_csv(self.output_file)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 3)
        self.assertEqual(list(result.columns), ['customer_id', 'billing_amount', 'tax_amount', 'total_charges'])
        self.assertEqual(result['total_charges'].tolist(), [110, 220, 330])

if __name__ == '__main__':
    unittest.main()