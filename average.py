import os

filepath = input("enter filepath")
test_result = "test_result.log"
avg_test_result = "avg_test_result.log"
full_test_result = os.path.join(filepath, test_result)
full_avg_test_result = os.path.join(filepath, avg_test_result)

acc = []
avg_acc = []
with open(full_test_result, 'r') as file:
    lines = file.readlines()
    for line in lines:
        acc.append(float(line.split()[-1]))

acc10 = sum(acc[:50]) / 50
acc50 = sum(acc[50 : 100]) / 50
acc100 = sum(acc[100:150]) / 50
acc200 = sum(acc[150:200]) / 50
acc600 = sum(acc[200:250]) / 50

with open(full_avg_test_result, 'w') as file:
    file.write(f"classes : 10  test acc: {acc10}\n")
    file.write(f"classes : 50  test acc: {acc50}\n")
    file.write(f"classes : 100  test acc: {acc100}\n")
    file.write(f"classes : 200  test acc: {acc200}\n")
    file.write(f"classes : 600  test acc: {acc600}")
