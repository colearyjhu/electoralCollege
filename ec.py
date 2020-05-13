import numpy as np
import sys

#state, margin, swingable EC votes(ME-SW = maine state wide(CD assumed 1 R 1 D), NE-2 = Nebraska 2nd)
states = { "MI": (-0.3,16),"WI": (-.7,10), "NH": (0.3,4), "PA": (-0.7,20),"FL":(-1.2,29),"MN":(1.5,10), "NV": (2.4,6),"ME-SW":(2.9,2), "NE-2":(-2.3,1), "NC":(-3.7,15), "AZ":(-3.6,11)}
states2024 =  { "MI": (-0.3,15),"WI": (-.7,10), "NH": (0.3,4), "PA": (-0.7,19),"FL":(-1.2,31),"MN":(1.5,9), "NV": (2.4,6),"ME-SW":(2.9,2), "NE-2":(-2.3,1), "NC":(-3.7,16), "AZ":(-3.6,12)}

nationalMargin2016 = 2
#totalEc = 0
demStates = 210
gopStates = 204
#tossup = 0
#for state in states:
#     tossup = tossup + states[state][1]  

dem2024 = 210
gop2024 = 203
#tossup = 0
#for state in states2024:
#     tossup = tossup + states2024[state][1]

def runSim(nationalMargin2020, noiseSigma):
  uniformSwing = nationalMargin2020 - nationalMargin2016
  demCount = 0
  dem2024Count = 0.0
  runs = 10000
  i = runs
  while i > 0:
    demWins = 0
    dem2024Wins = 0
    for state  in states:
      variant = np.random.normal(0,noiseSigma) + uniformSwing
      if (states[state][0] + variant) > 0:
        demWins += states[state][1]
        dem2024Wins += states2024[state][1]
    if(demStates + demWins >= 270):
      demCount = demCount + 1.0
    if(dem2024 + dem2024Wins >= 270):
      dem2024Count = dem2024Count + 1.0
    i = i -1
  #print("assuming random percentage swing of margin within state of < " + str(noiseSigma) + "% 2/3 of the time, twice that 95 percent of the time")
  #print("national margin is: " + str(nationalMargin2020))
  #print("demsWin percentage: " + str(demCount * 100 / runs ))
  #print("dems2024 percentage: " + str(dem2024Count * 100 / runs))
  return (demCount * 100 / runs)

nationalMargins = [2,3,4,5,6,7,8]
noiseSigmas = [1,2,3,4,5,6,7]
results = {} #[[0]* len(nationalMargins)]*len(noiseSigmas)
for ii in nationalMargins:
  for jj in noiseSigmas:
    results[ii,jj] = runSim(ii,jj)
    print (str(results[ii,jj]) + ", "),
  print(" ")
#print results
