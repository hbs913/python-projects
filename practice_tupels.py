visits = [ ("Acme Electric", "Yonkers", 450),
    ("Bright Wire", "Stamford", 120),
    ("Volt Co", "Yonkers", 300),
    ("Amp Bros", "Rye", 90),
    ("Current Kings", "Stamford", 610),]
#total_watts(visits) — returns the sum of all wattages. 1570 expected result

def total_watts(visits):
    total=0
    for name, town, w in visits:
        
        total+=w
    return total
    
result = total_watts(visits)
print (result)
        
#big_jobs(visits, threshold) — returns a list of the names of contractors whose job wattage is over the threshold.
#watts_by_town(visits) — returns a dictionary mapping each town to the total wattage quoted in that town.
#report_lines(visits) — returns a list of strings, one per visit, each formatted exactly like Acme Electric (Yonkers): 450 W.

def big_jobs(visits,threshold):
    above_thres=[]
    for name, town, w in visits:
        if w > threshold:
            above_thres.append(name)
    return above_thres

high_watt =  big_jobs(visits, 250)
print (high_watt)

#watts_by_town(visits) — returns a dictionary mapping each town to the total wattage quoted in that town. #{'Yonkers': 750, 'Stamford': 730, 'Rye': 90}

def watts_by_town (visits):
    new_dict={}
    for name, town, w in visits:
        if town in new_dict:
            new_dict[town] += w
        else:
            new_dict[town] = new_dict.get(town, 0) + w
    return new_dict

towns_watts= watts_by_town (visits)
print (towns_watts)




#report_lines(visits) — returns a list of strings, one per visit, each formatted exactly like Acme Electric (Yonkers): 450 W.

def report_lines(visits):
    lines = []
    for name, town, w in visits:
         lines.append(f"{name} ({town}): {w} W")
    return lines

report=report_lines(visits)
print (report)
