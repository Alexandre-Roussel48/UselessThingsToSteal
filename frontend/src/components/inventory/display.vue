<script>

export default {
  name: 'inventory_display',
  props: ['card_data']
}

</script>

<template>
  <div class="card">
    <div class="card-image">
      <div class="count-circle">{{card_data['count']}}</div>
      <figure class="image">
        <img :src="'src/assets/cards/' + card_data.name + '.png'" alt="Card image"/>
      </figure>
    </div>
  </div>
</template>