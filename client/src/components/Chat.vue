<template>
  <div class="chat">
    <h3>Messages</h3>
    <div class="message-list">
      <p v-for="(message, index) in messages" :key="index">{{ message.nickname }}: {{ message.message }}</p>
    </div>
    <div class="message-form">
      <input type="text" placeholder="Your message" v-model="message" />
      <button @click="sendMessage" :disabled="!this.message.length">Send</button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Chat',
  props: ['messages'],
  data() {
    return {
      message: ""
    }
  },
  methods: {
    sendMessage() {
      this.$emit('send-message', this.message);
    }
  }
}
</script>

<style scoped>
  h3 {
    margin-top: 0;
  }

  .message-list {
    border: 1px solid;
    width: 400px;
    height: 300px;
  }
</style>