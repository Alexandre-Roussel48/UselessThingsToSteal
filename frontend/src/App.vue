<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/app/navbar.vue'
import Login from '@/components/app/login.vue'
import Register from '@/components/app/register.vue'
import Thefts from '@/components/app/thefts.vue'
</script>

<template>
  <header>
    <Navbar />
  </header>
  <main class="home_height has-background-info is-clipped" v-if="$store.getters.has_thefts">
    <Thefts/>
  </main>
  <main class="home_height has-background-info is-clipped" v-else-if="!$store.getters.is_connected">
    <section class="section">
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
  <RouterView v-else class="home_height has-background-info is-clipped"/>
</template>