import json
import shutil # for making file copy and renaming

workdingDir = "/Users/<your_name>/folder/"
templateForm = workingDir + "template.pdf"

with open('source.json') as f:
    data = json.load(f)

for doc in data:
   
   outputForm = workingDir + doc["fileName"]

   fileName = doc["fileName"].replace("(", "\\(")
   fileName = fileName.replace(")", "\\)")
   field1 = doc["field1"].replace("(", "\\(")
   field1 = field1.replace(")", "\\)")
   field2 = doc["field2"].replace("(", "\\(")
   field2 = field2.replace(")", "\\)")
   field3 = doc["field3"].replace("(", "\\(")
   field3 = field3.replace(")", "\\)")
   field4 = doc["field4"].replace("(", "\\(")
   field4 = field4.replace(")", "\\)")

   formContent = "<</F(" \
                  + fileName \
                  + ")/Fields[<</T(field1)/V(" \
                  + field1 \
                  + ")>><</T(field2)/V(" \
                  + field2 \
                  + ")>><</T(field3)/V(" \
                  + field3 \
                  + ")>><</T(field4)/V(" \
                  + field4 \
                  + ")>>]/UF(" \
                  + fileName \
                  + ")>>"

   print("Making " + outputForm)
   shutil.copy("templateForm", "outputForm")

   with open(workingDir + doc["fileName"].replace("pdf", "fdf"), 'a+') as fileo:
      print("Producing " + doc["fileName"].replace("pdf", "fdf"))
      fileo.write("%FDF-1.2%\n1 0 obj\n<</FDF\n" + formContent + "\n/Type/Catalog>>\nendobj\ntrailer\n<</Root 1 0 R>>\n%%EOF")
