from app.core.mysql import Service


# 电器商城服务
class Digital_mall(Service):
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
                "table": "digital_mall",
                # 分页大小
                "size": 30,
                "page": 1,
            }
        super(Digital_mall , self).__init__(config_temp)
