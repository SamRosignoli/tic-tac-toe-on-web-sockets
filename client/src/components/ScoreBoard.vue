<template>
  <table v-if="me">
    <tr>
      <td>{{ me.name }} ({{ me.symbol }})</td>
      <td>stalemates</td>
      <td>{{ opponentDisplay.name }} ({{ opponentDisplay.symbol }})</td>
    </tr>
    <tr>
      <td>{{ me.games_won }}</td>
      <td>{{ stalemates }}</td>
      <td>{{ opponentDisplay.games_won }}</td>
    </tr>
  </table>
</template>
<script>
export default {
  name: 'ScoreBoard',
  props: ['me', 'opponent', 'games'],
  computed: {
    stalemates () {
      return this.games - this.me.games_won - this.opponentDisplay.games_won;
    },
    opponentDisplay () {
      return this.opponent ? this.opponent : {
        name: '(waiting opponent)',
        games_won: 0,
        symbol: '-'
      }
    }
  }
}
</script>