import sys

def process_row_format(data):

    dict_format = {}
    data = data[1:len(data)]
    for line in data:
        line = line.split()
        sum = 0
 
        for i in range(len(line)):
            if i != 0:
                sum += int(line[i])
        res = sum / (len(line) - 1)
        dict_format[line[0]] = res 

    return dict_format


def process_column_format(data):
    dict_sum = {}
    dict_num = {}
    data = data[1:len(data)]
    
    for line in data:
        line = line.split()
        if line[0] in dict_sum:
            dict_sum[line[0]] = int(dict_sum.get(line[0])) + int(line[1])
            dict_num[line[0]] = int(dict_num.get(line[0])) + 1
        else:
            dict_sum[line[0]] = int(line[1])
            dict_num[line[0]] = 1

    for key in dict_sum:
        res = int(dict_sum.get(key)) / int(dict_num.get(key))
        dict_sum[key] = res

    return dict_sum

            
def main():
    inputname = sys.argv[1]
    outputname = sys.argv[2]
    data = []
    with open(inputname, "r") as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)


    if data[0] == "#Format:Column":
        with open(outputname, "w") as f:
            dictc = process_column_format(data)
            f.write(str(dictc) + "\n")
        
    else:
        with open(outputname, "w") as f:
            dictn = process_row_format(data)
            f.write(str(dictn) + "\n")


if __name__ == "__main__":
    main()