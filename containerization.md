# How to create, build and publish the image on dockerhub

**1. Create a file called "requirements.txt" in the "meusite" folder and put:**
```
Flask==0.12 
```
**2. Create a Dockerfile in the "meusite" folder and put:**
```
FROM python:3.6.1-alpine

RUN pip install --upgrade pip

WORKDIR /env

ADD . /env

RUN pip install -r requirements.txt

CMD ["python","app.py"]
```
**3. build the image with docker:**
```
sudo docker build -t env .
```
**4. check if it was created:**
```
sudo docker images
```
``if yes:``
```
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE                                                                                                                                                  
env          latest    ff7a966a00a3   9 seconds ago   128MB
```
**5. run the container:**
```
sudo docker run -p 8888:5000 -d env
```
``you can change the port with -p``

**6. to list all containers and check if they are running:**
```
sudo docker ps -a
```
**7. to put the image on dockerhub repository, first we need login and place a tag:**
```
docker login or docker login -u "myusername" -p "mypassword" docker.io
```
``and placa a tag:``
```
sudo docker tag ff7a966a00a3 env:newtag
```
**8. push the image to your repository:**
```
sudo docker push abcd/env:newtag
```
``abcd= user /env= repository name :newtag= tagger by docker tag``



