'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def wordInRange():
    #Type your code here
    file_name = input()
    lower_bounds = input()
    upper_bounds = input()

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        for word in lines:
            word = word.strip()
            if word >= lower_bounds and word <= upper_bounds:
                print(f'{word} - in range')
            else:
                print(f'{word} - not in range')
    
    except FileNotFoundError:
        return
    return
if __name__ == '__main__':
    wordInRange()