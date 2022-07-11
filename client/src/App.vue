<template>
  <div id="app">
    <section class="app-view" v-if="!isLoading">

      <router-view v-if="isConnected" />

      <div class="app-connection-error" v-else>
        <h1>Oops! Something went wrong.</h1>
        <h2>Please try again in a few moments</h2>
      </div>

    </section>
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    isLoading() {
      return this.$store.getters.isLoading;
    },
    isConnected() {
      return this.$store.state.connected;
    }
  }
}
</script>


<style>
#app {
  font-family: 'Work Sans', sans-serif;
  color: #2c3e50;
}

.app-connection-error {
  text-align: center;
}
</style>
