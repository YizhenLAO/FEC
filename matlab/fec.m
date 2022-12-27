tic %计时开始

cloud = pcread('D:\cloud\kitti\004093_004408.ply');
point = cloud.Location';
min_component_size = 50; %最小聚类点数
max_n = 50;    %最大返回邻居数
tolorance = 0.2;    %半径阈值

cloud_size = length(point);
marked_indices = zeros(1,cloud_size);

if cloud_size < min_component_size
    error("Could not find any cluster")
else
    fprintf("Point Cloud has %d points\n",cloud_size)
end

tag_num = 1;
for i=1:cloud_size
    if marked_indices(i)==0
        p_cur = point(:,i);
        p_cur = p_cur';
        [indices,dists] = findNearestNeighbors(cloud,p_cur,max_n);
        for j=1:length(indices)
            if dists(j)>tolorance
                indices(j)=0;
            end
        end
        indices(indices==0)=[];
        min_tag_num = tag_num;
        for j=1:length(indices)
            if (marked_indices(indices(j))>0) && (marked_indices(indices(j))<min_tag_num)
                min_tag_num = marked_indices(indices(j));
            end
        end
        for j=1:length(indices)
            temp_tag_num = marked_indices(indices(j));
            if temp_tag_num > min_tag_num
                for k=1:cloud_size
                    if marked_indices(k)==temp_tag_num
                        marked_indices(k) = min_tag_num;
                    end
                end
            end
            marked_indices(indices(j)) = min_tag_num;
        end
    tag_num = tag_num+1;
    end
end

indices_tags = zeros(cloud_size,2);
for i = 1:cloud_size
    indices_tags(i,2) = i;
    indices_tags(i,1) = marked_indices(i);
end

indices_tags = sortrows(indices_tags);
final_index = zeros(cloud_size,1);
final_class = zeros(cloud_size,1);

begin_index = 1;
class = 0;
k=1;
for i =1:cloud_size
    if indices_tags(i,1) ~= indices_tags(begin_index,1)
        if i-begin_index>=min_component_size
            for j=begin_index:i
                final_index(k) = indices_tags(j,2);
                final_class(k) = class;
                k=k+1;
            end
            class = class+1;
        end
        begin_index = i;
    end
end
for i =1:cloud_size
    if indices_tags(i,1) ~= indices_tags(begin_index,1)
        if i-begin_index>=min_component_size    
            for j=begin_index:i
                final_index(k) = indices_tags(j,2);
                final_class(k) = class;
                k=k+1;
            end
            class = class+1;
        end
    end
end

final_class(k:end)=[];
final_index(k:end)=[];

toc %计时结束

cloud = select(cloud,final_index);
point = cloud.Location;

pcshow(point,final_class);

