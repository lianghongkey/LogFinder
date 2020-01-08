import os
import time
import re

class Lines(object):
  def __init__(self, path=''):
    self.value = []
    if path:
      self.filepath = path
      self.file = open(path, "r")
      self.value = self.file.readlines()

  def Search(self, pattern):
    if isinstance(pattern,Lines):
      pattern = pattern.value
    if isinstance(pattern,list):
      l = Lines()
      for p in pattern:
        l.value+=([s for s in self.value if re.search(p,s)])
      return l
    else:
      l = Lines()
      l.value = [s for s in self.value if re.search(pattern,s)]
      return l
    
  def Cut(self, pattern):
    l = Lines()
    l.value = [s for s in self.value if not re.search(pattern,s)]
    return l

  def SearchEach(self, pattern):
    l = Lines()
    l.value=[]
    for s in self.value:
      searchout = re.search(pattern, s)
      if searchout:
        l.value.append(searchout.group(0))
    return l
  
  def IndexEach(self, startindex, endindex):
    l = Lines()
    l.value=[]
    for s in self.value:
      l.value.append(s[startindex:endindex])
    return l
  
  def CutEach(self, pattern):
    return self.ReplaceEach(pattern,"")
  
  def ReplaceEach(self, pattern, value):
    l = Lines()
    l.value=[]
    for s in self.value:
      searchout = re.sub(pattern, value, s)
      l.value.append(searchout)
    return l

  def CatEach(self, start, end):
    l = Lines()
    l.value = [start+s+end for s in self.value]
    return l

  def Deduplication(self):
    l = Lines()
    l.value = list(set(self.value))
    return l

  def Count(self):
    return len(self.value)

  def Save(self, path):
    f = open(path,'w')
    for s in self.value:
      if(re.search('\n',s)):
        f.write(s)
      else:
        f.write(s+'\n')
    # f.writelines(self.value)
    f.close()

  def ToRegular(self):
    l = Lines()
    l.value=[]
    for s in self.value:
      # l.value.append(s.replace('\\',"\\\\").replace('[',"\[").replace(']',"\]").replace('(',"\(")
      #   .replace('{',"\{").replace('}',"\)").replace('}',"\)").replace('|',"\|").replace('^',"\^")
      #   .replace('$',"\$").replace('+',"\+").replace('?',"\?").replace('.',"\.").replace('*',"\*")
      #   .replace('/',"\/").replace(')',"\)"))
      l.value.append(s.replace('\\',".").replace('[',".").replace(']',".").replace('(',".")
        .replace('{',".").replace('}',".").replace('}',".").replace('|',".").replace('^',".")
        .replace('$',".").replace('+',".").replace('?',".").replace('*',".")
        .replace('/',".").replace(')',".").replace('%',"."))
    return l

  def Append(self, value):
    self.value.append(value)
  
