<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/app/navbar.vue'
</script>

<template>
  <header>
    <Navbar />
  </header>
  <RouterView class="home_height has-background-info is-clipped"/>
</template>