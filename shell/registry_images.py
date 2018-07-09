#-*- coding:utf-8 -*-

import requests
import json
import traceback

ip = '10.13.0.63'
port = 5000
user = 'admin'
passwd = '111111'

def getImageName(ip, port):

    docker_images = []

    try:

        url_images = "http://%s:%d/v2/_catalog" % (ip, port)

        resp_images = requests.get(url_images).content.strip()

        images_json = json.loads(resp_images)

        images = images_json['repositories']

        for image in images:

            url_image = "http://%s:%d/v2/%s/tags/list" % (ip, port, image)

            resp_image = requests.get(url_image).content.strip()

            image_json = json.loads(resp_image)

            name = image_json['name']

            tags = image_json['tags']

            for tag in tags:  

                docker_name = "%s:%d/%s:%s" % (ip, port, name, tag)  

                docker_images.append(docker_name)  

    except:

        traceback.print_exc()

    return docker_images

images = getImageName(ip, port)

for i in images:
    print i

