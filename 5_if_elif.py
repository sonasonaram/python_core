# student grade system
# 90+ => A+
# 80-90 => A
# 60-80 => B
# 40-60 => C
# <40 => D

marks = 95


if marks > 90:
    print("Grade: A+")
elif marks > 80 and marks <= 90:
    print("Grade: A")
elif marks > 60 and marks <= 80:
    print("Grade: B")
elif marks > 40 and marks <= 60:
    print("Grade: C")
else:
    print("Grade: D")


