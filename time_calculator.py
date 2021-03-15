def add_time(start, duration,optional = None):
    start = start.split()
    required_time = ''
    duration = duration.split()
    data = start + duration
    data = [x.split(':') for x in data]
    day = ''
    #calculate the addition of minutes and hours
    minutes = int(data[0][1])+ int(data[2][1])
    hours = int(data[0][0])+ int(data[2][0])
    # checking if start is given in 12 hours system
    if int(data[0][0]) > 12 :
        return 'error! please input a 12 hour format starting time'
    # checking if minutes > 60 and adding 1 to hours then converting them to minutes
    if minutes > 60:
        hours += 1
        minutes -= 60
    if hours % 24 == 0:
        if hours == 24:
            number_of_days = 1
            hours = 12
            if data[1][0] == 'AM' :       
                data[1][0] = 'PM'
                required_time = f'{hours}:{minutes:02d} {data[1][0]}'
            elif data[1][0] == 'PM' :
                data[1][0] = 'AM'
            required_time = f'{hours}:{minutes:02d} {data[1][0]} (next day)'
        else:
            number_of_days = int(hours / 24)
            hours = 12
        if data[1][0] == 'AM' :       
                data[1][0] = 'PM'
        elif data[1][0] == 'PM' :
            data[1][0] = 'AM'
        required_time = f'{hours}:{minutes:02d} {data[1][0]} ({number_of_days} days later)'
    elif hours%24 == 12 or hours == 12:
        number_of_days = int(hours // 24)
        if data[1][0] == 'AM' :       
            data[1][0] = 'PM'
        elif data[1][0] == 'PM' :
            data[1][0] = 'AM'
    else:
        number_of_days = int(hours // 24)
    def time_calc():
        nonlocal hours
        nonlocal minutes
        nonlocal data
        nonlocal required_time
        nonlocal day
        nonlocal number_of_days
        if hours < 48 :
            if hours < 24:
                if hours <12 :
                    if optional != None:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day}'
                    else:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]}'
                elif hours > 12:
                    if data[1][0] == 'AM' :
                        hours -= 12        
                        data[1][0] = 'PM'
                        if optional != None:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day}'
                        else:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]}'
                    elif data[1][0] == 'PM' :
                        hours -= 12
                        data[1][0] = 'AM'
                        if optional != None:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} (next day)'
                        else:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]} (next day)'
                else:
                    if optional != None:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day}'
                    else:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]}'
            elif hours > 24:
                hours -= 24
                if hours <12 :
                    if optional != None:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} (next day)'
                    else:
                        required_time =  f'{hours}:{minutes:02d} {data[1][0]} (next day)'
                elif hours > 12:
                    if data[1][0] == 'AM' :
                        hours -= 12
                        data[1][0] = 'PM'
                        if optional != None:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} (next day)'
                        else:
                            required_time = f'{hours}:{minutes} {data[1][0]} (next day)'
                    elif data[1][0] == 'PM' :
                        hours -= 12
                        data[1][0] = 'AM'
                        if optional != None:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} (next day)' 
                        else:
                            required_time = f'{hours}:{minutes} {data[1][0]} (next day)'
                else:
                    if data[1][0]== 'AM':
                        if optional != None:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} ({number_of_days} days later)'
                        else:
                            number_of_days += 1
                            required_time = f'{hours}:{minutes:02d} {data[1][0]} ({number_of_days} days later)'
                    else:
                        if optional != None:
                            required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} (next day)'
                        else:    
                            required_time =  f'{hours}:{minutes:02d} {data[1][0]} (next day)'
        elif hours >= 48:
            hours -= 24*number_of_days
            hours = abs(hours)
            if hours <12 :
                if optional != None:
                    required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} ({number_of_days} days later)'
                else:   
                    required_time = f'{hours}:{minutes:02d} {data[1][0]} ({number_of_days} days later)'
            elif hours > 12:
                if data[1][0] == 'AM' :
                    hours -= 12        
                    data[1][0] = 'PM'
                    if optional != None:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} ({number_of_days} days later)'
                    else:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]} ({number_of_days} days later)'
                elif data[1][0] == 'PM' :
                    hours -= 12
                    data[1][0] = 'AM'
                    number_of_days += 1
                    if optional != None:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} ({number_of_days} days later)'
                    else:
                        required_time = f'{hours}:{minutes:02d} {data[1][0]} ({number_of_days} days later)'
            else:
                if optional != None:
                    required_time = f'{hours}:{minutes:02d} {data[1][0]}, {day} ({number_of_days} days later)'
                else:
                    required_time = f'{hours}:{minutes:02d} {data[1][0]} ({number_of_days} days later)'
    if optional != None:
        days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
        if hours > 48:
            if hours%24 > 12:
                if data[1][0] == 'PM' :
                    number_of_days += 1
                    data[1][0] = 'AM' 
        if hours == 12 or hours%24 == 12:
            if data[1][0]== 'AM':
                number_of_days += 1  
        if optional.upper() in days:
            index = days.index(optional.upper()) + 1 
            if number_of_days > 7:
                index_of_the_calc_date = number_of_days % 7
                index_of_date_required = index + index_of_the_calc_date
                if index_of_date_required > 7:
                    index_of_date_required -= 7
            elif number_of_days == 7:
                index_of_date_required = index
            else:
                index_of_the_calc_date = number_of_days
                index_of_date_required = index + index_of_the_calc_date
                if index_of_date_required > 7:
                    index_of_date_required -= 7
            day = days[index_of_date_required-1].capitalize()
            time_calc()
    else:
        time_calc()            
    return required_time  
print(add_time("11:59 PM", "24:05",'wednesday'))