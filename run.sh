# K = 5
~/mahout-distribution-0.9/bin/mahout org.apache.mahout.clustering.syntheticcontrol.kmeans.Job -k 5 -t1 100 -t2 10 -x 1000 -ow -i /user/hadoop/temp.data -o result
~/mahout-distribution-0.9/bin/mahout/mahout seqdumper -i result/clusteredPoints -o points
~/mahout-distribution-0.9/bin/mahout/mahout clusterdump -i result/clusters-1-final --pointsDir centroids -o centroids

# K = 10
~/mahout-distribution-0.9/bin/mahout org.apache.mahout.clustering.syntheticcontrol.kmeans.Job -k 10 -t1 100 -t2 10 -x 1000 -ow -i /user/hadoop/temp.data -o result
~/hadoop/bin/hadoop fs -get /user/hadoop/result
mv result ~/k10

# K = 20
~/mahout-distribution-0.9/bin/mahout org.apache.mahout.clustering.syntheticcontrol.kmeans.Job -k 20 -t1 100 -t2 10 -x 1000 -ow -i /user/hadoop/temp.data -o result
~/hadoop/bin/hadoop fs -get /user/hadoop/result
mv result ~/k20

# K = 40
~/mahout-distribution-0.9/bin/mahout org.apache.mahout.clustering.syntheticcontrol.kmeans.Job -k 40 -t1 100 -t2 10 -x 1000 -ow -i /user/hadoop/temp.data -o result
~/hadoop/bin/hadoop fs -get /user/hadoop/result
mv result ~/k40

