<template>
  <div class="home-view">
    <h1>Welcome to Tic Tac Toe on Sockets!</h1>
    <form>
      <label for="nickname">Nickname:</label><br>
      <input class="text-input" type="text" id="nickname" name="nickname" v-model="formNickname"><br><br>

      <label for="room">Room name:</label><br>
      <input class="text-input" type="text" id="room" name="room" v-model="formRoom"><br><br>

      <input type="submit" value="Go!" @click.prevent="submitForm">
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

<style scoped>
.home-view {
  text-align: center;
}

label {
  font-weight: 700;
}

input {
  font-size: 1.3rem;
  border-radius: 5px;
}

input[type=text] {
  border: 1px solid #aaa;
  padding: 3px;
  background: #fff;
  transition: 0.5s ease;
  color: #2c3e50;
}

input[type=text]:hover {
  background: #eee;
}

input[type=submit] {
  background: #41b783;
  border: none;
  padding: 5px 25px;
  color: #fff;
  transition: 0.5s ease;
  cursor: pointer;
}

input[type=submit]:hover {
  background: #278c60;
}
</style>