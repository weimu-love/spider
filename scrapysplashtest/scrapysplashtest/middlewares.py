class HeaderMiddleware(object):

    def __init__(self, headers=None):
        headers = dict(headers)
        if headers:
            self.user_agent = headers.get('user-agent')
            self.cookie = headers.get('cookie')
            self.accept_language = headers.get('accept-language')
            self.accept = headers.get('accept')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(headers=crawler.settings.get('DEFAULT_REQUEST_HEADERS'))

    def process_request(self, request, spider):
        request.headers["user-agent"] = self.user_agent
        request.headers["accept-language"] = self.accept_language
        request.headers["cookie"] = self.cookie
        request.headers["accept"] = self.accept

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
