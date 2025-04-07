from app.core import controller

controllerClass = getattr(controller, "Controller")


# 物流
class Logistics_delivery(controllerClass):
    def __init__(self, config={}):
        """
        构造函数
        @param {Object} config 配置参数
        """
        config_init = {
            # 选择的模板那路径模板
            "tpl": "./logistics_delivery/",
            # 选择的服务
            "service": "logistics_delivery",
        }
        config_temp = config
        config_temp.update(config_init)
        super(Logistics_delivery, self).__init__(config_temp)
