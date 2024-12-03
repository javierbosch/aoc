file = io.open(arg[1], "r")

function half(str)
    local len = string.len(str)
    local half = math.floor(len / 2)
    return string.sub(str, 1, half), string.sub(str, half + 1)
end

function common_char(str1, str2)
    local common = ""
    for i = 1, #str1 do
        for j = 1, #str2 do
            if str1:sub(i, i) == str2:sub(j, j) then
                if not common:find(str1:sub(i, i)) then
                    common = common .. str1:sub(i, i)
                end
            end
        end
    end
    return common
end

function eval(c)
    local val = string.byte(c)
    if val > 96 then
        return val - 96
    else
        return val - 38
    end
end

io.input(file)

-- Part 1 --
t1 = 0
n = 0
for line in io.lines() do
    p1, p2 = half(line)
    c = common_char(p1, p2)
    t1 = t1 + eval(c)
    n = n + 1
end

file:seek("set",0)

-- Part 2 --
t2 = 0
for i=0, (n-1)/3 do
    line1 = io.read()
    line2 = io.read()
    line3 = io.read()
    c = common_char(line1, line2)
    c = common_char(c, line3)
    t2 = t2 + eval(c)
end

print("Part 1: " .. t1)
print("Part 2: " .. t2)

