<script>

export default {
  name: 'inventory_display',
  props: ['card_data'],
  methods: {
    async vault() {
      await fetch(`${this.$url_prefix}/api/user/vault_card`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'authorization': 'Bearer ' + this.$store.state.token
        },
        body: JSON.stringify({
          'card':this.card_data
        })
      })
      .then(response => {
        this.$emit('rerender');
      });
    },
    async forge() {
      await fetch(`${this.$url_prefix}/api/user/forge_card`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'authorization': 'Bearer ' + this.$store.state.token
        },
        body: JSON.stringify({
          'card':this.card_data
        })
      })
      .then(response => {
        this.$emit('rerender');
      });
    }
  }
}

</script>

<template>
  <div class="card">
    <div class="card-image">
      <button class="vault-circle" v-on:click.prevent="vault()">
        <span class="icon has-text-success">
          <font-awesome-icon :icon="['fas', 'toolbox']" />
        </span>
      </button>
      <button class="forge-circle" v-on:click.prevent="forge()">
        <span class="icon has-text-success">
          <font-awesome-icon :icon="['fas', 'hammer']" />
        </span>
      </button>
      <div class="count-circle">{{card_data['count']}}</div>
      <figure class="image">
        <img :src="'src/assets/cards/' + card_data.name + '.png'" alt="Card image"/>
      </figure>
    </div>
  </div>
</template>