import bisect
def test_list():
    li= [1,2,3,4,4,4,6,7,]
    print ("The rightmost index to insert, so list remains sorted is  : ", end="")
    print (bisect.bisect(li, 5))
test_list()
