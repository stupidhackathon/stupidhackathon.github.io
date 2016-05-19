import csv
import json
import urllib2


def youtube_time_to_seconds(time_str):
  """Transform format HH:MM:SS to seconds"""
  if not time_str:
    return None
  time = [int(s) for s in time_str.split(':')]
  time.reverse()
  if len(time) > 3:
    raise Exception('Cannot parse time with greater units than hours: %s',
                    time_str)
  if len(time) == 0:
    raise Exception('Nothing here: %s', time_str)

  seconds = time[0]
  if len(time) > 1:
    seconds += time[1] * 60
  if len(time) > 2:
    seconds += time[2] * 3600
  return seconds


SUBMISSIONS_CSV_URL = 'https://docs.google.com/spreadsheets/d/1HwdQudacNaRwfjcqgDE3DJ1whoX6dtqwYGZlDoJsEl0/pub?gid=1380420183&single=true&output=csv'
submissions = urllib2.urlopen(SUBMISSIONS_CSV_URL)
reader = csv.DictReader(submissions)
with open('submissions.json', 'w') as out:
  # Transform some cols
  rows = []
  for row in reader:
    print row
    if row.get('video_start'):
      row['video_start'] = youtube_time_to_seconds(row['video_start'])
    if row.get('video_end'):
      row['video_end'] = youtube_time_to_seconds(row['video_end'])
    rows.append(row)
  # Dump to json
  out.write(json.dumps(rows))
