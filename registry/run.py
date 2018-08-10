# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-07-27 21:45:01
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-10 09:28:24

# flask用法，导入app模块下__init__.py的app实例
from app import app


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)