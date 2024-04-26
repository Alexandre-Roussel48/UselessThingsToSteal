<script>

export default {
  name: 'drop'
}

</script>

<template>
  <main>
    <div v-if="this.$store.getters.is_connected">
      <div class="header_long">
        <img src="@/assets/drop.svg">
      </div>
    </div>
  </main>
</template>