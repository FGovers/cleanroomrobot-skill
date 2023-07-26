from mycroft import MycroftSkill, intent_file_handler


class Cleanroomrobot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cleanroomrobot.intent')
    def handle_cleanroomrobot(self, message):
        self.speak_dialog('cleanroomrobot')


def create_skill():
    return Cleanroomrobot()

