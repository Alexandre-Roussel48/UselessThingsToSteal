<script>

export default {
  name: 'vault'
}

</script>

<template>
  <main>
    <div v-if="this.$store.getters.is_connected">
      <div class="header_long">
        <img src="@/assets/vault.svg">
      </div>
    </div>
  </main>
</template>