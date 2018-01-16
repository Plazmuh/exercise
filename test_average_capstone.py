
# Global constant for a high/low score

HIGH_SCORE = 95
LOW_SCORE = 60


# Print "name" here are your results:, your average is: ,that is
# a good/bad grade.
def main(resultParam = "unknown"):
    print (resultParam)
    


# obtain users name 
def get_name(): 
    endUser = input("Please provide me your name: ")
    return endUser

endUserResponce = get_name()


# get input for three tests, and calculate average
def calc_grade():
    test1 = int(input("please provide test 1: "))
    test2 = int(input("Please give me test 2: "))
    test3 = int(input("Please give me test 3: "))
    average = (test1 + test2 + test3) / 3
    return average
                                                                                
    
vari = calc_grade()

def print_results(nameParam = "unknown", calcParam = "unknown"):
    # Print results of get_name, and calc_grade
    print ("%s" %endUserResponce, "here are your results:")
    print ("This is your average: %s" %vari)

    # Create if/else for average being less than/more than high/low score
    # Return to main
    if (vari >= HIGH_SCORE):
        print("Congratulations, that it a Great average!")
        
    elif (vari < LOW_SCORE):
        print("That is a failing grade.")
        print("better luck next time!")
        
        
print_results(endUserResponce, vari)

main(print_results)
