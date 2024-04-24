<script>

import Display from '@/components/inventory/display.vue'

export default {
  name: 'inventory',
  components: {Display},
  data () {
    return {
      inventory: []
    }
  },
  methods: {
    async get_cards() {
      let response = await fetch(`${this.$url_prefix}/inventory/get_cards`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'Authorization': this.$store.state.token
        }
      });
      return await response.json();
    }
  },
  async mounted () {
    this.inventory = await this.get_cards();
  }
}

</script>

<template>
  <main>
    <div v-if="this.$store.getters.is_connected">
      <div class="header_long">
        <img src="@/assets/inventory.svg">
      </div>
    </div>
    <div class="columns">
      <div class="column is-10 is-offset-1">
        <div class="columns is-multiline">
          <div class="column is-1"></div>
          <div class="column is-2" v-for="card in this.inventory">
            <Display :card_data="card"/>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>