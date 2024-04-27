<script>

export default {
  name: 'theft',
  data () {
    return {
      timer : -1,
      card : {}
    }
  },
  methods: {
    async theft() {
      let response = await fetch(`${this.$url_prefix}/user/theft`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'Authorization': this.$store.state.token
        }
      });
      this.card = await response.json();
    }
  },
  watch: {
    timer: {
      handler(value) {
        if (value > 0) {
          setTimeout(() => {
            this.timer--;
          }, 1000);
        }
      },
      immediate: true
    }
  },
  mounted () {
    this.timer = this.$store.getters.next_theft;
  }
}

</script>

<template>
  <main v-if="this.$store.getters.is_connected">
    <div class="header_long">
      <img src="@/assets/canister.svg" class="image-animation">
      <div class="has-background-info view-cover"></div>
      <img src="@/assets/theft.svg">
    </div>
    <div class="columns">
      <div class="column is-8 is-offset-2">
        <div class="box">
          <div class="columns is-multiline">
            <div class="column is-12">
              <h3 class="title" v-if="timer > 0">Next theft in {{Math.trunc(timer/60)}}:{{timer-Math.trunc(timer/60)*60}} ! 🥷</h3>
              <h3 class="title" v-else>Next theft NOW ! 🥷</h3>
            </div>
            <div class="column is-12 header_long">
              <button class="button is-large is-success" v-if="timer == 0" v-on:click.prevent="theft()">THEFT</button>
              <button class="button is-large is-success" disabled v-else>THEFT</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>