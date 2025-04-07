from app.core.mysql import Service


# 优惠券用户
class Coupon_user(Service):
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
                "table": "coupon_user",
                # 分页大小
                "size": 10,
            }
        super(Coupon_user, self).__init__(config_temp)
