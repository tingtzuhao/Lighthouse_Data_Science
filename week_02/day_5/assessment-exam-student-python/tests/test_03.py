import pytest
import sys
import sqlite3
import pandas as pd
sys.path.append("..")
from answers.question_03 import SQL
from supporting_files.data_loader import load_data_from_database

DB = 'supporting_files/hr.db'
ANSWER_SQL = """SELECT first_name,
                last_name,
                salary, 
                0.12*salary as PF
         FROM employees
"""

df_answer = load_data_from_database(ANSWER_SQL,DB)


def test_on_valid_sql():
    global df_student

    try:
        df_student = load_data_from_database(SQL,DB)
    except:
        df_student = pd.DataFrame()
    
    assert not df_student.empty

def test_on_number_of_rows():
    assert df_student.shape[0] == df_answer.shape[0]

def test_on_number_of_columns():
    assert df_student.shape[1] == df_answer.shape[1]

def test_on_correct_columns():
    assert list(df_student.columns) == list(df_answer.columns)

def test_on_correct_answer():
    assert df_student.equals(df_answer)

