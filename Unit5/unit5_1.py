def read_txt_file(filepath)
    with open("./input.txt",'r') as f:
        data = f.readlines()
    return data

def main() :
    text_data = read_txt_file("./input.txt")
    print('data from inout:', text_data[0])
    print('data from input:', text_data[1])
    print('data from input:', text_data[2])
main()

def sums_of_2nd_col(input_data):
    for line in input_data:
        index = 0 
        counter = 0
        firstCounter = 0
        secondCounter = 0
        for char in line:
            index += 1
            if char == ' ':
                if counter == 0
                    firstCounter = index
                    counter += 1
                elif counter == 1:
                    secondCounter = index
                    break
        secondNumber = line[firstCounter:secondCounter]
        sum = sum + secondNumber
        print('second number:', secondNumber)

 
def sums(input_data):
    # looping through one line at a line      
    sum = 0
    for line in input_data:
        print('line:', line)
        # at each line i want to extrCT THE
        # first number number
        # LINEAR SEARCH to search for the index of space character
        counter = 0
        for char in line:
            counter += 1
            if char == ' ':
                break

        first_number_str = line[0:counter] 
        first_num_int = int(first_number_str)
        sum = sum + first_num_int
        print('first_number:', first_number_str)  
        print('===========')  

    print('sum:', sum)                                                                                

def main():
    text_data = read_txt_file("input.txt")
    print('line 691 data:', text_data[690])
    sum(text_data)
