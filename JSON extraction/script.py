#written by Dylienne Every 2127946
#Department of Computer Sciences VU AMSTERDAM
#Master Thesis

import json
import pandas as pd
import numpy as np
import prov
from datetime import datetime
import calendar

#definition of contents
document = pd.read_json('Data/JSON/AFKPROV.json', orient='records')
# print(document)
Bundles = document["bundle"]
provenance = Bundles["result:provenance"]
elementoverview = list(provenance)
print(provenance)

# dataframe
df = pd.DataFrame(provenance)
# print(df.count())

#timestamp generation
def time_set(provenance):
    used = provenance['used']
    wasGeneratedBy = provenance['wasGeneratedBy']
    wasStartedBy = provenance["wasStartedBy"]
    timeset = dict(used, **wasGeneratedBy)
    timesetfunction = dict(timeset, **wasStartedBy)
    print(timesetfunction)

def list_time(provenance):
    for key, value in provenance.items():
        if key == 'wasGeneratedBy':
            for subkey, subvalue in value.items():
                times = []
                for sskey, ssvalue in subvalue.items():
                    if sskey == 'prov:time':
                            times.append(ssvalue)
                            print(times)
    return times

dateframe= pd.to_datetime(list_time(provenance)) #list

print(type(dateframe))


timeminmax = timeprov.iloc[0,-1]
elapstime = print(np.divide(timeminmax[0],timeminmax[1]))
meantimecommit =
print(type(timeprov))