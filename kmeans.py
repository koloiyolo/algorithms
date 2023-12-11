from random import randrange
import maths


def kmeans(data, centroid_count, iters=100):

    data_copy = data.copy()
    data_with_centroids = []
    centroids = []
    clusters = []

    if len(data) > 1000:
        sampled_data = [data.pop(randrange(0, len(data))) for _ in range(1000)]
        data.clear()
        data.extend(sampled_data)

    for _ in range(centroid_count):
        centroids.append([randrange(0, 1000)/1000 for i in range(len(data[0]))])

    for _ in range(iters):
        data_with_centroids.clear()
        for point in data:
            current_centroid = centroids[0]
            for centroid in centroids:
                if maths.euclidean_distance(point, current_centroid) > maths.euclidean_distance(point, centroid):
                    current_centroid = centroid
            data_with_centroids.append([point, current_centroid])

        for i, centroid in enumerate(centroids):
            count = 0
            points = []
            scaling_factor = 2 * len(data)

            for point in data_with_centroids:
                if point[1] == centroid:
                    count += 1
                    points.append(point[0])

            for point in points:
                for j in range(len(centroid)):
                    centroid[j] += round(maths.means([point[j], centroid[j]]) / scaling_factor)

    # data_with_centroids.clear()
    # for point in data:
    #     current_centroid = centroids[0]
    #     for centroid in centroids:
    #         if maths.euclidean_distance(point, current_centroid) > maths.euclidean_distance(point, centroid):
    #             current_centroid = centroid
    #     data_with_centroids.append([point, current_centroid])

    for centroid in centroids:
        cluster = []
        clusters.append(cluster)
    #     for point in data_with_centroids:
    #         if centroid == point[1]:
    #             cluster.append(point[0])
    #     clusters.append(cluster)

    for point in data_copy:
        index = 0;
        min = maths.euclidean_distance(centroids[0], point)
        for i in range(len(centroids)):
            if min < maths.euclidean_distance(centroids[i], point):
                index = i
                min = maths.euclidean_distance(centroids[i], point)
        clusters[index].append(point)


    return clusters


data = [[randrange(0, 1000)/1000 for _ in range(4)] for _ in range(100000)]



print (kmeans(data, 5, 100))
