function sieve_of_atkin(limit)
    if limit < 2
        return []  # Handle limits below 2
    end

    # Initialize the sieve
    sieve = falses(limit)

    # Predetermine primes based on perfect squares
    sieve[2] = true
    sieve[3] = true

    sqrt_limit = Int(ceil(sqrt(limit)))

    # Invariants:
    # * 4x^2 + y^2 = n with n odd
    # * 3x^2 + y^2 = n with n odd
    # * 3x^2 - y^2 = n with x > y and n odd

    for x in 1:sqrt_limit
        for y in 1:sqrt_limit
            n = 4 * x^2 + y^2
            if n <= limit && (n % 12 == 1 || n % 12 == 5)
                sieve[n] = !sieve[n]
            end

            n = 3 * x^2 + y^2
            if n <= limit && n % 12 == 7
                sieve[n] = !sieve[n]
            end

            n = 3 * x^2 - y^2
            if x > y && n <= limit && n % 12 == 11
                sieve[n] = !sieve[n]
            end
        end
    end

    # Eliminate multiples of prime squares
    for r in 5:sqrt_limit
        if sieve[r]
            for i in r^2:r^2:limit
                sieve[i] = false
            end
        end
    end

    # Collect the primes
    primes = [2, 3]  
    for n in 5:limit
        if sieve[n]
            primes = push!(primes, n)
        end
    end

    return primes
end

sieve_of_atkin(100)