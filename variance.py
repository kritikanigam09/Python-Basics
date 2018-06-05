#To get the sum and average of items in a list

grades = [100, 100, 90, 50.5]

def grades_sum(scores):
    total = 0
    for x in scores:
        total += x
        return total
print(grades_sum(grades))

def grades_average(grades_input):
    
        average = grades_sum(grades_input)/len(grades_input)
        return average

print (grades_average(grades))

#To calculate variance

def grades_variance(scores):
    avg = grades_average(scores)
    variance = 0

    
    variance += avg**2
    total_variance = variance/len(scores)

    return total_variance

print(grades_variance(grades))

#To calulate standard deviation

def grades_std_deviation(variance):
    return variance**0.5

variance = grades_variance(grades)
print(grades_std_deviation(variance))

