from nameko.standalone.rpc import ClusterRpcProxy


class LQNGraphQClient:
    def __init__(self, amqp_user, amqp_password, amqp_host, amqp_virtual_host):
        self.config = {
            "AMQP_URI": "amqp://{}:{}@{}/{}".format(amqp_user, amqp_password, amqp_host, amqp_virtual_host)
        }

    def find_one_concept_by_code(self, code):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_concept_by_code = rpc.crud.find_one_concept_by_code(code)
            user_id = find_one_concept_by_code['data']['allPaymentConcepts'][0]["id"]
            return user_id
