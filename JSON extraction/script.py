#written by Dylienne Every 2127946
#Department of Computer Sciences VU AMSTERDAM
#Master Thesis

import pandas as pd
from datetime import datetime
import os

#definition of contents
document = pd.read_json('Data/JSON/KOAPROV.json', orient='records')
# print(document)
Bundles = document["bundle"]
provenance = Bundles["result:provenance"]
elementoverview = list(provenance)


# dataframe
df = pd.DataFrame(provenance)

#timestamp generation

used = provenance['used']
wasGeneratedBy = provenance['wasGeneratedBy']
wasStartedBy = provenance["wasStartedBy"]
timeset = dict(used, **wasGeneratedBy)
timesetfunction = dict(timeset, **wasStartedBy)
print(timesetfunction)


def list_time(provenance):
    time =[]
    for key, value in provenance.items():
        if key == 'wasStartedBy':
            for subkey, subvalue in value.items():
                for sskey, ssvalue in subvalue.items():
                    if sskey == 'prov:time':
                            time.append({"time":ssvalue})
    return time

# def list_time2(timeset):
#     time = []
#     for key,value in timeset.items():
#         for skey, svalue in value.items():
#             if skey == 'time:prov':
#                 time.append({"time":svalue})
#                 print(time)
#     return time

# #timearithmetrics
timedf = list_time(provenance)
print(timedf)
df_time= pd.DataFrame.from_records(timedf)
print(df_time)
oldest = str(df_time.max())[0:18][-10:]
youngest = str(df_time.min())[0:18][-10:]
oldestobject = datetime.strptime(oldest, "%Y-%M-%d")
youngestobject = datetime.strptime(youngest, "%Y-%M-%d")
diff = oldestobject-youngestobject


#document
print(provenance)
print("------")
print(df.count())
print("------")
print(oldest)
print(youngest)
print("------")
print(diff)
