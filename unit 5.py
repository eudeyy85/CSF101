def read_txt_file(filepath):
    data=[]
    with open("./input.txt",'r') as f:
          data = f.readlines()
    return data

#task 3
def sums():
     print('sum function called')
     print('testing input dta 1:',input_data[0])
     print('testing input dta 1:',input_data[1])
     print('testing input dta 1:', input_data[2])
sums('input_data')

def main():
     #task 1:Reading txt file
     text_data = read_txt_file("./input.txt")
     #task 2
     print('line 691 data', text_data[690])
     sums(text_data)
main()