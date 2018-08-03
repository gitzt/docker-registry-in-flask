# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-07-27 21:45:01
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-03 15:30:35

import requests
import json
import traceback

ip = '10.13.0.63'
port = 5000

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

            if image_json['tags'] != None:

                name = image_json['name']

                tags = image_json['tags']

                for tag in tags:  

                    docker_name = "%s:%d/%s:%s" % (ip, port, name, tag)  

                    docker_images.append(docker_name)  

    except:

        traceback.print_exc()

    return docker_images

# imgs = getImageName(ip, port)

# for i in imgs:
#     print i

