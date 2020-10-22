"""
    Every night, the virus spreads to all neighboring cells in all four
    directions unless blocked by a wall. Resources are limited. Each day,
    you can install walls around only one region -- the affected area
    (continuous block of infected cells) that threatens the most
    uninfected cells the following night. There will never be a tie.

    Can you save the day? If so, what is the number of walls required?
    If not, and the world becomes fully infected, return the number of walls used.

    1. The number of rows and columns of grid will each be in the range [1, 50]
    2. Each grid[i][j] will be either 0 or 1.
    3. Throughout the described process, there is always a contiguous viral
        region that will infect strictly more uncontaminated squares in
        the next round.
"""

# 112 ms
class bfs_contain_algo(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def adj(i, j):
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < m and 0 <= jj < n:
                    yield ii, jj

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

        def spread(dangers):
            for danger in dangers:
                for i, j in danger:
                    grid[i][j] = 1

        wall_count = 0
        areas, dangers, walls = get_virus_areas(grid)
        while areas:
            # 如果全是感染区，返回
            n_area = len(areas)
            if sum(len(area) for area in areas) == m * n:
                return wall_count

            # 获取危险点最多的区域
            dangerest_i = 0
            for i in xrange(n_area):
                if len(dangers[i]) > len(dangers[dangerest_i]):
                    dangerest_i = i

            # 建墙，统计墙数，将对应感染区变为安全区
            wall_count += walls[dangerest_i]
            for i, j in areas[dangerest_i]:
                grid[i][j] = -1

            # 其他感染区扩散
            spread(dangers[:dangerest_i] + dangers[dangerest_i + 1:])

            # 重新获取感染区
            areas, dangers, walls = get_virus_areas(grid)

        return wall_count

class dfs_contain_algo(object):
    def containVirus(self, grid):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def cells():
            for r in range(R):
                for c in range(C):
                    yield (r, c)

        def is_valid(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbours(r, c):
            """Get valid neighbour cells"""
            for dr, dc in dirs:
                if is_valid(r + dr, c + dc):
                    yield (r + dr, c + dc)

        def pick_most_threatening_region():
            visited = set()

            def dfs(r, c):
                """Returns number of walls needed to quarantine infected region
                starting at (r,c)"""
                # Avoid already visited or quarantined cells.
                if (r, c) in visited or grid[r][c] == -1:
                    return 0
                # Found an empty perimeter space
                if grid[r][c] == 0:
                    perimeter.add((r, c))
                    # Counts as one wall needed to contain infected cell.
                    return 1

                visited.add((r, c))
                # Explore neighbours and return the sum of the walls needed to
                # contain their perimeter.
                return sum(dfs(nr, nc) for (nr, nc) in neighbours(r, c))

            max_perimeter, max_p_walls, max_start = 0, 0, (0, 0)
            for r, c in cells():
                # Find cells that have not yet been visited and are infected.
                if (r, c) not in visited and grid[r][c] == 1:
                    perimeter = set()
                    # Get the total walls needed to quarantine the infected region.
                    walls = dfs(r, c)
                    # If the parameter we could save is the biggest we've seen...
                    if len(perimeter) > max_perimeter:
                        # update the walls needed to quarantine, and an infected cell
                        # from which we might mark the infected region as quarantined (setting -1)
                        max_perimeter, max_p_walls, max_start = len(perimeter), walls, (r, c)
            return max_p_walls, max_start

        def quarantine(r, c):
            """Mark an infected region as quarantined by setting cells to -1"""
            grid[r][c] = -1
            # Explore neighbours to quarantine them too.
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == 1:
                    quarantine(nr, nc)

        def simulate_night():
            """Spreads the infection by one night of non-quarntined regions."""

            def infected_neighbour(r, c):
                """Returns True if an orthogonally adjacent square is infected."""
                return any(grid[nr][nc] == 1 for nr, nc in neighbours(r, c))

            for r, c in cells():
                # Find clean cells that are next to infected cells
                if grid[r][c] == 0 and infected_neighbour(r, c):
                    # Set them temporarily to 2, so that further iterations do not
                    # count them as infected (otherwise it would spread endlessly
                    # in one night).
                    grid[r][c] = 2

            # Go over a second time and set the temporarily marked newly infected cells
            # to permanently infected.
            for r, c in cells():
                if grid[r][c] == 2:
                    grid[r][c] = 1

        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])

        walls = 0
        while True:
            new_walls, (r, c) = pick_most_threatening_region()
            # Stop when there are no more infected regions, i.e. only
            # -1 (quarantined by us) and 0's are left.
            if new_walls == 0:
                return walls
            quarantine(r, c)
            walls += new_walls
            simulate_night()
        return walls