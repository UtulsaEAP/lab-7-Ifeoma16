'''
Name: Ifeoma Ogwu
Lab Time: Thursday, 2pm - 3:15pm
'''

def courseGrade():
    # TODO: Declare any necessary variables here. 
    total_students = 0
    total_midterm1 = 0
    total_midterm2 = 0
    total_finals = 0

    # TODO: Read a file name from the user and read the tsv file here. 
    file_name = input()

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # File 1
            if file_name == "./Problem 3/StudentInfo.tsv":
                output_file_name = f"./Problem 3/report.txt".replace("\\", "/")
                
                with open(output_file_name, 'w') as output_file:
                    for line in lines:
                        components = line.strip().split('\t')
                        if len(components) == 5:
                            last_name, first_name, midterm1, midterm2, final = components
                            midterm1, midterm2, final = map(int, [midterm1, midterm2, final])

                            average_score = (midterm1 + midterm2 + final) / 3
                            grade = ''

                            if average_score >= 90:
                                grade = 'A'
                            elif 80 <= average_score < 90:
                                grade = 'B'
                            elif 70 <= average_score < 80:
                                grade = 'C'
                            elif 60 <= average_score < 70:
                                grade = 'D'
                            elif average_score < 60:
                                grade = 'F'

                            output_file.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{grade}\n')

                            total_midterm1 += midterm1
                            total_midterm2 += midterm2
                            total_finals += final
                            total_students += 1

                    # Compute averages outside the loop
                    average_midterm1 = total_midterm1 / total_students
                    average_midterm2 = total_midterm2 / total_students
                    average_final = total_finals / total_students
                    output_file.write(f'\nAverages: midterm1 {average_midterm1:.2f}, midterm2 {average_midterm2:.2f}, final {average_final:.2f}')

            # File 2
            if file_name == "./Problem 3/StudentInfo1.tsv":
                output_file_name1 = f"./Problem 3/report1.txt".replace("\\", "/")
                
                with open(output_file_name1, 'w') as output_file1:
                    for line in lines:
                        components = line.strip().split('\t')
                        
                        last_name, first_name, midterm1, midterm2, final = components
                        midterm1, midterm2, final = map(int, [midterm1, midterm2, final])

                        average_score = (midterm1 + midterm2 + final) / 3
                        grade = ''

                        if average_score >= 90:
                            grade = 'A'
                        elif 80 <= average_score < 90:
                            grade = 'B'
                        elif 70 <= average_score < 80:
                            grade = 'C'
                        elif 60 <= average_score < 70:
                            grade = 'D'
                        elif average_score < 60:
                            grade = 'F'

                        output_file1.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{grade}\n')

                        total_midterm1 += midterm1
                        total_midterm2 += midterm2
                        total_finals += final
                        total_students += 1

                    # Compute averages outside the loop
                    average_midterm1 = total_midterm1 / total_students
                    average_midterm2 = total_midterm2 / total_students
                    average_final = total_finals / total_students
                    output_file1.write(f'\nAverages: midterm1 {average_midterm1:.2f}, midterm2 {average_midterm2:.2f}, final {average_final:.2f}')

            # File 3
            if file_name == "./Problem 3/StudentInfo2.tsv":
                output_file_name2 = f"./Problem 3/report2.txt".replace("\\", "/")
                
                with open(output_file_name2, 'w') as output_file2:
                    for line in lines:
                        components = line.strip().split('\t')
                        
                        last_name, first_name, midterm1, midterm2, final = components
                        midterm1, midterm2, final = map(int, [midterm1, midterm2, final])

                        average_score = (midterm1 + midterm2 + final) / 3
                        grade = ''

                        if average_score >= 90:
                            grade = 'A'
                        elif 80 <= average_score < 90:
                            grade = 'B'
                        elif 70 <= average_score < 80:
                            grade = 'C'
                        elif 60 <= average_score < 70:
                            grade = 'D'
                        elif average_score < 60:
                            grade = 'F'

                        output_file2.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{grade}\n')

                        total_midterm1 += midterm1
                        total_midterm2 += midterm2
                        total_finals += final
                        total_students += 1

                    # Compute averages outside the loop
                    average_midterm1 = total_midterm1 / total_students
                    average_midterm2 = total_midterm2 / total_students
                    average_final = total_finals / total_students
                    output_file2.write(f'\nAverages: midterm1 {average_midterm1:.2f}, midterm2 {average_midterm2:.2f}, final {average_final:.2f}')

    except FileNotFoundError:
        print("No file")
    except OSError as e:
        print(f"Error opening file: {e}")



if __name__ == "__main__":
    courseGrade()
    
    