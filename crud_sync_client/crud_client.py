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

    def find_one_payment_status_by_ended(self):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_concept_by_code = rpc.crud.find_one_payment_status_by_ended()
            return find_one_concept_by_code['data']['allPaymentStatuses'][0]

    def find_one_payment_status_by_error(self):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_concept_by_code = rpc.crud.find_one_payment_status_by_error()
            return find_one_concept_by_code['data']['allPaymentStatuses'][0]

    def update_necessity_concept_send_to_pay(self, id):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_concept_by_code = rpc.crud.update_necessity_concept_send_to_pay(id)
            return find_one_concept_by_code['data']['updateNecessityConcept']

    def update_user_token(self, user_id, token, token_franchise):
        with ClusterRpcProxy(self.config) as rpc:
            update_user_token = rpc.crud.update_user_token(user_id, token, token_franchise)
            return update_user_token['data']['updateUser']

    def update_payment_status_from_response(self, id, status_id, transaction_response, payment_date):
        with ClusterRpcProxy(self.config) as rpc:
            update_payment_status_from_response = rpc.crud.update_payment_status_from_response(id, status_id, transaction_response, payment_date)
            return update_payment_status_from_response['data']['updatePayment']

    def find_one_necessity_concept_status_by_completed(self):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_necessity_concept_status_by_completed = rpc.crud.find_one_necessity_concept_status_by_completed()
            return find_one_necessity_concept_status_by_completed['data']['allStatusConcepts'][0]

    def find_one_necessity_concept_status_by_in_progress(self):
        with ClusterRpcProxy(self.config) as rpc:
            find_one_necessity_concept_status_by_in_progress = rpc.crud.find_one_necessity_concept_status_by_in_progress()
            return find_one_necessity_concept_status_by_in_progress['data']['allStatusConcepts'][0]

    def update_necessity_status(self, id, status_id):
        with ClusterRpcProxy(self.config) as rpc:
            update_necessity_status = rpc.crud.update_necessity_status(id, status_id)
            return update_necessity_status['data']['updateNecessityConcept']