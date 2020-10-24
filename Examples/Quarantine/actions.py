def get_virus_areas(grid):
    areas = []
    dangers = []
    walls = []
    color = [[0] * n for i in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and color[i][j] == 0:
                area = [(i, j)]
                danger = set()
                wall = 0
                Q = [(i, j)]
                color[i][j] = 1
                while Q:
                    s, t = Q.pop(0)
                    for ii, jj in adj(s, t):
                        if grid[ii][jj] == 1 and color[ii][jj] == 0:
                            color[ii][jj] = 1
                            Q.append((ii, jj))
                            area.append((ii, jj))
                        if grid[ii][jj] == 0:
                            wall += 1
                            danger.add((ii, jj))
                areas.append(area)
                dangers.append(danger)
                walls.append(wall)
    return areas, dangers, walls


def spread_grid(grid):
    areas, dangers, walls = get_virus_areas(grid)
    def spread(dangers):
        for danger in dangers:
            for i, j in danger:
                grid[i][j] = 1

    dangerest_i = 0
    n_area = len(areas)
    for i in range(n_area):
        if len(dangers[i]) > len(dangers[dangerest_i]):
            dangerest_i = i
    spread(dangers[:dangerest_i] + dangers[dangerest_i + 1:])