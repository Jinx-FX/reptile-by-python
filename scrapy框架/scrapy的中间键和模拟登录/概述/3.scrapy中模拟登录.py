#  scrapy中模拟登录：两种方法

#  找到 post 登录接口，构造表单数据，构造POST请求对象，传递参数

#  使用cookie，访问登录以后的页面，把cookie作为参数传递到Request对象中

#  重写start_requests方法

#  scrapy中默认支持cookie持久化，只需要传递一次cookie或者模拟登录一次(post)，后续所有请求默认都会带入cookie

#  dont_filter:不过滤请求，默认为False，就是会过滤相同的请求
