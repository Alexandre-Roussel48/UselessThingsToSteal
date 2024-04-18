<script>

import Login from '@/components/home/login.vue'
import Register from '@/components/home/register.vue'

export default {
  name: 'home',
  components: {Login, Register}
}

</script>

<template>
  <main class="home_height has-background-info">
    <section class="section" v-if="!this.$store.getters.is_connected">
      <div class="columns">
        <div class="column is-3 is-offset-3">
          <Login />
        </div>
        <div class="column is-3">
          <Register />
        </div>
      </div>
    </section>
  </main>
</template>