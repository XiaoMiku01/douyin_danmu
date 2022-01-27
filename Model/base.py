
class Base:

    instance = None

    def set_payload(self, payload):
        self.instance.ParseFromString(payload)

    def extra_info(self):
        return dict()

    def user(self):
        if(hasattr(self.instance, 'user')):
            return self.instance.user

        return None

    def __str__(self):
        pass
