import requests
import json
import argparse
import sys
import time



def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Script to Enumerate ICO\'s')
    # Add arguments
    parser.add_argument(
        '-f', '--finished', type=str, help='return a set of tuple\'s  from finished ICO\'s', required=False)
    parser.add_argument(
        '-u', '--upcoming', type=str, help='return a set of tuple\'s from upcoming ICO\'s', required=False, nargs='+')
    parser.add_argument(
        '-l', '--live', type=str, help='return a set of tuple\'s from live ICO\'s', required=False, default=None)
      # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    finished = args.finished
    upcoming = args.upcoming
    live = args.live
    # Return all variable values
    return finished, upcoming,live

def parser():
    url_live = 'https://api.icowatchlist.com/public/v1/live'
    url_upcoming = 'https://api.icowatchlist.com/public/v1/upcoming'
    url_finished = 'https://api.icowatchlist.com/public/v1/finished'
    finished, upcoming, live = get_args()
     
    if finished:
        print('finished ico list selected')
        method = 'finished'
        finished_names,finished_links = Api_Call(url_finished,method)
        for live in finished_names:
            print(live)

        for live in finished_links:
            print(live)
        return finished_names,finished_links

    if upcoming:
        print('upcoming ico list selected')
        method = 'upcoming'
        upcoming_names,upcoming_links = Api_Call(url_upcoming,method)
        for live in upcoming_names:
            print(live)

        for live in upcoming_links:
            print(live)
        return upcoming_names,upcoming_links
       
    if live:
        print('live ico list selected')
        method = 'live'
        live_names,live_links = Api_Call(url_live,method)
        for live in live_names:
            print(live)

        for live in live_links:
            print(live)
        return live_names,live_links

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
          return tmp_names,tmp_lnks
        
       elif method == "finished":
          r = requests.get(url)
          data = json.loads(r.content.decode('utf-8'))
          data_parsed = data['ico']['finished']
          for data in data_parsed:
              tmp_names.append(data['name'])
              tmp_lnks.append(data['website_link'])
          return tmp_names,tmp_lnks

       elif method == "upcoming":
          r = requests.get(url)
          data = json.loads(r.content.decode('utf-8'))
          data_parsed = data['ico']['upcoming']
          for data in data_parsed:
              tmp_names.append(data['name'])
              tmp_lnks.append(data['website_link'])
          return tmp_names,tmp_lnks
           
    except:
        pass
    

def main():
    parsed_names,parsed_urls = parser()
    
    
    for domains in parsed_urls:
        try:
           print(domains)
           
        except:
            pass

if __name__ == "__main__":
    main()
