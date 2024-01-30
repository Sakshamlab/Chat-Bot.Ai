css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #3D3B40
}
.chat-message.bot {
    background-color: #A6E3E9
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/premium-vector/robot-icon-chat-bot-sign-support-service-concept-chatbot-character-flat-style_41737-796.jpg?w=740">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/premium-photo/face-smiling-indian-man_130568-534.jpg?w=740">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''