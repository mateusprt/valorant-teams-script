import requests
from bs4 import BeautifulSoup


URL = 'https://liquipedia.net/valorant/Portal:Teams'
TEAMS = {}

def request(url):
  try:
    response = requests.get(url)
    if response:
      return response.text
  except Exception as error:
    print('An error occurred')
    print(error)


def parsing(response):
  response_soup = BeautifulSoup(response, 'html.parser')
  regions = response_soup.find_all('div', class_='toggle-group toggle-state-show')
  if regions:
    for region in regions:
      region_name = region.find_previous_sibling('h4').get_text().replace('[edit]', '')
      print(region_name)
      TEAMS[region_name] = []
      teams_by_region = region.find_all('div', class_='template-box')
      if teams_by_region:
        for team in teams_by_region:
          team_name = team.find('span', class_='team-template-text')
          if team_name:
            print(region_name + ' - ' + team_name.get_text().strip())
            TEAMS[region_name].append(team_name.get_text().strip())
      else:
        print('Teams not found')


response = request(URL)
if response:
  parsing(response)
  print(TEAMS)