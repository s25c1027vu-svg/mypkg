import rclpy
from rclpy.node import Node
from person_msgs.msg import Person   #変更: 作ったPerson型を使う

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)   #変更: 型とトピック名
n = 0


def cb():
    global n
    msg = Person()          #変更: Person型のメッセージを作る
    msg.name = "勝野"    #変更: msgファイルに書いた「name」
    msg.age = n % 256       #変更: msgファイルに書いた「age」（0〜255まで）
    pub.publish(msg)
    n += 1
