#pragma warning(disable:4996)
#include <iostream>
#include <fstream>
#include <ctime>
#include <chrono>
#include <string>
#include <pcl/io/ply_io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/PointIndices.h>
#include <pcl/point_types.h>
#include <pcl/point_cloud.h>
#include <pcl/visualization/pcl_visualizer.h>
#include "FEC.h"
using namespace std;
using namespace chrono;

// generate cluster color randomly
int* rand_rgb() {
    int* rgb = new int[3];
    rgb[0] = rand() % 255;
    rgb[1] = rand() % 255;
    rgb[2] = rand() % 255;
    return rgb;
}

int main() {
    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>);
    std::vector<pcl::PointIndices> cluster_indices;
    pcl::PLYReader readerPLY;
    unsigned long long size,i = 0,j = 0;

    // replace your data path here
    readerPLY.read("D:\\cloud\\kitti\\004093_004408.ply", *cloud);
    size = cloud->size();
    std::cout << "PointCloud has: " << size << " data points." << std::endl;

    auto start = system_clock::now();
    cluster_indices = FEC(cloud, 50, 0.2, 50);
    auto end = system_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    cout << "The algorithm took " << double(duration.count()) * microseconds::period::num / microseconds::period::den << " seconds." << endl;
   

    //visualization
    pcl::visualization::PCLVisualizer::Ptr viewer(new pcl::visualization::PCLVisualizer("Result of segement"));
    vector<unsigned char>color;
    for (int i_segment = 0; i_segment < cluster_indices.size(); i_segment++)
    {
        color.push_back(static_cast<unsigned char>(rand() % 256));
        color.push_back(static_cast<unsigned char>(rand() % 256));
        color.push_back(static_cast<unsigned char>(rand() % 256));
    }
    int color_index = 0;
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr color_point(new pcl::PointCloud<pcl::PointXYZRGB>);

    for (i = 0; i < cluster_indices.size(); i++) {
        for (j = 0; j < cluster_indices[i].indices.size(); j++) {
            pcl::PointXYZRGB point;
            point.x = cloud->points[cluster_indices[i].indices[j]].x;
            point.y = cloud->points[cluster_indices[i].indices[j]].y;
            point.z = cloud->points[cluster_indices[i].indices[j]].z;
            point.r = color[int(3) * color_index];
            point.g = color[int(3) * color_index + 1];
            point.b = color[int(3) * color_index + 2];
            color_point->push_back(point);
        }
        color_index++;
    }
    std::stringstream ss;
    viewer->addPointCloud(color_point);
    viewer->spin();


    return 0;
}