import math


def getHoursMinutesSeconds(totalSeconds):
  totalHours = totalSeconds//3600
  totalMinutes = math.floor((totalSeconds/3600-totalSeconds//3600)*60)
  totalSeconds = round((totalSeconds/60-totalSeconds//60)*60)

  if totalSeconds == 0 and totalHours == 0 and totalMinutes == 0:
    output='0s'
  else:
    output=[]
    if totalHours > 0:
      totalHours = str(totalHours)+'h'
      output.append(totalHours)
    if totalMinutes > 0:
      totalMinutes = str(totalMinutes)+'m'
      output.append(totalMinutes)
    if totalSeconds > 0:
      totalSeconds = str(totalSeconds) +'s'
      output.append(totalSeconds)
  if output == '0s':
    output=output
  elif len(output) > 1:
    output=' '.join(output)
  else:
    output=''.join(output)
  return(output)

print(getHoursMinutesSeconds(0))

  

assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'
