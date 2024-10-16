for k in range(0,0)
    c = 0
    for i in range(1,step=2,1000000)
        flag = true
        for j in range(2,sqrt(i))
            if i % j == 0
                flag = false
                break
            end
        end
        if flag == true
            print(i) 
            c+=1
        end
    end
    println("c = ", c)
end