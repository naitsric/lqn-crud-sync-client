from nameko.standalone.rpc import ClusterRpcProxy


class LQNGraphQClient:
    def __init__(self, amqp_user, amqp_password, amqp_host, amqp_virtual_host):
        self.config = {
            "AMQP_URI": "amqp://{}:{}@{}/{}".format(amqp_user, amqp_password, amqp_host, amqp_virtual_host)
        }

    def find_one_concept_by_code(self, code):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_concept_by_code = rpc.crud.find_one_concept_by_code(code)
            return find_one_concept_by_code['data']['allPaymentConcepts'][0]

    def find_one_payment_status_by_default(self):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_concept_by_code = rpc.crud.find_one_payment_status_by_default()
            return find_one_concept_by_code['data']['allPaymentStatuses'][0]

    def update_necessity_concept_send_to_pay(self, id):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_concept_by_code = rpc.crud.update_necessity_concept_send_to_pay(id)
            return find_one_concept_by_code['data']['updateNecessityConcept']

    def update_user_token(self, user_id, token, token_franchise):
        with ClusterRpcProxy(self.config) as rpc:
            update_user_token = rpc.crud.update_user_token(user_id, token, token_franchise)
            return update_user_token['data']['updateUser']