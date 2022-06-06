docker_name="api_tests"
docker build -t $docker_name .
CID=$(docker container run -t -d $docker_name)

docker wait $CID
docker cp $CID:"/usr/app/src/ApiTesting/results/" ./
docker stop $CID
docker rm $CID
docker rmi $docker_name