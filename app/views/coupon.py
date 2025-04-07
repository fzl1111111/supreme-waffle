from app.core import controller

controllerClass = getattr(controller, "Controller")


# 优惠券
class Coupon(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./coupon/",
            # 选择的服务
            "service": "coupon",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Coupon, self).__init__(config_temp)
