from app.core.mysql import Service


# 物流
class Logistics_delivery(Service):
    def __init__(self, *config):
        """
        构造函数
        @param {Object} config 配置参数
        """
        if config:
            config_temp = config[0]
        else:
            config_temp = {
                # 操作的表
                "table": "logistics_delivery",
                # 分页大小
                "size": 10,
            }
        super(Logistics_delivery, self).__init__(config_temp)
