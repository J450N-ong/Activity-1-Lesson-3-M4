studentdata = {'id1':{'Name' : 'Jason'},'id2':{'Name' : 'Jevin'},'id3':{'Name' : 'Simon'},'id4':{'Name' : 'Garnold'}}

print(studentdata)

result = {}

for key, value in studentdata.items():
    if value not in result.values():
        result[key] = value

print(result)