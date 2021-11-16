def divide_and_conquer(a,b):
    num_1=a
    num_2=b
    num_1=str(num_1)
    num_2=str(num_2)
    if len(num_1)%2 != 0:
        num_1='0'+ num_1
    if len(num_2)%2 != 0:
        num_2='0'+ num_2

    out_1 = []
    while num_1:
        out_1.append(num_1[:2])
        num_1 = num_1[2:]

    out_2 = []
    while num_2:
        out_2.append(num_2[:2])
        num_2 = num_2[2:]

    final_out=[]
    count_1=len(out_1)
    for stg in out_1:
        stg=int(stg) 
        count_1 -= 1

        count_2=len(out_2)
        for stg_2 in out_2:
            stg_2=int(stg_2)
            count_2 -=1

            ans=stg*stg_2
            pwr=100**(count_1+count_2)
            ans=ans*pwr
            final_out.append(ans)
            sum=0
    for num in final_out:
        sum+=num
    return sum


print divide_and_conquer(123,1234567)
