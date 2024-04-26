<script>

export default {
  name: 'me'
}

</script>

<template>
  <main>
    <div v-if="this.$store.getters.is_connected">
      <div class="header_long">
        <img src="@/assets/me.svg">
      </div>
    </div>
  </main>
</template>