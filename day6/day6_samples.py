# with open("sample.text","r") as file:
#     # content=file.readline()
#     # print(content)
    
#     file.write("hello world")
#     file.writelines("alice","bob","cheery")
    
    
    
#file is automatically closed



try:
    with open("sample.text","r") as file:
        content=file.read()
except FileNotFoundError:
    print("File not found")