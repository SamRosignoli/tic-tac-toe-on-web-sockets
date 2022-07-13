<template>
  <table v-if="me">
    <tr>
      <td><p class="me-text" :class="{blinking: this.opponent && turn === me.name}">{{ me.name }} ({{ me.symbol }})</p></td>
      <td><p>stalemates</p></td>
      <td><p :class="{blinking: turn === opponentDisplay.name}">{{ opponentDisplay.name }} ({{ opponentDisplay.symbol }})</p></td>
    </tr>
    <tr>
      <td><p class="score-text">{{ me.games_won }}</p></td>
      <td><p class="score-text">{{ stalemates }}</p></td>
      <td><p class="score-text">{{ opponentDisplay.games_won }}</p></td>
    </tr>
  </table>
</template>
<script>
export default {
  name: 'ScoreBoard',
  props: ['me', 'opponent', 'games', 'turn'],
  computed: {
    stalemates () {
      return this.games - this.me.games_won - this.opponentDisplay.games_won;
    },
    opponentDisplay () {
      return this.opponent ? this.opponent : {
        name: '(waiting)',
        games_won: 0,
        symbol: '-'
      }
    }
  }
}
</script>

<style scoped>
  table {
    border: 2px solid #41b783;
    width: 450px;
    table-layout: fixed;
  }

  p {
    text-align: center;
    font-weight: 700;
  }

  .me-text {
    color: #41b783;
  }

  .score-text {
    font-size: 2rem;
  }

  .blinking {
    animation: blinker 1s linear infinite;
  }

  @keyframes blinker {
    50% {
      opacity: 0;
    }
  }
</style>