import json
from rospy_message_converter import message_converter

def convert_json_to_ros_message(message_type, json_message):
    """
    Takes in the message type and a JSON-formatted string and returns a ROS
    message.

    Example:
        message_type = "std_msgs/String"
        json_message = '{"data": "Hello, Robot"}'
        ros_message = convert_json_to_ros_message(message_type, json_message)
    """
    dictionary = json.loads(json_message)
    if dictionary.has_key("topic_name"):
        del dictionary["topic"]
    if dictionary.has_key("msg_typ"):
        del dictionary["msg_type"]
    return message_converter.convert_dictionary_to_ros_message(message_type, dictionary)

def convert_ros_message_to_json(message, topic_name="", msg_type=""):
    """
    Takes in a ROS message and returns a JSON-formatted string.

    Example:
        ros_message = std_msgs.msg.String(data="Hello, Robot")
        json_message = convert_ros_message_to_json(ros_message)
    """
    dictionary = message_converter.convert_ros_message_to_dictionary(message)
    if topic_name:
        dictionary["topic_name"]=topic_name
    if msg_type:
        dictionary["msg_type"]=msg_type
    json_message = json.dumps(dictionary)
    return json_message
