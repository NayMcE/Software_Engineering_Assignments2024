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

def square_sum(*number):
    ttl = 0
    for num in number:
        ttl += num**0.5
    return int(ttl)

print(square_sum(1,2,2))

