""" yf_example3.py

The answer of the week4 code challenge.
"""
import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(tic,pth):
    """
    Download Qantas stock prices for a given year into a CSV file

    Parameters
    ----------
    year : int
          Year
    """
    df = yf_example2.yf_prc_to_csv(tic,pth,start='2020-01-01',end='2020-12-31')

if __name__ == "__main__":
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
    qan_prc_to_csv(tic,pth)