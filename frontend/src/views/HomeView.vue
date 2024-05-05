<script>
import Tutorial from '@/components/home/tutorial.vue'

export default {
  name: 'home',
  components: {Tutorial}
}

</script>

<template>
  <main>
    <Tutorial v-if="this.$store.getters.is_first_time" />
  </main>
</template>