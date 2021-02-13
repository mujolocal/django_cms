from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from polls.views import PollListView, PollDetailView


@apphook_pool.register
class PollsApphook(CMSApp):
    app_name = "polls"
    name = _("Polls Application")

    # def get_urls(self, page=None, Language=None, **kwargs):
    #     return ["polls.urls"]

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            url(r'^$', PollListView.as_view()),
            url(r'^(?P<slug>[\w-]+)/?$', PollDetailView.as_view()),
        ]
