<script>

export default {
  name: 'drop',
  data () {
    return {
      timer : -1,
      card : {}
    }
  },
  methods: {
    async drop() {
      fetch(`${this.$url_prefix}/api/user/drop`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'authorization': 'Bearer ' + this.$store.state.token
        }
      })
      .then(resp => resp.json())
      .then(drop_data => {
        if ('drop' in drop_data) {
          this.card = drop_data['drop'];
          this.$store.commit('set_next_card', {next_card: drop_data['next_card']});
          this.timer = this.$store.getters.next_card;
        }
      });
    },
    reset () {
      this.card = {};
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
    this.timer = this.$store.getters.next_card;
  }
}

</script>

<template>
  <main v-if="this.$store.getters.is_connected">
    <div class="header_long">
      <img src="@/assets/canister.svg" class="image-animation">
      <div class="has-background-info view-cover"></div>
      <img src="@/assets/drop.svg">
    </div>
    <div class="columns">
      <div class="column is-8 is-offset-2">
        <div class="box">
          <div class="columns is-multiline">
            <div class="column is-12">
              <h3 class="title" v-if="timer > 0">Next drop in {{Math.trunc(timer/60)}}:{{timer-Math.trunc(timer/60)*60}} ! 💵</h3>
              <h3 class="title" v-else>Next drop NOW ! 💵</h3>
            </div>
            <div class="column is-12 header_long">
              <button class="button is-large is-success" v-if="timer == 0" v-on:click.prevent="drop()">DROP</button>
              <button class="button is-large is-success" disabled v-else>DROP</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal is-active" v-if="Object.keys(this.card).length !== 0">
      <div class="modal-background"></div>
      <div class="modal-content drop_card_content" v-on:click.prevent="reset()">
        <div class="card drop_card">
          <div class="card-image">
            <figure class="image">
              <img :src="'src/assets/cards/' + card.name + '.png'" alt="Card image"/>
            </figure>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>