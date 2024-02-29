
for i in range(3,100)
    flag = false
    for j in range(3,2,i-1)
        if i%j==0
            flag = true
        end
    end
        if flag == false
            println(i)
        else
            flag = false
        end
    print(RoundUp(sqrt(i-1)),1)
end