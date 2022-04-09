import numpy


def run():
    q = int(input("Введите длину q "))
    answer = task(q)
    print(f"Количество подходящих значений: {answer}")

def task(q):
    if not isinstance(q,int):
        raise TypeError
    if q<1 or q > pow(10,14):
        raise ValueError

    answers = 0
    for p in range(q+1,pow(q,2)):
        start = 1
        sum_p=-1
        sum_q=0
        while sum_p < sum_q:
            sum_p = numpy.sum([x for x in range(start,p+start)])
            sum_q = numpy.sum([x for x in range(p+start,p+start+q)])
            if sum_p == sum_q:
                answers+=+1
            start+=1
    return answers

if __name__ == '__main__':
    run()