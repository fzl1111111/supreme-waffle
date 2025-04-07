from app.core import controller

controllerClass = getattr(controller, "Controller")


# 优惠券用户
class Coupon_user(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./coupon_user/",
            # 选择的服务
            "service": "coupon_user",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Coupon_user, self).__init__(config_temp)
