<script>

import Login from '@/components/home/login.vue'
import Register from '@/components/home/register.vue'
import Tutorial from '@/components/home/tutorial.vue'

export default {
  name: 'home',
  components: {Login, Register, Tutorial}
}

</script>

<template>
  <main>
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
    <section v-else>
      <Tutorial v-if="this.$store.getters.is_first_time" />
    </section>
  </main>
</template>