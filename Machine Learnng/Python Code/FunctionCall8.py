class FindPercent:
    @staticmethod
    def percentage():
        # Define subject marks
        subject_marks = [98, 87, 95, 95, 93]
        
        # Calculate total marks
        total_marks = sum(subject_marks)
        total_subjects = len(subject_marks)
        
        # Calculate percentage
        percentage = (total_marks / (total_subjects * 100)) * 100
        
        # Print subject marks
        for i, mark in enumerate(subject_marks, start=1):
            print(f"Subject{i}= {mark}")
        
        # Print total marks and percentage
        print(f"Total : {total_marks}")
        print(f"Percentage : {percentage:}")
