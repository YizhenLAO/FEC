import time
import numpy
import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class PointIndex_NumberTag(object):
    def __init__(self):
        self.nPointIndex = 0.0
        self.nNumberTag = 0.0

    class Struct(object):
        def __init__(self, nPointIndex, nNumberTag):
            self.nPointIndex = nPointIndex
            self.nNumberTag = nNumberTag

def main():
    # 通过pcl.load加载pcd文件
    min_component_size = 100
    tolorance = 0.5
    max_n = 50

    start = time.perf_counter()
    cloud = o3d.io.read_point_cloud("../data/street.ply")
    cloud_tree = o3d.geometry.KDTreeFlann(cloud)
    point = numpy.asarray(cloud.points)
    size = len(point)
    marked_indices = [0] * size

    if size < min_component_size:
        raise("Could not find any cluster")
    else:
        print(cloud)

    tag_num = 1
    temp_tag_num = -1
    for i in range(size):
        if marked_indices[i] == 0:
            idx = []
            [k, idx, _] = cloud_tree.search_hybrid_vector_3d(cloud.points[i], tolorance, max_n)
            min_tag_num = tag_num
            for j in idx:
                if (marked_indices[j] > 0) and (marked_indices[j] < min_tag_num):
                    min_tag_num = marked_indices[j]
            for j in idx:
                temp_tag_num = marked_indices[j]
                if temp_tag_num > min_tag_num:
                    for k in range(size):
                        if marked_indices[k] == temp_tag_num:
                            marked_indices[k] = min_tag_num
                marked_indices[j] = min_tag_num
        tag_num += 1

    indices_tags = [[0]*2 for i in range(size)]
    for i in range(size):
        indices_tags[i][0] = i
        indices_tags[i][1] = marked_indices[i]

    indices_tags = sorted(indices_tags, key=lambda x:x[1])

      #indices_tags保存了每个聚类点云的索引和tag，下一步是根据索引提取点云，分开上色，并可视化
    begin_index = i = color_index = 0
    fianl_points = []
    for i in range(size):
        if indices_tags[i][1] != indices_tags[begin_index][1]:
            if i - begin_index >= min_component_size:
                for j in range(begin_index, i):
                    fianl_points.append(point[indices_tags[j][0]][0])
                    fianl_points.append(point[indices_tags[j][0]][1])
                    fianl_points.append(point[indices_tags[j][0]][2])
                    fianl_points.append(color_index)
                color_index += 1
            begin_index = i
    if indices_tags[i][1] != indices_tags[begin_index][1]: #最后一个聚类
        if i - begin_index >= min_component_size:
            for j in range(begin_index, i):
                fianl_points.append(point[indices_tags[j][0]][0])
                fianl_points.append(point[indices_tags[j][0]][1])
                fianl_points.append(point[indices_tags[j][0]][2])
                fianl_points.append(color_index)
            color_index += 1

    fianl_points = np.array(fianl_points)
    fianl_points = fianl_points.reshape(-1,4)

    end = time.perf_counter()
    print("running time: ", {end - start}, 'seconds')

    x = fianl_points[:,0]
    y = fianl_points[:,1]
    z = fianl_points[:,2]
    l = fianl_points[:,3]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig.add_axes(ax)
    ax.scatter(x,  # x
               y,  # y
               z,  # z
               l,
               c=l,  # height data for color
               s = 2,
               marker = 'o',
               cmap='rainbow')
    plt.axis('off')
    ax.set_box_aspect([15,15,1])
    plt.show()

if __name__ == "__main__":
    main()

