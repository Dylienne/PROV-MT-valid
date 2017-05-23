#written by Dylienne Every 2127946
#Department of Computer Sciences VU AMSTERDAM
#Master Thesis

import json
import pandas as pd
import numpy as np
import prov
from datetime import datetime

#definition of contents
document = pd.read_json('Data/JSON/SJSPROV.json', orient='records')
print(document)
Bundles = document["bundle"]
provenance = Bundles["result:provenance"]
elementoverview = list(provenance)
print(provenance)

#pandas dataframe
df = pd.DataFrame(provenance)
print(df.count())

# timestamp

# def list_time(provenance):
#     for key, value in provenance.items():
#         if key == 'wasGeneratedBy':
#             for subkey, subvalue in value.items():
#                 for sskey, ssvalue in subvalue.items():
#                     if sskey == 'prov:time':
#                         print(ssvalue)
#
# timeprov = list_time(provenance)
# firsttime = datetime.strftime(timeprov[1,-1], '%Y-%m-%d 'T' '%H''
# lasttime = timeprov[1,-1]
# elaptime = datetime
# timeprov.sort
#
# recording = pd.read_xlsx('/Users/dylienneevery/Dropbox (Personal)/SimpliLegal/Thesis dnki/Provenance recoding.xlsx')
#

# to do: crreate bundle of used, wgb, wib
# compare if they differ
# get first and get last - calculate time
# calculate average time between commits
#



