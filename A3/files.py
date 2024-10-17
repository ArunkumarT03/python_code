import json
D={'rcb':7,'csk':6,'kkr':8}
with open('ipl.json','w') as fobj:
    content=json.dumps(D,indent=3)
    fobj.write(content)
d='hello everyone   hii vanakam'
with open('zoom.json','w')as fobj:
    con=json.dumps(d,indent=2)
    fobj.writelines(con)

d1=[2,3,2,1,2,1,1]
with  open('list1.json','w')as fobj:
    json.dump(d1,fobj,indent=4)
    
#loads
    
with open('ipl.json','r')as fobj:
    content=fobj.read()
    pythdata=json.loads(content)
    print(pythdata)

with open('list1.json','r')as fobj:
    pythondata=json.load(fobj)
    print(pythondata)
