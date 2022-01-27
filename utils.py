# from Model.member import MemberMessage
import Model.member
from Model.like import LikeMessage
from Model.roomuserseq import RoomUserSeqMessage
from Model.gift import GiftMessage
from Model.social import SocialMessage
from Model.chat import ChatMessage


def decodeMsg(messages):
    for message in messages:
        try:
            if message.method == 'WebcastMemberMessage':
                member_message = Model.member.MemberMessage()
                member_message.set_payload(message.payload)
                print(member_message)

            elif message.method == 'WebcastSocialMessage':
                social_message = SocialMessage()
                social_message.set_payload(message.payload)
                print(social_message)

            elif message.method == 'WebcastChatMessage':
                chat_message = ChatMessage()
                chat_message.set_payload(message.payload)
                print(chat_message)

            elif message.method == 'WebcastLikeMessage':
                like_message = LikeMessage()
                like_message.set_payload(message.payload)
                print(like_message)

            elif message.method == 'WebcastGiftMessage':
                gift_message = GiftMessage()
                gift_message.set_payload(message.payload)
                print(gift_message)

            elif message.method == 'WebcastRoomUserSeqMessage':
                room_user_seq_message = RoomUserSeqMessage()
                room_user_seq_message.set_payload(message.payload)
                print(room_user_seq_message)

        except Exception as e:
            print(e)
