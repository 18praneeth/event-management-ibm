from asyncio import events
import slack
from event_management.settings import SLACK_TOKEN
from django.core.mail import send_mail


def send_slack_message(event_object):
    message = {
        "channel": "#project",
        "blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "A new event is created",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"`Date:` {event_object.date}\n`Event activity mode:`{event_object.event_activity_type}\n`Technology tracks:`{event_object.technology_tracks}\n`Event activity mode:`{event_object.event_activity_mode}\n`Session topic name:`{event_object.session_topic_name}\n `Session duration:`{event_object.session_duration}\n"
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
					"value": "click_me_123",
					"url": f"http://127.0.0.1:8000/signup-event/{event_object.id}"
				}
			]
		}
	]
    }

    client_obj = slack.WebClient(token=SLACK_TOKEN)
    client_obj.chat_postMessage(**message)


def send_mail_assigned(assigned_list, event_object):

	content =  f"Date: {event_object.date}\nEvent activity mode:{event_object.event_activity_type}\nTechnology tracks:{event_object.technology_tracks}\nEvent activity mode:{event_object.event_activity_mode}\nSession topic name:{event_object.session_topic_name}\n Session duration:{event_object.session_duration}\n"


	send_mail(
		'Event is assigned!!',
		content,
		'from@example.com',
		assigned_list,
		fail_silently=False,
	)