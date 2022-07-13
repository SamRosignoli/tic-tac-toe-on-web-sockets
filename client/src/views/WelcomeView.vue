<template>
  <div class="home-view">
    <h1>Welcome to Tic Tac Toe on SocketIO!</h1>
    <form>
      <label for="nickname">Nickname:</label><br>
      <input type="text" id="nickname" name="nickname" v-model="formNickname"><br>
      <label for="Room">Room:</label><br>
      <input id="room" name="room"  v-model="formRoom"><br><br>
      <input type="submit" value="Submit" @click.prevent="submitForm">
    </form>
    <p class="error-text" v-if="joinErrorMessage.length">{{ joinErrorMessage }}</p>
  </div>
</template>

<script>
export default {
  name: "WelcomeView",
  data() {
    return {
      formNickname: "",
      formRoom: ""
    }
  },
  computed: {
    joinErrorMessage() {
      return this.$store.state.joinErrorMessage;
    }
  },
  methods: {
    submitForm() {
      if (!this.formNickname.length || !this.formRoom.length) {
        this.errorMessage = "Please provide a nickname and a room";
        return;
      }

      const data = { nickname: this.formNickname, room: this.formRoom };
      this.$socket.emit('joinRoom', data);
    }
  }
}
</script>
