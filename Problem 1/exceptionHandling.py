'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def exceptionHandling():
    try:
        # Split input into 2 parts: name and age
        parts = input().split()
        name = parts[0]
        while name != '-1':
            try:
                # FIXME: The following line will throw ValueError exception.
                #        Insert try/except blocks to catch the exception.
                age = int(parts[1]) + 1
                print(f'{name} {age}')
            except ValueError:
                print(f'{name} 0')
                
            # Get next line
            parts = input().split()
            name = parts[0]
    
    except IndexError:
        print()

if __name__ == '__main__':
    exceptionHandling()