"""
Numeros The Artist was arranging two identical lists A and B into specific orders. The arrangements of the two arrays were random, Numeros was very proud of his arrangements. Unfortunately, some numbers got left out of List A. Can you find the missing numbers from A without messing up his order?
"""
def lister():
    lista = []
    listb = []
    listc = []
    num = input()
    for i in range(0, num):
        lista.append(input())
    num2 = input()
    for i in range(0, num2):
        temp = input()
        listb.append(temp)
	print lista.count(temp)
	print listb.count(temp)
        if(lista.count(temp) < listb.count(temp)):
	    listc.append(temp)
            print listc
	
    print ' '.join(sorted(listc))

def main():
    lister()
if __name__ == "__main__":
    main()
