import csv
import json
import urllib2

submissions = urllib2.urlopen('https://docs.google.com/spreadsheets/d/1HwdQudacNaRwfjcqgDE3DJ1whoX6dtqwYGZlDoJsEl0/pub?gid=1380420183&single=true&output=csv')
reader = csv.DictReader(submissions)
with open('submissions.json', 'w') as out:
  out.write(json.dumps([row for row in reader]))
