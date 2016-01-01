from lwpcms.moduling.moduling import LWPCMSModule
from lwpcms.api.constants import hooks


class SampleModule(LWPCMSModule):
    
    def __init__(self):
        super().__init__()

        self.register_event(hooks['layout_head'], self.layout_head)
        self.register_event(hooks['layout_footer'], self.layout_footer)
        self.register_event(hooks['post_publish'], self.post_publish)

    def layout_head(self, data):
        return '<script>console.log("test");</script>'

    def layout_footer(self, data):
        return '<div style="display:none;">SampleModule</div>'

    def post_publish(self, data):
        data['post'].title += ' ~ SampleModule'

module = SampleModule()
