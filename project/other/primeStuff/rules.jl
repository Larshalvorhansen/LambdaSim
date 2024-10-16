using Plots

function ruleToBinary(ruleNumber)
    binaryRule = zeros(Bool, 8)
    for i in 1:8
        binaryRule[i] = ((ruleNumber >> (i - 1)) & 1) == 1
    end
    return reverse(binaryRule)
end

function applyRule(grid, ruleBinary)
    newGrid = copy(grid)
    for i in 2:length(grid)-1
        neighborhood = (grid[i-1] << 2) + (grid[i] << 1) + grid[i+1]
        newGrid[i] = ruleBinary[neighborhood + 1]
    end
    return newGrid
end

function generateCA(ruleNumber, generations, width)
    ruleBinary = ruleToBinary(ruleNumber)
    grid = zeros(Bool, width)
    grid[Int(ceil(width / 2))] = true
    
    cellular_automaton_data = zeros(Bool, generations, width)

    for gen in 1:generations
        cellular_automaton_data[gen, :] = grid
        grid = applyRule(grid, ruleBinary)
    end

    heatmap(cellular_automaton_data, color=:grays, yflip=true) 
end

# Example usage: Rule 30 for 40 generations with a width of 50 cells
 
for i in 1:10
    generateCA(i, 40, 50)
end
