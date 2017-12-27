import requests
import json
import argparse
import sys
import time
from collections import defaultdict
result_dic = defaultdict(dict)
result_dic['name']['url']= [0][0]


def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Script to Enumerate ICO\'s')
    # Add arguments


    parser.add_argument(
        '-l', '--live', type=str, help='return a set of tuple\'s from live ICO\'s', required=False, default=None)
      # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    live = args.live
    # Return all variable values
    return live

def parser():
    url_live = 'https://api.icowatchlist.com/public/v1/live'
    live = get_args()
       
    if live:
        print('live ico list selected')
        method = 'live'
        Api_Call(url_live,method)
        


def Api_Call(url,method):
    try:
       tmp_names =[]
       tmp_lnks = []
       if method == "live":
          r = requests.get(url)
          data = json.loads(r.content.decode('utf-8'))
          data_parsed = data['ico']['live']
          for data in data_parsed:
              tmp_names.append(data['name'])
              tmp_lnks.append(data['website_link'])
              result_dic[0][1] = data['name'],data['website_link']
              print(result_dic[0][1])
             
              
    except:
        pass
        

def main():
    parser()
         
   

if __name__ == "__main__":
    main()
