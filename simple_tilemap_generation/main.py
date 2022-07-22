from random import choices
N = 9
N_iters = 3
column = N
line = N
start = 0
end = N-1
column_id = 1
line_id = 0
alive = 1
dead = 0
alive_population = [0, 1]
alive_weights = [0.3, 0.7]
# tilemap consists of tiles with attributes of [line, column]
tilemap = [[[iter_line,iter_col] for iter_col in range(column)] for iter_line in range(line)]
c_out = "tilemap:\n"
# for tile in tilemap:
#     c_out += str(tile) + "\n"
liveability = {}
for iter_line in range(line):
    for iter_tile in range(column):
        liveability[iter_line,iter_tile] = choices(alive_population, alive_weights)[0]
# c_out += "liveability:\n" + str(liveability) + "\n"
for tm_tile in tilemap:
    for tile in tm_tile:
        c_out += str(liveability[tile[line_id],tile[column_id]]) + " "
    c_out += "\n"

def get_neighbors(tile):
    neighbors = []
    for iter_line in range(3):
        lin = tile[line_id]-1+iter_line
        for iter_tile in range(3):
            if(iter_line==1 and iter_tile==1):
                continue
            col = tile[1]-1+iter_tile
            if(lin == -1):
                lin = end
            if(col == -1):
                col = end
            if(lin == N):
                lin = 0
            if(col == N):
                col = 1
            neighbors.append([lin,col])
    return neighbors
# tile = tilemap[0][1]
# c_out += "tile: " + str(tile) + "\nneighbors:" + str(get_neighbors(tile))
for i in range(N_iters):
    c_out += "tilemap #" + str(i+1) + ":\n"
    for tm_line in tilemap:
        for tile in tm_line:
            alive_neighbors = 0
            for elem in get_neighbors(tile):
                alive_neighbors += liveability[elem[line_id],elem[column_id]]
            cur_tile_liveability = liveability[tile[line_id],tile[column_id]]
            if(cur_tile_liveability == dead):
                if(alive_neighbors==2 or alive_neighbors==3):
                    liveability[tile[line_id],tile[column_id]] = alive
            elif(cur_tile_liveability == alive):
                if(alive_neighbors<2 or alive_neighbors>3):
                    liveability[tile[line_id],tile[column_id]] = dead
            c_out += str(liveability[tile[line_id],tile[column_id]]) + " "
        c_out +="\n"
print(c_out)