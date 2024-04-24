<script>

export default {
  name: 'drop'
}

</script>

<template>
  <main class="home_height has-background-info">
    <div v-if="this.$store.getters.is_connected">
      <div class="header_long">
        <img src="@/assets/drop.svg">
      </div>
    </div>
  </main>
</template>