# There was a test in your class and you passed it. Congratulations!
#
# But you're an ambitious person. You want to know if you're better than the average student in your class.
#
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return true if you're better, else false!
#
# Note:
# Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

def better_tan_average(class_points, your_points):
    class_points = [12,15,15,10,12,18,20]
    average_class_points = sum(class_points) / len(class_points)
    return average_class_points
    your_points =