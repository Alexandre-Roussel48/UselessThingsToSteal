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
      let response = await fetch(`${this.$url_prefix}/api/user/get_inventory`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'authorization': 'Bearer ' + this.$store.state.token
        }
      });
      let cards = await response.json();
      const cardsMap = new Map();
      cards.forEach(card => {
        const key = `${card.id}-${card.name}-${card.rarity}`;
        if (cardsMap.has(key)) {
          const existingCard = cardsMap.get(key);
          existingCard.count++;
        } else {
          cardsMap.set(key, { ...card, count: 1 });
        }
      });
      return Array.from(cardsMap.values());
    }
  },
  async mounted () {
    this.inventory = await this.get_cards();
  }
}

</script>

<template>
  <main v-if="this.$store.getters.is_connected">
    <div class="header_long">
      <img src="@/assets/canister.svg" class="image-animation">
      <div class="has-background-info view-cover"></div>
      <img src="@/assets/inventory.svg">
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