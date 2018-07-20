"""Event module."""


class Event(object):
    def __init__(self, *args, **kwargs):
        """
        channel: raw.SUBSCRIBE[1],
        type: parsed.type,
        messageID: parsed.messageID,
        avatarURL: parsed.avatarURL,
        username: parsed.username,
        userPK: parsed.userPK,
        text: parsed.text,
        timestamp : parsed.timestamp,
        """

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __iter__(self):
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                yield key, value

    def __repr__(self):
        return ";".join("{}::{}".format(k, v) for k, v in self)
