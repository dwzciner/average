import os
import re 

filepath = input("enter filepath")
test_result = "test_result.log"
avg_test_result = "max_test_result.log"
full_test_result = os.path.join(filepath, test_result)
full_avg_test_result = os.path.join(filepath, avg_test_result)

acc = []
avg_acc = []
with open(full_test_result, 'r') as file:
    lines = file.readlines()
    for line in lines:
        clean_s = re.sub(r'\x1b\[[0-9;]*m', '',line.split()[-1])
        acc.append(float(clean_s))

acc10 = max(acc[:50])
acc50 = max(acc[50 : 100])
acc100 = max(acc[100:150])
acc200 = max(acc[150:200])
acc600 = max(acc[200:250])

with open(full_avg_test_result, 'w') as file:
    file.write(f"classes : 10  max test acc: {acc10}\n")
    file.write(f"classes : 50  max test acc: {acc50}\n")
    file.write(f"classes : 100  max test acc: {acc100}\n")
    file.write(f"classes : 200  max test acc: {acc200}\n")
    file.write(f"classes : 600  max test acc: {acc600}\n")
