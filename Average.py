def average(grades):
    total=0
    for grade in grades:
        total=total+grade
    avg = total/len(grades)
    return avg

def main():
    grades=[87,84,86,95,51]
    print(average(grades))
    return 0

main()