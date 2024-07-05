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
"""


cities = list()                 # 城市存储
def show_city():                # 查看城市
    print(cities)
def add_city(new_city):         # 添加城市
    if new_city in cities:      # 城市已存在，跳过
        print(f"{new_city}已存在")
    else:                       # 城市不存在，添加
        cities.append(new_city)
        print(f"{new_city}已添加")
def delete_city(del_city):      # 删除城市
    if del_city not in cities:  # 城市不存在，跳过
        print(f"{del_city}不存在")
    else:                       # 城市已存在，删除
        cities.remove(del_city)
        del train_time[del_city]  # 时刻表中删除
        for city in train_time:
            train_time[city].pop(del_city, None)
        del train_cost[del_city]  # 价格表中删除
        for city in train_cost:
            train_cost[city].pop(del_city, None)
        print(f"{del_city}已删除")


train_time = dict()     # 火车时刻表
train_cost = dict()     # 火车价格表
def show_train_time():  # 查看火车时刻表
    print(train_time)
def show_train_cost():  # 查看火车价格表
    print(train_cost)
def add_train(start_city, end_city, start_time, end_time, cost):    # 添加火车线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法添加")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法添加")
        return None
    if start_city not in train_time.keys():
        train_time[start_city] = dict()
        train_cost[start_city] = dict()
    if end_city not in train_time.keys():
        train_time[end_city] = dict()
        train_cost[end_city] = dict()
    train_time[start_city][end_city] = (start_time, end_time)       # 两个时间均采用hhmm格式
    train_cost[start_city][end_city] = cost
def delete_train(start_city, end_city):                                # 删除火车线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法删除")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法删除")
        return None
    train_time[start_city].pop(end_city)
    if not train_time[start_city]:                                  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del train_time[start_city]
    train_cost[start_city].pop(end_city)
    if not train_cost[start_city]:                                  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del train_cost[start_city]
def get_train_time(start_city, end_city):           # 查询火车时长
    return train_time[start_city][end_city][1] - train_time[start_city][end_city][0]
def get_train_cost(start_city, end_city):           # 查询火车价钱
    return train_cost[start_city][end_city]


INF = float('inf')
def train_time_decision():                                                  # 火车最短时间
    nodes = list(train_time.keys())
    distances = {node: {node: 0 for node in nodes} for node in nodes}       # 权值初始化为0
    times = {node: {node: (0, 0) for node in nodes} for node in nodes}      # 时间初始化为(0, 0)
    path = {u: {v: [] for v in nodes if u != v} for u in nodes}             # 路径初始化为空列表
    for u in nodes:
        for v in nodes:
            if u != v:
                times[u][v] = train_time[u].get(v, (INF, INF))              # 获取到另一个点的起止时间，如果没有点就置为(INF, INF)
                if times[u][v] != (INF, INF):                               # 有起止时间就计算权值，没有就置为INF
                    distances[u][v] = times[u][v][1] - times[u][v][0]
                else:
                    distances[u][v] = INF
                if distances[u][v] < INF:                                   # 两个点之间有距离说明有路径，添加到结点列表中
                    path[u][v] = [u, v]
    for k in nodes:                                                         # Floyd算法
        for i in nodes:
            for j in nodes:
                spare_time = times[k][j][0] - times[i][k][1]                # 换乘时间
                if spare_time >= 100:                                       # 火车至少1h换乘
                    if distances[i][k] < INF and distances[k][j] < INF:
                        if distances[i][j] > distances[i][k] + distances[k][j] + spare_time:        # 更新时间时将换乘时间加入计算
                            distances[i][j] = distances[i][k] + distances[k][j] + spare_time
                            path[i][j] = path[i][k] + path[k][j][1:]        # 将两段路径（以列表存储）连起来
    return distances, path
def train_cost_decision():                                                  # 火车最少价钱
    nodes = list(train_cost.keys())
    distances = {node: {node: 0 for node in nodes} for node in nodes}       # 权值初始化为0
    times = {node: {node: (0, 0) for node in nodes} for node in nodes}      # 时间初始化为(0, 0)
    path = {u: {v: [] for v in nodes if u != v} for u in nodes}             # 路径初始化为空列表
    for u in nodes:
        for v in nodes:
            if u != v:
                times[u][v] = train_time[u].get(v, (INF, INF))              # 获取到另一个点的起止时间，如果没有点就置为(INF, INF)
                distances[u][v] = train_cost[u].get(v, INF)                 # 获取到另一个点的距离，如果没有距离就置为INF
                if distances[u][v] < INF:                                   # 两个点之间有距离说明有路径，添加到结点列表中
                    path[u][v] = [u, v]
    for k in nodes:                                                         # Floyd算法
        for i in nodes:
            for j in nodes:
                spare_time = times[k][j][0] - times[i][k][1]                # 换乘时间
                if spare_time >= 100:                                       # 火车至少1h换乘
                    if distances[i][k] < INF and distances[k][j] < INF:
                        if distances[i][j] > distances[i][k] + distances[k][j]:
                            distances[i][j] = distances[i][k] + distances[k][j]
                            path[i][j] = path[i][k] + path[k][j][1:]        # 将两段路径（以列表存储）连起来
    return distances, path


def train_cost_count(path):       # 计算总价格
    total_cost = 0
    i = 0
    while i < len(path) - 1:
        total_cost += get_train_cost(path[i], path[i+1])
        i += 1
    return total_cost
def train_time_count(path):       # 计算总时间
    total_time = 0
    i = 0
    while i < len(path) - 1:
        if i != len(path) - 2:
            spare_time = train_time[path[i + 1]][path[i + 2]][0] - train_time[path[i]][path[i + 1]][1]  # 换乘时间
            total_time = total_time + get_train_time(path[i], path[i + 1]) + spare_time                 # 每段路径的时间加上换乘下一段的时间
        else:
            total_time = total_time + get_train_time(path[i], path[i + 1])
        i += 1
    return total_time


def train_display_information(path):      # 显示每段路程信息
    i = 0
    while i < len(path) - 1:
        print(f"出发城市：{path[i]}，到达城市：{path[i + 1]}，出发时间：{train_time[path[i]][path[i + 1]][0]}，"
              f"到达时间：{train_time[path[i]][path[i + 1]][1]}，价格：{train_cost[path[i]][path[i + 1]]}")
        i += 1


plane_time = dict()     # 飞机时刻表
plane_cost = dict()     # 飞机价格表
def show_plane_time():  # 查看飞机时刻表
    print(plane_time)
def show_plane_cost():  # 查看飞机价格表
    print(plane_cost)
def add_plane(start_city, end_city, start_time, end_time, cost):    # 添加飞机线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法添加")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法添加")
        return None
    if start_city not in plane_time.keys():
        plane_time[start_city] = dict()
        plane_cost[start_city] = dict()
    if end_city not in plane_time.keys():
        plane_time[end_city] = dict()
        plane_cost[end_city] = dict()
    plane_time[start_city][end_city] = (start_time, end_time)       # 两个时间均采用hhmm格式
    plane_cost[start_city][end_city] = cost
def delete_plane(start_city, end_city):                                # 删除飞机线路
    if start_city not in cities or end_city not in cities:
        if start_city not in cities:
            print(f"{start_city}不在城市列表里，无法删除")
        if end_city not in cities:
            print(f"{end_city}不在城市列表里，无法删除")
        return None
    plane_time[start_city].pop(end_city)
    if not plane_time[start_city]:                                  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del plane_time[start_city]
    plane_cost[start_city].pop(end_city)
    if not plane_cost[start_city]:                                  # 如果出发城市没有通往其他城市的线路，在字典中删除
        del plane_cost[start_city]
def get_plane_time(start_city, end_city):           # 查询飞机时长
    return plane_time[start_city][end_city][1] - plane_time[start_city][end_city][0]
def get_plane_cost(start_city, end_city):           # 查询飞机价钱
    return plane_cost[start_city][end_city]


# INF defined above
def plane_time_decision():                                                  # 飞机最短时间
    nodes = list(plane_time.keys())
    distances = {node: {node: 0 for node in nodes} for node in nodes}       # 权值初始化为0
    times = {node: {node: (0, 0) for node in nodes} for node in nodes}      # 时间初始化为(0, 0)
    path = {u: {v: [] for v in nodes if u != v} for u in nodes}             # 路径初始化为空列表
    for u in nodes:
        for v in nodes:
            if u != v:
                times[u][v] = plane_time[u].get(v, (INF, INF))              # 获取到另一个点的起止时间，如果没有点就置为(INF, INF)
                if times[u][v] != (INF, INF):                               # 有起止时间就计算权值，没有就置为INF
                    distances[u][v] = times[u][v][1] - times[u][v][0]
                else:
                    distances[u][v] = INF
                if distances[u][v] < INF:                                   # 两个点之间有距离说明有路径，添加到结点列表中
                    path[u][v] = [u, v]
    for k in nodes:                                                         # Floyd算法
        for i in nodes:
            for j in nodes:
                spare_time = times[k][j][0] - times[i][k][1]                # 换乘时间
                if spare_time >= 200:                                       # 飞机至少2h换乘
                    if distances[i][k] < INF and distances[k][j] < INF:
                        if distances[i][j] > distances[i][k] + distances[k][j] + spare_time:        # 更新时间时将换乘时间加入计算
                            distances[i][j] = distances[i][k] + distances[k][j] + spare_time
                            path[i][j] = path[i][k] + path[k][j][1:]        # 将两段路径（以列表存储）连起来
    return distances, path
def plane_cost_decision():                                                  # 飞机最少价钱
    nodes = list(plane_cost.keys())
    distances = {node: {node: 0 for node in nodes} for node in nodes}       # 权值初始化为0
    times = {node: {node: (0, 0) for node in nodes} for node in nodes}      # 时间初始化为(0, 0)
    path = {u: {v: [] for v in nodes if u != v} for u in nodes}             # 路径初始化为空列表
    for u in nodes:
        for v in nodes:
            if u != v:
                times[u][v] = plane_time[u].get(v, (INF, INF))              # 获取到另一个点的起止时间，如果没有点就置为(INF, INF)
                distances[u][v] = plane_cost[u].get(v, INF)                 # 获取到另一个点的距离，如果没有距离就置为INF
                if distances[u][v] < INF:                                   # 两个点之间有距离说明有路径，添加到结点列表中
                    path[u][v] = [u, v]
    for k in nodes:                                                         # Floyd算法
        for i in nodes:
            for j in nodes:
                spare_time = times[k][j][0] - times[i][k][1]                # 换乘时间
                if spare_time >= 200:                                       # 飞机至少2h换乘
                    if distances[i][k] < INF and distances[k][j] < INF:
                        if distances[i][j] > distances[i][k] + distances[k][j]:
                            distances[i][j] = distances[i][k] + distances[k][j]
                            path[i][j] = path[i][k] + path[k][j][1:]        # 将两段路径（以列表存储）连起来
    return distances, path


def plane_cost_count(path):       # 计算飞机总价格
    total_cost = 0
    i = 0
    while i < len(path) - 1:
        total_cost += get_plane_cost(path[i], path[i+1])
        i += 1
    return total_cost
def plane_time_count(path):       # 计算飞机总时间
    total_time = 0
    i = 0
    while i < len(path) - 1:
        if i != len(path) - 2:
            spare_time = plane_time[path[i + 1]][path[i + 2]][0] - plane_time[path[i]][path[i + 1]][1]  # 换乘时间
            total_time = total_time + get_plane_time(path[i], path[i + 1]) + spare_time                 # 每段路径的时间加上换乘下一段的时间
        else:
            total_time = total_time + get_plane_time(path[i], path[i + 1])
        i += 1
    return total_time


def plane_display_information(path):      # 显示每段路程信息
    i = 0
    while i < len(path) - 1:
        print(f"出发城市：{path[i]}，到达城市：{path[i + 1]}，出发时间：{plane_time[path[i]][path[i + 1]][0]}，"
              f"到达时间：{plane_time[path[i]][path[i + 1]][1]}，价格：{plane_cost[path[i]][path[i + 1]]}")
        i += 1


def administrator():
    print("管理员界面")
    while True:
        print("请输入要操作的内容：")
        print("城市[1]\n火车[2]\n飞机[3]\n返回上一页[4]")
        choice1 = int(input())
        if choice1 == 1:
            while True:
                print("请输入要进行的操作：")
                print("查看城市[1]\n添加城市[2]\n删除城市[3]\n返回上一页[4]")
                choice2 = int(input())
                if choice2 == 1:
                    show_city()
                    continue
                elif choice2 == 2:
                    print("请输入要添加的城市：")
                    add_city(input())
                    continue
                elif choice2 == 3:
                    print("请输入要删除的城市：")
                    delete_city(input())
                    continue
                elif choice2 == 4:
                    break
        elif choice1 == 2:
            while True:
                print("请输入要进行的操作：")
                print("查看时刻表[1]\n查看价格表[2]\n添加线路[3]\n删除线路[4]\n返回上一页[5]")
                choice3 = int(input())
                if choice3 == 1:
                    show_train_time()
                    continue
                elif choice3 == 2:
                    show_train_cost()
                    continue
                elif choice3 == 3:
                    start_city = input("出发城市：")
                    end_city = input("到达城市：")
                    start_time = int(input("出发时间："))
                    end_time = int(input("到达时间："))
                    cost = int(input("价格："))
                    add_train(start_city, end_city, start_time, end_time, cost)
                    print(f"{start_city}到{end_city}的火车线路已添加")
                    continue
                elif choice3 == 4:
                    start_city = input("出发城市：")
                    end_city = input("到达城市：")
                    delete_train(start_city, end_city)
                    print(f"{start_city}到{end_city}的火车线路已删除")
                    continue
                elif choice3 == 5:
                    break
        elif choice1 == 3:
            while True:
                print("请输入要进行的操作：")
                print("查看时刻表[1]\n查看价格表[2]\n添加线路[3]\n删除线路[4]\n返回上一页[5]")
                choice3 = int(input())
                if choice3 == 1:
                    show_plane_time()
                    continue
                elif choice3 == 2:
                    show_plane_cost()
                    continue
                elif choice3 == 3:
                    start_city = input("出发城市：")
                    end_city = input("到达城市：")
                    start_time = int(input("出发时间："))
                    end_time = int(input("到达时间："))
                    cost = int(input("价格："))
                    add_plane(start_city, end_city, start_time, end_time, cost)
                    print(f"{start_city}到{end_city}的飞机线路已添加")
                    continue
                elif choice3 == 4:
                    start_city = input("出发城市：")
                    end_city = input("到达城市：")
                    delete_plane(start_city, end_city)
                    print(f"{start_city}到{end_city}的飞机线路已删除")
                    continue
                elif choice3 == 5:
                    break
        elif choice1 == 4:
            break
def user():
    print("用户界面")
    while True:
        print("请输入要进行的操作：")
        print("查看城市[1]\n查看火车时刻表与价格表[2]\n查看飞机时刻表与价格表[3]\n查询火车线路[4]\n查询飞机线路[5]\n返回上一页[6]")
        choice1 = int(input())
        if choice1 == 1:
            show_city()
            continue
        elif choice1 == 2:
            show_train_time()
            show_train_cost()
            continue
        elif choice1 == 3:
            show_plane_time()
            show_plane_cost()
            continue
        elif choice1 == 4:
            start_city = input("出发城市：")
            end_city = input("到达城市：")
            print("请选择决策方式：")
            print("最短时间[1]\n最低价格[2]")
            choice2 = int(input())
            if choice2 == 1:
                t_dist, t_path = train_time_decision()
                t_time = train_time_count(t_path[start_city][end_city])
                t_cost = train_cost_count(t_path[start_city][end_city])
                print(f"{start_city}到{end_city}之间火车的最短时间为{t_time}，总价格为{t_cost}")
                print("每段路程详细信息：")
                train_display_information(t_path[start_city][end_city])
            elif choice2 == 2:
                c_dist, c_path = train_cost_decision()
                c_time = train_time_count(c_path[start_city][end_city])
                c_cost = train_cost_count(c_path[start_city][end_city])
                print(f"{start_city}到{end_city}之间火车的最低价格为{c_cost}，总时间为{c_time}")
                print("每段路程详细信息：")
                train_display_information(c_path[start_city][end_city])
            continue
        elif choice1 == 5:
            start_city = input("出发城市：")
            end_city = input("到达城市：")
            print("请选择决策方式：")
            print("最短时间[1]\n最低价格[2]")
            choice2 = int(input())
            if choice2 == 1:
                t_dist, t_path = plane_time_decision()
                t_time = plane_time_count(t_path[start_city][end_city])
                t_cost = plane_cost_count(t_path[start_city][end_city])
                print(f"{start_city}到{end_city}之间飞机的最短时间为{t_time}，总价格为{t_cost}")
                print("每段路程详细信息：")
                plane_display_information(t_path[start_city][end_city])
            elif choice2 == 2:
                c_dist, c_path = train_cost_decision()
                c_time = train_time_count(c_path[start_city][end_city])
                c_cost = train_cost_count(c_path[start_city][end_city])
                print(f"{start_city}到{end_city}之间飞机的最低价格为{c_cost}，总时间为{c_time}")
                print("每段路程详细信息：")
                train_display_information(c_path[start_city][end_city])
            continue
        elif choice1 == 6:
            break
def main():
    print("欢迎使用本系统！")
    while True:
        print("请输入您的身份：")
        print("管理员[1]\n用户[2]\n退出系统[3]")
        choice = int(input())
        if choice == 1:
            administrator()
            continue
        elif choice == 2:
            user()
            continue
        elif choice == 3:
            break
main()