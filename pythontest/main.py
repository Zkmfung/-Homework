"""
0.0：
1. 设计了城市
2. 设计了火车线路的时刻表与价格表
3. 设计了Floyd基本算法

1.0 update:
1. 将火车时刻用开始时间和结束时间表示
2. 在Floyd算法中添加了换乘时间的判断
3. 最短时间和最少价钱分开处理
4. 根据计算的最短路径得到相应时间和价钱
5. 进行了基础功能测试

1.1 update:
1. 删除城市时在时刻表和价格表中删除对应路线
2. 根据价格计算总时间加上了换乘时间的计算
3. 增加了每段路径的时间和价格显示
4. 对线路的添加和删除进行了城市限制
5. 解决了到达城市可能没有出发线路导致报错的问题

2.0 update:
1. 实现了交互界面
2. 加入了飞机的算法

3.0 update:
1. 将Floyd算法改为适用于多重图的Dijkstra算法，实现了两个城市之间有多条路线的计算
2. 对所有函数进行了相应修改
"""

import heapq

cities = list()  # 城市存储


def show_city():  # 查看城市
    print(cities)


def add_city(new_city):  # 添加城市
    if new_city in cities:  # 城市已存在，跳过
        print(f"{new_city}已存在")
    else:  # 城市不存在，添加
        cities.append(new_city)
        print(f"{new_city}已添加")


def delete_city(del_city):  # 删除城市
    if del_city not in cities:  # 城市不存在，跳过
        print(f"{del_city}不存在")
    else:  # 城市已存在，删除
        cities.remove(del_city)
        del train_time[del_city]  # 时刻表中删除
        for city in train_time:
            train_time[city].pop(del_city, None)
        del train_cost[del_city]  # 价格表中删除
        for city in train_cost:
            train_cost[city].pop(del_city, None)
        print(f"{del_city}已删除")


train_time = dict()  # 火车时刻表
train_cost = dict()  # 火车价格表


def show_train_time():  # 查看火车时刻表
    print(train_time)


def show_train_cost():  # 查看火车价格表
    print(train_cost)


def add_train(start_city, end_city, start_time, end_time, cost):  # 添加火车线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法添加")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法添加")
        return None
    if start_city not in train_time.keys():
        train_time[start_city] = dict()
        train_cost[start_city] = dict()
    if end_city not in train_time[start_city].keys():
        train_time[start_city][end_city] = list()
        train_cost[start_city][end_city] = list()
    if end_city not in train_time.keys():
        train_time[end_city] = dict()
        train_cost[end_city] = dict()
    if (start_time, end_time) in train_time[start_city][end_city]:
        index = list()
        i = 0
        while i < len(train_time[start_city][end_city]):
            if train_time[start_city][end_city][i] == (start_time, end_time):
                index.append(i)
            i += 1
        for x in index:
            if train_cost[start_city][end_city][x] == cost:
                print("该线路已存在，无法添加")
                return None
    train_time[start_city][end_city].append((start_time, end_time))  # 两个时间均采用hhmm格式
    train_cost[start_city][end_city].append(cost)


def delete_train(start_city, end_city, start_time, end_time, cost):  # 删除火车线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法删除")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法删除")
        return None
    time_index = list()
    i = 0
    while i < len(train_time[start_city][end_city]):
        if train_time[start_city][end_city][i] == (start_time, end_time):
            time_index.append(i)
        i += 1
    cost_index = list()
    j = 0
    while j < len(train_time[start_city][end_city]):
        if train_cost[start_city][end_city][j] == cost:
            cost_index.append(j)
        j += 1
    index = [elem for elem in time_index if elem in cost_index]  # 得到同时符合时间和价格的车次下标
    train_time[start_city][end_city].pop(index[0])
    if not train_time[start_city][end_city]:  # 如果出发城市没有通往到达城市的线路，在字典中删除
        del train_time[start_city][end_city]
    if not train_time[start_city]:  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del train_time[start_city]
    train_cost[start_city][end_city].pop(index[0])
    if not train_cost[start_city][end_city]:  # 如果出发城市没有通往到达城市的线路，在字典中删除
        del train_cost[start_city][end_city]
    if not train_cost[start_city]:  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del train_cost[start_city]


INF = float('inf')


def train_time_decision(start_city, end_city):  # 火车最短时间
    distances = {node: INF for node in train_time}  # 距离初始化为无穷
    previous_nodes = {node: None for node in train_time}  # 经过节点初始化为空，Key为前驱，Value为后继
    distances[start_city] = 0  # 起点到起点的距离为0
    priority_queue = [(0, start_city)]  # 初始化优先队列
    prev_node = start_city  # 前驱节点初始化为起点
    prev_path = {node: {node: list() for node in train_time} for node in train_time}  # 前驱路径初始化为空列表
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)  # 取队首最小值
        if curr_distance > distances[curr_node]:  # 距离大于已有距离说明已经优化，跳过
            continue
        for neighbor, all_times in train_time[curr_node].items():  # neighbor为相邻节点，all_times为两个节点之间的所有车次时间
            all_costs = train_cost[curr_node][neighbor]
            all_weights = list()
            i = 0
            while i < len(all_times):  # 遍历所有车次，得到时间权重
                if curr_node == start_city:  # 当前节点为起点，没有换乘时间，直接计算车次时长
                    weight = all_times[i][1] - all_times[i][0]
                elif curr_node != start_city:  # 当前节点不是起点，权重为换乘时间+车次时长
                    weight = all_times[i][1] - prev_path[prev_node][curr_node][1]
                    if all_times[i][0] - prev_path[prev_node][curr_node][1] < 100:  # 换乘时间小于100，不满足条件，跳过
                        weight = INF
                all_weights.append(weight)  # 将计算的权重加入所有权重
                i += 1
            all_locates = [0]  # 下标定位列表
            min_weight = INF
            j = 0
            while j < len(all_weights):
                if all_weights[j] <= min_weight:
                    min_weight = all_weights[j]  # 取最小权重
                    if j != 0:
                        # 下标列表中要么只有1个元素，要么所有元素对应的权重相同，和第1个元素比较，若不相等则清空列表
                        if all_weights[j] <= all_weights[all_locates[0]]:
                            if all_weights[j] < all_weights[all_locates[0]]:
                                all_locates.clear()
                            all_locates.append(j)
                j += 1
            distance = curr_distance + min_weight  # 距离更新为当前距离+最小权重
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = curr_node
                min_cost = INF
                locate = None
                for x in all_locates:  # 遍历所有定位，得到价格最低的车次下标
                    x_cost = all_costs[x]
                    if x_cost < min_cost:
                        min_cost = x_cost
                        locate = x
                prev_path[curr_node][neighbor] = all_times[locate]  # 把当前节点到相邻节点的车次更新为最小权重对应的最低价格车次
                prev_node = curr_node
                heapq.heappush(priority_queue, (distance, neighbor))
    path = list()
    path_node = end_city
    while path_node is not None:  # 得到经过城市的倒序排列
        path.append(path_node)
        path_node = previous_nodes[path_node]
    path = path[::-1]  # 反转path得到正序排列
    return distances[end_city], path, prev_path  # 返回总时间，起点到终点的路径，使用的所有车次


def train_cost_decision(start_city, end_city):  # 火车最少价钱
    distances = {node: INF for node in train_cost}  # 距离初始化为无穷
    previous_nodes = {node: None for node in train_cost}  # 经过节点初始化为空，Key为前驱，Value为后继
    distances[start_city] = 0  # 起点到起点的距离为0
    priority_queue = [(0, start_city)]  # 初始化优先队列
    prev_node = start_city  # 前驱节点初始化为起点
    prev_path = {node: {node: list() for node in train_time} for node in train_time}  # 前驱路径初始化为空列表
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)  # 取队首最小值
        if curr_distance > distances[curr_node]:  # 距离大于已有距离说明已经优化，跳过
            continue
        for neighbor, all_costs in train_cost[curr_node].items():  # neighbor为相邻节点，all_costs为两个节点之间的所有车次价格
            all_times = train_time[curr_node][neighbor]  # 根据城市得到所有车次时间
            all_weights = list()
            i = 0
            while i < len(all_costs):  # 遍历所有价格，得到价格权重
                weight = all_costs[i]
                i_time = all_times[i]  # 记录价格对应的车次时间
                if curr_node != start_city:
                    if i_time[0] - prev_path[prev_node][curr_node][1] < 100:  # 换乘时间小于100，不满足条件，跳过
                        weight = INF
                all_weights.append(weight)  # 将计算的权重加入所有权重
                i += 1
            all_locates = [0]  # 下标定位列表
            min_weight = INF
            j = 0
            while j < len(all_weights):
                if all_weights[j] <= min_weight:
                    min_weight = all_weights[j]  # 取最小权重
                    if j != 0:
                        # 下标列表中要么只有1个元素，要么所有元素对应的权重相同，和第1个元素比较，若不相等则清空列表
                        if all_weights[j] <= all_weights[all_locates[0]]:
                            if all_weights[j] < all_weights[all_locates[0]]:
                                all_locates.clear()
                            all_locates.append(j)  # 将最小权重对应的下标加入定位列表中
                j += 1
            distance = curr_distance + min_weight  # 距离更新为当前距离+最小权重
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = curr_node
                min_time = INF
                locate = None
                for x in all_locates:  # 遍历所有定位，得到时间最短的车次下标
                    if curr_node == start_city:
                        x_time = all_times[x][1] - all_times[x][0]
                    elif curr_node != start_city:
                        x_time = all_times[x][1] - prev_path[prev_node][curr_node][1]
                    if x_time < min_time:
                        locate = x
                prev_path[curr_node][neighbor] = all_times[locate]  # 把当前节点到相邻节点的车次更新为最小权重对应的最短时间车次
                prev_node = curr_node
                heapq.heappush(priority_queue, (distance, neighbor))
    path = list()
    path_node = end_city
    while path_node is not None:  # 得到经过城市的倒序排列
        path.append(path_node)
        path_node = previous_nodes[path_node]
    path = path[::-1]  # 反转path得到正序排列
    return distances[end_city], path, prev_path  # 返回总时间，起点到终点的路径，使用的所有车次


def train_cost_count(path, prev_path):  # 计算总价格
    total_cost = 0
    i = 0
    while i < len(path) - 1:
        index = list()
        j = 0
        while j < len(train_time[path[i]][path[i + 1]]):
            if train_time[path[i]][path[i + 1]][j] == prev_path[path[i]][path[i + 1]]:
                index.append(j)
            j += 1
        min_cost = INF
        for x in index:  # 对时间相同的路径计算最低价格，与时间算法的取法一致
            if train_cost[path[i]][path[i + 1]][x] < min_cost:
                min_cost = train_cost[path[i]][path[i + 1]][x]
        total_cost += min_cost
        i += 1
    return total_cost


def train_time_count(path, prev_path):  # 计算总时间
    total_time = prev_path[path[-2]][path[-1]][1] - prev_path[path[0]][path[1]][0]  # 最后一趟车的到达时间-第一趟车的出发时间
    return total_time


def train_display_information(path, prev_path):  # 显示每段路程信息
    i = 0
    while i < len(path) - 1:
        index = list()
        j = 0
        while j < len(train_time[path[i]][path[i + 1]]):
            if train_time[path[i]][path[i + 1]][j] == prev_path[path[i]][path[i + 1]]:
                index.append(j)
            j += 1
        min_cost = INF
        for x in index:  # 对时间相同的路径计算最低价格，与时间算法的取法一致
            if train_cost[path[i]][path[i + 1]][x] < min_cost:
                min_cost = train_cost[path[i]][path[i + 1]][x]
        print(f"{path[i]}, {path[i + 1]}, {prev_path[path[i]][path[i + 1]]}, {min_cost}")
        i += 1


plane_time = dict()  # 飞机时刻表
plane_cost = dict()  # 飞机价格表


def show_plane_time():  # 查看飞机时刻表
    print(plane_time)


def show_plane_cost():  # 查看飞机价格表
    print(plane_cost)


def add_plane(start_city, end_city, start_time, end_time, cost):  # 添加飞机线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法添加")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法添加")
        return None
    if start_city not in plane_time.keys():
        plane_time[start_city] = dict()
        plane_cost[start_city] = dict()
    if end_city not in plane_time[start_city].keys():
        plane_time[start_city][end_city] = list()
        plane_cost[start_city][end_city] = list()
    if end_city not in plane_time.keys():
        plane_time[end_city] = dict()
        plane_cost[end_city] = dict()
    if (start_time, end_time) in plane_time[start_city][end_city]:
        index = list()
        i = 0
        while i < len(plane_time[start_city][end_city]):
            if plane_time[start_city][end_city][i] == (start_time, end_time):
                index.append(i)
            i += 1
        for x in index:
            if plane_cost[start_city][end_city][x] == cost:
                print("该线路已存在，无法添加")
                return None
    plane_time[start_city][end_city].append((start_time, end_time))  # 两个时间均采用hhmm格式
    plane_cost[start_city][end_city].append(cost)


def delete_plane(start_city, end_city, start_time, end_time, cost):  # 删除飞机线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法删除")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法删除")
        return None
    time_index = list()
    i = 0
    while i < len(plane_time[start_city][end_city]):
        if plane_time[start_city][end_city][i] == (start_time, end_time):
            time_index.append(i)
        i += 1
    cost_index = list()
    j = 0
    while j < len(plane_time[start_city][end_city]):
        if plane_cost[start_city][end_city][j] == cost:
            cost_index.append(j)
        j += 1
    index = [elem for elem in time_index if elem in cost_index]  # 得到同时符合时间和价格的车次下标
    plane_time[start_city][end_city].pop(index[0])
    if not plane_time[start_city][end_city]:  # 如果出发城市没有通往到达城市的线路，在字典中删除
        del plane_time[start_city][end_city]
    if not plane_time[start_city]:  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del plane_time[start_city]
    plane_cost[start_city][end_city].pop(index[0])
    if not plane_cost[start_city][end_city]:  # 如果出发城市没有通往到达城市的线路，在字典中删除
        del plane_cost[start_city][end_city]
    if not plane_cost[start_city]:  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del plane_cost[start_city]


def plane_time_decision(start_city, end_city):  # 飞机最短时间
    distances = {node: INF for node in plane_time}  # 距离初始化为无穷
    previous_nodes = {node: None for node in plane_time}  # 经过节点初始化为空，Key为前驱，Value为后继
    distances[start_city] = 0  # 起点到起点的距离为0
    priority_queue = [(0, start_city)]  # 初始化优先队列
    prev_node = start_city  # 前驱节点初始化为起点
    prev_path = {node: {node: list() for node in plane_time} for node in plane_time}  # 前驱路径初始化为空列表
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)  # 取队首最小值
        if curr_distance > distances[curr_node]:  # 距离大于已有距离说明已经优化，跳过
            continue
        for neighbor, all_times in plane_time[curr_node].items():  # neighbor为相邻节点，all_times为两个节点之间的所有车次时间
            all_costs = plane_cost[curr_node][neighbor]
            all_weights = list()
            i = 0
            while i < len(all_times):  # 遍历所有车次，得到时间权重
                if curr_node == start_city:  # 当前节点为起点，没有换乘时间，直接计算车次时长
                    weight = all_times[i][1] - all_times[i][0]
                elif curr_node != start_city:  # 当前节点不是起点，权重为换乘时间+车次时长
                    weight = all_times[i][1] - prev_path[prev_node][curr_node][1]
                    if all_times[i][0] - prev_path[prev_node][curr_node][1] < 200:  # 换乘时间小于200，不满足条件，跳过
                        weight = INF
                all_weights.append(weight)  # 将计算的权重加入所有权重
                i += 1
            all_locates = [0]  # 下标定位列表
            min_weight = INF
            j = 0
            while j < len(all_weights):
                if all_weights[j] <= min_weight:
                    min_weight = all_weights[j]  # 取最小权重
                    if j != 0:
                        # 下标列表中要么只有1个元素，要么所有元素对应的权重相同，和第1个元素比较，若不相等则清空列表
                        if all_weights[j] <= all_weights[all_locates[0]]:
                            if all_weights[j] < all_weights[all_locates[0]]:
                                all_locates.clear()
                            all_locates.append(j)
                j += 1
            distance = curr_distance + min_weight  # 距离更新为当前距离+最小权重
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = curr_node
                min_cost = INF
                locate = None
                for x in all_locates:  # 遍历所有定位，得到价格最低的车次下标
                    x_cost = all_costs[x]
                    if x_cost < min_cost:
                        min_cost = x_cost
                        locate = x
                prev_path[curr_node][neighbor] = all_times[locate]  # 把当前节点到相邻节点的车次更新为最小权重对应的最低价格车次
                prev_node = curr_node
                heapq.heappush(priority_queue, (distance, neighbor))
    path = list()
    path_node = end_city
    while path_node is not None:  # 得到经过城市的倒序排列
        path.append(path_node)
        path_node = previous_nodes[path_node]
    path = path[::-1]  # 反转path得到正序排列
    return distances[end_city], path, prev_path  # 返回总时间，起点到终点的路径，使用的所有车次


def plane_cost_decision(start_city, end_city):  # 飞机最少价钱
    distances = {node: INF for node in plane_cost}  # 距离初始化为无穷
    previous_nodes = {node: None for node in plane_cost}  # 经过节点初始化为空，Key为前驱，Value为后继
    distances[start_city] = 0  # 起点到起点的距离为0
    priority_queue = [(0, start_city)]  # 初始化优先队列
    prev_node = start_city  # 前驱节点初始化为起点
    prev_path = {node: {node: list() for node in plane_time} for node in plane_time}  # 前驱路径初始化为空列表
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)  # 取队首最小值
        if curr_distance > distances[curr_node]:  # 距离大于已有距离说明已经优化，跳过
            continue
        for neighbor, all_costs in train_cost[curr_node].items():  # neighbor为相邻节点，all_costs为两个节点之间的所有车次价格
            all_times = plane_time[curr_node][neighbor]  # 根据城市得到所有车次时间
            all_weights = list()
            i = 0
            while i < len(all_costs):  # 遍历所有价格，得到价格权重
                weight = all_costs[i]
                i_time = all_times[i]  # 记录价格对应的车次时间
                if curr_node != start_city:
                    if i_time[0] - prev_path[prev_node][curr_node][1] < 200:  # 换乘时间小于200，不满足条件，跳过
                        weight = INF
                all_weights.append(weight)  # 将计算的权重加入所有权重
                i += 1
            all_locates = [0]  # 下标定位列表
            min_weight = INF
            j = 0
            while j < len(all_weights):
                if all_weights[j] <= min_weight:
                    min_weight = all_weights[j]  # 取最小权重
                    if j != 0:
                        # 下标列表中要么只有1个元素，要么所有元素对应的权重相同，和第1个元素比较，若不相等则清空列表
                        if all_weights[j] <= all_weights[all_locates[0]]:
                            if all_weights[j] < all_weights[all_locates[0]]:
                                all_locates.clear()
                            all_locates.append(j)  # 将最小权重对应的下标加入定位列表中
                j += 1
            distance = curr_distance + min_weight  # 距离更新为当前距离+最小权重
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = curr_node
                min_time = INF
                locate = None
                for x in all_locates:  # 遍历所有定位，得到时间最短的车次下标
                    if curr_node == start_city:
                        x_time = all_times[x][1] - all_times[x][0]
                    elif curr_node != start_city:
                        x_time = all_times[x][1] - prev_path[prev_node][curr_node][1]
                    if x_time < min_time:
                        locate = x
                prev_path[curr_node][neighbor] = all_times[locate]  # 把当前节点到相邻节点的车次更新为最小权重对应的最短时间车次
                prev_node = curr_node
                heapq.heappush(priority_queue, (distance, neighbor))
    path = list()
    path_node = end_city
    while path_node is not None:  # 得到经过城市的倒序排列
        path.append(path_node)
        path_node = previous_nodes[path_node]
    path = path[::-1]  # 反转path得到正序排列
    return distances[end_city], path, prev_path  # 返回总时间，起点到终点的路径，使用的所有车次


def plane_cost_count(path, prev_path):  # 计算总价格
    total_cost = 0
    i = 0
    while i < len(path) - 1:
        index = list()
        j = 0
        while j < len(plane_time[path[i]][path[i + 1]]):
            if plane_time[path[i]][path[i + 1]][j] == prev_path[path[i]][path[i + 1]]:
                index.append(j)
            j += 1
        min_cost = INF
        for x in index:  # 对时间相同的路径计算最低价格，与时间算法的取法一致
            if plane_cost[path[i]][path[i + 1]][x] < min_cost:
                min_cost = plane_cost[path[i]][path[i + 1]][x]
        total_cost += min_cost
        i += 1
    return total_cost


def plane_time_count(path, prev_path):  # 计算总时间
    total_time = prev_path[path[-2]][path[-1]][1] - prev_path[path[0]][path[1]][0]  # 最后一趟车的到达时间-第一趟车的出发时间
    return total_time


def plane_display_information(path, prev_path):  # 显示每段路程信息
    i = 0
    while i < len(path) - 1:
        index = list()
        j = 0
        while j < len(plane_time[path[i]][path[i + 1]]):
            if plane_time[path[i]][path[i + 1]][j] == prev_path[path[i]][path[i + 1]]:
                index.append(j)
            j += 1
        min_cost = INF
        for x in index:  # 对时间相同的路径计算最低价格，与时间算法的取法一致
            if plane_cost[path[i]][path[i + 1]][x] < min_cost:
                min_cost = plane_cost[path[i]][path[i + 1]][x]
        print(f"{path[i]}, {path[i + 1]}, {prev_path[path[i]][path[i + 1]]}, {min_cost}")
        i += 1




from Views.login_ui import Win as MainWin

from Controller.login_control import Controller as MainUIController

app = MainWin(MainUIController())                   #窗口控制器传递给UI

if __name__ == '__main__':
    app.mainloop()
