def print__info(header, info):
    print(f"***********{header}***********")
    for key,value in info.items():
        print(f"{key} : {value}")
    print("***********End of information***********")
print__info("Using globals function",globals())
print(__name__)

if __name__ == "__main__":
    print("File name was changed to main")
else:
    print("Error!, Name not changed")
# __name__ == __main___
# whatever the file name is,
# python will convert it to __main__