from nis import match
import re
prefix_path = "./VOChisakawa/Annotations/"
for i in range(85):
  idx = i+1
  file_name = "IMG"+str(idx)
  with open(prefix_path+file_name+".xml", "r", encoding="UTF-8") as f:
    data = f.read()
    pattern = r'<filename>(.+?)</filename>'
    matched_list = re.findall(pattern, data)
    if len(matched_list) < 1:
      continue
    data = data.replace(matched_list[0], file_name+".jpg")
    f.close()
  with open(prefix_path+file_name+".xml", "w", encoding="UTF-8") as f:
    f.write(data)