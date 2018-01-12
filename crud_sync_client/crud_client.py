from nameko.standalone.rpc import ClusterRpcProxy


class LQNConceptsGraphQClient:
    def __init__(self, amqp_user, amqp_password, amqp_host, amqp_virtual_host):
        self.config = {
            "AMQP_URI": "amqp://{}:{}@{}/{}".format(amqp_user, amqp_password, amqp_host, amqp_virtual_host)
        }

    def get_user_id_remax(self):
        with ClusterRpcProxy(self.config) as rpc:
            find_remax_default_user = rpc.crud.find_remax_default_user()
            user_id = find_remax_default_user['data']['allUsers'][0]["id"]
            return user_id
