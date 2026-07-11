file =input("输入文件路径")
if file.startswith('"') and file.endswith('"'):
    file=file[1:-1]
elif file.startswith("'") and file.endswith("'"):
    file=file[1:-1]
with open(file,'r',encoding='UTF-8') as f:
    context=f.read().split()
    content={}
    for i in context:
        content[i]=content.get(i,0)+1
    print(content)