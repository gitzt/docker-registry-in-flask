# docker resigry 命令
登录/上传  
docker login -u admin 10.36.0.141:5000  
docker push 10.36.0.141:5000/registry  

查看镜像  
curl -u admin 10.36.0.141:5000/v2/_catalog  
curl -u admin 10.36.0.141:5000/v2/registry/tags/list  

获取sha256  
curl -u admin -H "Accept: application/vnd.docker.distribution.manifest.v2+json" -I -XGET http://10.36.0.141:5000/v2/registry/manifests/latest  

删除镜像  
curl -u admin --header "Accept:application/vnd.docker.distribution.manifest.v2+json" -I -X DELETE http://10.36.0.141:5000/v2/registry/manifests/sha256:6d995dae7b7b1ec8c782f2b45f9d569a65b5210b117172831bf15c85e3b086f5  

垃圾回收  
docker run -it --name gc --rm --volumes-from registry registry garbage-collect /etc/docker/registry/config.yml


# requirements.txt
记录了当前程序的所有依赖包及其精确版本号  
生成  
(venv) $ pip freeze > requirements.txt  
安装依赖  
(venv) $ pip install -r requirements.txt  


# venv
安装虚拟环境：pip install virtualenv  
初始化环境：virtualenv --no-site-packages venv  
进入环境：source venv/bin/activate  
退出环境：deactivate  
