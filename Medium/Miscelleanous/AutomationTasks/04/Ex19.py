# 19. Automate Notifications
import pushbullet


def sent_notification(api_key, title, body):
    pb = PushBullet(api_key)
    pb.push_note(title, body)
