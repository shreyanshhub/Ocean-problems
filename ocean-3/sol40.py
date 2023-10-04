def generate_spiral():

    dir = ['R','U','L','D']
    k = 0 
    count = [1,1,2,2]
    spiral = ''

    while len(spiral) < 1000000:

        curr_dir = dir[k]
        curr_count = count[k]

        spiral = spiral + curr_dir*curr_count 

        count[k] += 2
        k = (k+1) % 4

    return spiral

print(generate_spiral())