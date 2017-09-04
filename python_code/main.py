# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 04:31:02 2017

@author: Matthew A. O'Brien

Purpose: To dig into the 900K observation Lending Club dataset. 
         The project will also be used as a test project for John Haley's
         distributed processing environment. 
         
Notes: Data stored in:
        C:\Users\matthew\Documents\lending-club-loan-data
"""

#--------------------------------------------------------------------------#

import sqlite3
import pandas as pd


conn = sqlite3.connect(r'C:\Users\matthew\Documents\lending-club-loan-data\database.sqlite')

cur = conn.cursor()

cur.execute("""
            SELECT *
            from loan
            LIMIT 100
            """)
pd.DataFrame(cur.fetchall())
print
