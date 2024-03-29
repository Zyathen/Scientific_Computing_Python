def add_time(start, duration, week = None):

  #Parsing through the input strings

  #Parsing through start input
  length_start = len(start)
  time_of_day = start[length_start-2:length_start]
  #start_time[0] is hours, start_time[1] is minutes
  start_time = start[0:length_start-2].split(":")

  #Parsing through the duration input
  duration_time = duration.split(":")

  #Calculating the number of minutes
  mins = int(start_time[1]) + int(duration_time[1])
  if mins >= 60:
      hours = 1
      mins = mins - 60
  else: 
      hours = 0

  #Calculating the number of hours
  days = 0
  hours += int(duration_time[0])
  if hours >= 24:
      days = (hours // 24)
      hours = hours - (days * 24)
  #Determine the time of day, based on added hours
  hours += int(start_time[0])
  if hours >= 12:
      if time_of_day == "PM":
          time_of_day = "AM"
          days += 1
      else: 
          time_of_day = "PM"
      #If the combined hours equal 12, keep it, only change time of day
      if hours != 12:
          hours += -12


  #Formatting the new_time
  new_time = str(hours) + ":"
  if mins < 10:
      mins = "0" + str(mins)
  new_time += str(mins) + " " + time_of_day

  #If there is a day of the week listed
  if week != None:
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_of_week = -1
    #Matching the input week with the day of the week
    for i, day in enumerate(days_of_week):
      if (week[:2]).casefold() == day[:2].casefold():
          day_of_week = i
          break
        
    #Calculating what day of the week it is based on the added days     
    extra_days = (days - ((days // 7) * 7)) + day_of_week
    
    if extra_days > 6:
        week = days_of_week[extra_days - 7]
    else: 
        week = days_of_week[extra_days]
    new_time += ", " + week
  #Formatting the string
  if days == 1:
      new_time += " (next day)"
  elif days != 0: 
      new_time += " (" + str(days) + " days later)"

  return new_time