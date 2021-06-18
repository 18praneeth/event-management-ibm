import slack
from event_management.settings import SLACK_TOKEN


def send_slack_message(event_object):
    message = {
        "channel": "#project",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f"{event_object.session_topic_name}",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"A new Event has been created!!\n :calendar: {event_object.date}\n\n *Please view in the website.*"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Event Link",
                            "emoji": True
                        },
                        "url": f"http://127.0.0.1:8000/signup-event/{event_object.id}"
                    }
                ]
            }
	    ]
    }

    client_obj = slack.WebClient(token=SLACK_TOKEN)
    client_obj.chat_postMessage(**message)