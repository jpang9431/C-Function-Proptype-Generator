f = open(input("Enter the file path: "), "r")

keywordList = ["char", "int", "float", "void", "short", "long", "signed", "unsigned"]


def valInList(val, lst):
  for i in lst:
    if val == i:
      return True
  return False


def createProptype(lineList):
  proptype = ""
  index = 0
  while "(" not in proptype:
    proptype += " " + lineList[index]
    index += 1
  proptype+=" "
  wasSpecial = "struct" in lineList[index-1]
  if ")" in proptype:
    proptype = proptype[:-1]
    proptype+=";"
    return proptype
  while index < len(lineList):
    if "[" in lineList[index]:
      proptype = proptype[:-1]
      proptype += "[]"
    if wasSpecial:
      proptype += lineList[index]
      wasSpecial = False
    elif "," in lineList[index]:
      if (proptype[-1]==" "):
        proptype = proptype[:-1]
      proptype += ","
    elif valInList(lineList[index], keywordList):
      proptype += lineList[index]
    elif lineList[index] == "struct":
      proptype += lineList[index]
      wasSpecial = True
    elif ")" in lineList[index]:
      if proptype[-1] == " ":
        proptype = proptype[:-1]
      break
    proptype += " "
    index += 1
  proptype += ");"
  return proptype


for line in f:
  lineList = line.split(" ")
  if (lineList[-1] == "{\n"
      and (valInList(lineList[0], keywordList) or lineList[0] == "struct")):
    print(createProptype(lineList)[1:])
