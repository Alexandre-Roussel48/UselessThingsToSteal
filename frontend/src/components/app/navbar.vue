<script>

export default {
  name: 'app_navbar',
  methods: {
    logout() {
      this.$store.getters.get_ws.close();
      this.$store.commit('set_user_data', {
        username: "",
        token: ""
      });
      this.$store.commit('set_next_card', {
        next_card: ""
      });
      this.$store.commit('set_next_theft', {
        next_theft: ""
      });
      this.$store.commit('set_thefts', {
        thefts: []
      });
      this.$router.push('/');
    }
  }
}

</script>

<template>
  <nav class="navbar has-background-primary" role="navigation" aria-label="main navigation" v-if="this.$store.getters.is_connected">
    <div class="navbar-brand">
      <RouterLink to="/" class="navbar-item">
        <img class="header_logo" src="@/assets/favicon.svg">
      </RouterLink>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start">
        <RouterLink to="/inventory" class="navbar-item">
          <img class="header_category" src="@/assets/inventory.svg">
        </RouterLink>
        <RouterLink to="/vault" class="navbar-item">
          <img class="header_category" src="@/assets/vault.svg">
        </RouterLink>
        <RouterLink to="/forge" class="navbar-item">
          <img class="header_category" src="@/assets/forge.svg">
        </RouterLink>
      </div>
      <div class="navbar-end">
        <RouterLink to="/theft" class="navbar-item">
          <img class="header_category" src="@/assets/theft.svg">
        </RouterLink>
        <RouterLink to="/drop" class="navbar-item">
          <img class="header_category" src="@/assets/drop.svg">
        </RouterLink>
        <RouterLink to="/me" class="navbar-item">
          <img class="header_category" src="@/assets/me.svg">
        </RouterLink>
        <div class="navbar-item">
          <button class="button is-success" v-on:click.prevent="logout()">
            <span>Log out</span>
          </button>
        </div>
      </div>
    </div>
  </nav>
  <nav class="header_long has-background-primary" v-else>
    <img src="@/assets/long.svg">
  </nav>
</template>