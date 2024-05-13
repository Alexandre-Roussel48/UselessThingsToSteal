<script>

import Display from '@/components/vault/display.vue'

export default {
  name: 'vault',
  components: {Display},
  data () {
    return {
      vault: []
    }
  },
  methods: {
    async get_vault() {
      let response = await fetch(`${this.$url_prefix}/api/user/get_vault`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json',
          'authorization': 'Bearer ' + this.$store.state.token
        }
      });
      this.vault = await response.json();
    }
  },
  async mounted () {
    await this.get_vault();
  }
}

</script>

<template>
  <main>
    <div class="header_long">
      <img src="@/assets/canister.svg" class="image-animation">
      <div class="has-background-info view-cover"></div>
      <img src="@/assets/vault.svg">
    </div>
    <div class="columns">
      <div class="column is-10 is-offset-1">
        <div class="columns is-multiline">
          <div class="column is-1"></div>
          <div class="column is-2" v-for="card in this.vault">
            <Display :card_data="card" @rerender="get_vault"/>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>