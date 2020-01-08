import os
import LogObject

import re


# f  = LogObject.Lines("/home/colin/Dump1.14_2/140317094421296_executable_graph.dot")
# f.value[0]="* . ? + $ ^ [ ] ( ) { } | \ /"
# replace = f.ToRegular()

# ss = f.Search(["Executor40","Executor41"])
# sub = ss.SearchEach("Executor\d\d")

# de = sub.Deduplication()

# cat  = de.CatEach("colin_","_sub")

# count = cat.Count()





g14 = LogObject.Lines("/home/colin/Dump1.14_2/140317094421296_executable_graph.dot")
g8 = LogObject.Lines("/home/colin/Dump1.8/139913242459680_executable_graph.dot")

# log14 = LogObject.Lines("/home/colin/tf1.14.log")
# log8 = LogObject.Lines("/home/colin/tf1.8.log")
# log14 = log14.Search("\[OPID\] \d\d\d\d kernel")
# log14 = log14.SearchEach("\[OPID\].*")
# log14 = log14.CutEach("\.\d{1,5}")
# log8 = log8.Search("\[OPID\] \d\d\d\d kernel")
# log8 = log8.SearchEach("\[OPID\].*")
# log8 = log8.CutEach("\.\d{1,5}")
# log14.Save("log14.log")
# log8.Save("log8.log")

log14 = LogObject.Lines("log14.log")
log8 = LogObject.Lines("log8.log")



opid14 = g14.SearchEach("_opid\d{1,4}")
opid14 = opid14.SearchEach("\d{1,4}")
opid14 = opid14.Deduplication()

opid8 = g8.SearchEach("_opid\d{1,4}")
opid8 = opid8.SearchEach("\d{1,4}")
opid8 = opid8.Deduplication() 



result = LogObject.Lines()

for opid in opid14.value:
  kernel = log14.Search("\[OPID\] "+str(opid)+" kernel").SearchEach("\[OPID\].*").SearchEach("\%.*")

  kernel = kernel.SearchEach("\%[^\)]*.")
  kernel = kernel.CutEach("\.\d{1,5}")
  kernel = kernel.ToRegular()
  kernel = kernel.IndexEach(0,100)

  opidfind8 = log8.Search(kernel)
  if opidfind8.value:
    opidfind8 = opidfind8.SearchEach("\[OPID\] \d{1,4}").SearchEach("\d{1,4}")
    opidfind8 = opidfind8.Search(opid8).CatEach("_opid","")

    if opidfind8.value:
      opidfind8.value = opidfind8.value[0]

      items14 = g14.Search("_opid"+opid)
      items8 = g8.Search(opidfind8)

      # if items14.Count() == 9:
      #   fdafd=0

      result.Append("1.14:1.08 : "+ str(items14.Count()) + ":"+ str(items8.Count()) + "  opid14:"+ str(opid) +"  kernel114 : "+kernel.value[0])

result.Save("result.log")

gafd = 32
