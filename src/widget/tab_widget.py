from PyQt5.QtWidgets import QWidget

class TabWidget(QWidget):
    def get_login_label_text(self):
        if self.api.is_authenticated():
            return "Logged in as: {}".format(self.api.get_login_name())
        if self.api.has_access_token():
            return "Access token has expired. Please login again."
        return "User has not logged in."

    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api
