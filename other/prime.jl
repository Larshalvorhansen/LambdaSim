isP = true
lim = 1000

for i in 3:2:lim
    isP = true
    for j in 2:floor(Int, sqrt(i))
        if i % j == 0
            isP = false
            break
        end
    end
    if isP
        println(i)
    end
end