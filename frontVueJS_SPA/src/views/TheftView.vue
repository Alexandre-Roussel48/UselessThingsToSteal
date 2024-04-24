<script>

export default {
  name: 'theft'
}

</script>

<template>
  <main class="home_height has-background-info">
    <div v-if="this.$store.getters.is_connected">
      <div class="header_long">
        <img src="@/assets/theft.svg">
      </div>
    </div>
  </main>
</template>