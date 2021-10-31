#  1.在items中定义图片的字段名称为 image_urls（不能随便修改这个字段名称）
#  2.在spiders中，向item['image_urls']中填写待下载图片的url地址，必须是列表格式
#  3.在settings中配置IMAGES_STORE
#  4.在settings中添加管道
#       ITEM_PIPELINES = {
#           'scrapy.pipelines.images.ImagesPipeline': 300
#       }


#  修改文件的保存目录
#  1. 前面的操作和上面一样
#  2. 自定义图片的保存管道，继承自 ImagesPipeline
#  3. 重写自定义管道中的file_path方法，删掉full/，这样下载的图片就会保存在IMAGES_STORE所定义的文件目录中
#  4. 在settings中指定管道为自定义的管道


#  修改文件的名称
#  1.在修改保存目录操作的基础上
#  2. 重写get_media_requests方法，把文件的名称以meta的方式传递到请求中
#  3. 在file_path方法中用request.meta.get('name') 获取想要保存的文件名称
#  4. 拼接图片的名称
